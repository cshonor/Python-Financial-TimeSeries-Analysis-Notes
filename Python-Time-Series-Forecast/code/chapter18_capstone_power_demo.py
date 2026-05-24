"""
《Python 时间序列预测》第 18 章配套：家庭用电量 DL 顶点项目
清洗 / 小时重采样 / FFT 日季节 / DataWindow / 七大模型 MAE 对比

运行：
  python Python-Time-Series-Forecast/code/chapter18_capstone_power_demo.py

依赖：pip install numpy pandas
推荐：pip install tensorflow scikit-learn  (Python 3.10–3.12)
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
np.random.seed(SEED)

TARGET = "Global_active_power"
OUT_STEPS = 24
INPUT_LSTM = 24
KERNEL_WIDTH = 3
INPUT_CNN = OUT_STEPS + KERNEL_WIDTH - 1  # 26
BATCH = 32
MAX_EPOCHS = 25
PATIENCE = 3
FAST_HOURS = 5_000  # book ~34949; reduce for demo speed

BOOK_TEST_MAE = {
    "baseline_last": None,
    "baseline_seasonal": None,
    "linear": None,
    "dnn": None,
    "lstm": None,
    "cnn": None,
    "cnn_lstm": None,
    "arlstm": 0.074,
}

_CODE = Path(__file__).resolve().parent


def _load_ch13():
    spec = importlib.util.spec_from_file_location("ch13", _CODE / "chapter13_data_window_baseline_demo.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def _load_ch17_ar_builder(tf):
    spec = importlib.util.spec_from_file_location("ch17", _CODE / "chapter17_arlstm_demo.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod.build_autoregressive_model(tf, units=32, out_steps=OUT_STEPS)


ch13 = _load_ch13()
DataWindow = ch13.DataWindow
eval_baseline = ch13.eval_baseline


def minute_raw(n_minutes: int, seed: int = SEED) -> pd.DataFrame:
    """Synthetic minute-level household power (UCI-like columns)."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2006-12-16", periods=n_minutes, freq="min")
    gap = np.maximum(0.1, 0.5 + 0.3 * np.sin(2 * np.pi * np.arange(n_minutes) / (24 * 60)))
    sm1 = rng.choice([0.0, 0.0, 1.0], n_minutes) * rng.uniform(0, 2, n_minutes)
    sm2 = rng.uniform(0, 3, n_minutes)
    sm3 = np.full(n_minutes, np.nan)
    sm3[10000:17226] = np.nan  # long gap -> drop column per book
    power = 0.8 + 0.4 * np.sin(2 * np.pi * np.arange(n_minutes) / (24 * 60) - 1)
    power += rng.normal(0, 0.15, n_minutes)
    return pd.DataFrame(
        {
            "Global_active_power": np.maximum(power, 0.05),
            "Global_reactive_power": rng.uniform(0.1, 0.5, n_minutes),
            "Sub_metering_1": sm1,
            "Sub_metering_2": sm2,
            "Sub_metering_3": sm3,
            "gap": gap,
        },
        index=idx,
    )


def preprocess(raw: pd.DataFrame) -> pd.DataFrame:
    print("=== 18.2.1 drop Sub_metering_3 (long missing block) ===")
    df = raw.drop(columns=["Sub_metering_3"], errors="ignore").copy()
    print("=== 18.2.2 astype float64 ===")
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(how="all")
    print("=== 18.2.3 resample hourly sum ===")
    hourly = df.resample("h").sum()
    hourly = hourly.dropna(subset=[TARGET])
    print(f"hourly rows: {len(hourly)} (book ~34949)")
    return hourly


def fft_daily_peak(hourly: pd.Series) -> None:
    print("\n=== 18.3.2 FFT daily seasonality ===")
    y = hourly.values - hourly.values.mean()
    spec = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(len(y), d=1.0)
    if len(freqs) > 1:
        daily_idx = np.argmin(np.abs(freqs - 1 / 24))
        weekly_idx = np.argmin(np.abs(freqs - 1 / (24 * 7)))
        print(f"amplitude@daily (~1/24h): {spec[daily_idx]:.2f}")
        print(f"amplitude@weekly:        {spec[weekly_idx]:.2f} (book: daily dominates)")


def cyclic_hour(index: pd.DatetimeIndex) -> pd.DataFrame:
    hour = index.hour + index.minute / 60
    rad = 2 * np.pi * hour / 24
    return pd.DataFrame({"sin_day": np.sin(rad), "cos_day": np.cos(rad)}, index=index)


def build_matrix(hourly: pd.DataFrame) -> pd.DataFrame:
    print("\n=== 18.3.1 drop Sub_metering_1 (mostly zeros) ===")
    drop = ["Sub_metering_1"]
    use = [c for c in hourly.columns if c not in drop]
    desc = hourly[use].describe()
    print(desc.loc["75%", ["Sub_metering_2", TARGET]].round(3))
    cyc = cyclic_hour(hourly.index)
    feat = pd.concat([cyc, hourly[[c for c in use if c != TARGET]], hourly[[TARGET]]], axis=1)
    return feat


def temporal_split(df: pd.DataFrame, train=0.7, val=0.2):
    n = len(df)
    n_tr = int(n * train)
    n_va = int(n * val)
    return df.iloc[:n_tr], df.iloc[n_tr : n_tr + n_va], df.iloc[n_tr + n_va :]


def scale(train, val, test, cols):
    try:
        from sklearn.preprocessing import MinMaxScaler

        sc = MinMaxScaler()
        return sc.fit_transform(train[cols]), sc.transform(val[cols]), sc.transform(test[cols]), sc
    except ImportError:
        mn, mx = train[cols].min(), train[cols].max()
        denom = (mx - mn).replace(0, 1)

        def tr(x):
            return ((x[cols] - mn) / denom).to_numpy()

        return tr(train), tr(val), tr(test), None


def target_idx(cols: list[str]) -> int:
    return cols.index(TARGET)


def baseline_repeat_last(inputs: np.ndarray, label_width: int, tidx: int) -> np.ndarray:
    x = ch13._as_batch(inputs)
    last = x[:, -1, tidx]
    return np.tile(last[:, None], (1, label_width))


def baseline_repeat_season(inputs: np.ndarray, label_width: int, tidx: int) -> np.ndarray:
    x = ch13._as_batch(inputs)
    return x[:, -label_width:, tidx]


def try_import_tf():
    try:
        import tensorflow as tf

        tf.random.set_seed(SEED)
        return tf
    except ImportError:
        return None


def compile_and_fit(model, train_ds, val_ds, tf):
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=MAX_EPOCHS,
        callbacks=[
            tf.keras.callbacks.EarlyStopping(
                monitor="val_loss", patience=PATIENCE, restore_best_weights=True
            )
        ],
        verbose=0,
    )


def val_mae(model, val_ds) -> float:
    _, mae = model.evaluate(val_ds, verbose=0)
    return float(mae)


def build_models(tf, n_features: int, tidx: int):
    """Keras builders for linear, DNN, LSTM, CNN, CNN+LSTM."""
    models = {}

    models["linear"] = tf.keras.Sequential(
        [
            tf.keras.layers.Input((INPUT_LSTM, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(OUT_STEPS),
        ]
    )

    models["dnn"] = tf.keras.Sequential(
        [
            tf.keras.layers.Input((INPUT_LSTM, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(OUT_STEPS),
        ]
    )

    models["lstm"] = tf.keras.Sequential(
        [
            tf.keras.layers.Input((INPUT_LSTM, n_features)),
            tf.keras.layers.LSTM(32, return_sequences=True),
            tf.keras.layers.Dense(1),
            tf.keras.layers.Reshape((OUT_STEPS,)),
        ]
    )

    models["cnn"] = tf.keras.Sequential(
        [
            tf.keras.layers.Input((INPUT_CNN, n_features)),
            tf.keras.layers.Conv1D(32, KERNEL_WIDTH, padding="same", activation="relu"),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(OUT_STEPS),
        ]
    )

    models["cnn_lstm"] = tf.keras.Sequential(
        [
            tf.keras.layers.Input((INPUT_CNN, n_features)),
            tf.keras.layers.Conv1D(32, KERNEL_WIDTH, padding="same", activation="relu"),
            tf.keras.layers.LSTM(32, return_sequences=True),
            tf.keras.layers.Dense(1),
            tf.keras.layers.Reshape((OUT_STEPS,)),
        ]
    )

    models["arlstm"] = _load_ch17_ar_builder(tf)
    return models


def main() -> None:
    print("=== 18.1 household power capstone (synthetic UCI-like) ===")
    minutes = FAST_HOURS * 60
    hourly = preprocess(minute_raw(minutes))
    if len(hourly) > FAST_HOURS:
        hourly = hourly.iloc[:FAST_HOURS]

    fft_daily_peak(hourly[TARGET])
    matrix = build_matrix(hourly)
    cols = list(matrix.columns)
    tidx = target_idx(cols)
    train, val, test = temporal_split(matrix)
    X_tr, X_va, X_te, _ = scale(train, val, test, cols)
    print(f"\n=== 18.3.3 split train={len(X_tr)} val={len(X_va)} test={len(X_te)} ===")

    w24 = DataWindow(INPUT_LSTM, OUT_STEPS, INPUT_LSTM, X_tr, X_va, (tidx,), BATCH)
    w26 = DataWindow(INPUT_CNN, OUT_STEPS, INPUT_CNN, X_tr, X_va, (tidx,), BATCH)

    print("\n=== 18.5.1 baselines (val MAE) ===")
    _, mae_last = eval_baseline(
        w24, X_va, lambda inp: baseline_repeat_last(inp, OUT_STEPS, tidx)
    )
    _, mae_seas = eval_baseline(
        w24, X_va, lambda inp: baseline_repeat_season(inp, OUT_STEPS, tidx)
    )
    print(f"repeat last value:    {mae_last:.4f}")
    print(f"repeat last 24h curve:{mae_seas:.4f}")

    results = {"baseline_seasonal": mae_seas, "baseline_last": mae_last}

    tf = try_import_tf()
    if tf is None:
        print("\nTensorFlow not available — book test MAE champion: ARLSTM = 0.074")
        print("Install tensorflow (Python 3.10–3.12) to train all seven models.")
        print("=== 18.6 next: ch.19 Prophet ===")
        return

    print("\n=== 18.4 seed=42 | compile_and_fit MSE+MAE EarlyStopping ===")
    builders = build_models(tf, len(cols), tidx)
    train24 = w24.make_tf_dataset(X_tr, shuffle=True)
    val24 = w24.make_tf_dataset(X_va, shuffle=False)
    train26 = w26.make_tf_dataset(X_tr, shuffle=True)
    val26 = w26.make_tf_dataset(X_va, shuffle=False)

    for name in ("linear", "dnn", "lstm"):
        m = builders[name]
        compile_and_fit(m, train24, val24, tf)
        results[name] = val_mae(m, val24)
        print(f"18.5.x {name:10s} val MAE: {results[name]:.4f}")

    for name in ("cnn", "cnn_lstm"):
        m = builders[name]
        compile_and_fit(m, train26, val26, tf)
        results[name] = val_mae(m, val26)
        print(f"18.5.x {name:10s} val MAE: {results[name]:.4f}")

    ar = builders["arlstm"]
    compile_and_fit(ar, train24, val24, tf)
    results["arlstm"] = val_mae(ar, val24)
    print(f"18.5.7 arlstm      val MAE: {results['arlstm']:.4f}  (book test ~0.074)")

    best = min(results, key=results.get)
    print(f"\n=== 18.5.8 best in this run: {best} ({results[best]:.4f}) ===")
    print("=== 18.6 DL capstone done -> ch.19 Prophet ===")


if __name__ == "__main__":
    main()
