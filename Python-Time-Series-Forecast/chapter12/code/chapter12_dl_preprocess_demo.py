"""
《Python 时间序列预测》第 12 章配套：DL 预处理流水线
I-94 风格合成数据 / 探索 / 删列 / sin-cos 周期编码 / 70-20-10 拆分 / MinMaxScaler

运行：
  python Python-Time-Series-Forecast/code/chapter12_dl_preprocess_demo.py

依赖：pip install numpy pandas scikit-learn matplotlib
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

np.random.seed(12)

SECONDS_PER_DAY = 24 * 60 * 60
DROP_COLS = ("rain_1h", "snow_1h")
TARGET_TRAFFIC = "traffic_volume"
TARGET_TEMP = "temp"


def i94_hourly_like(n_hours: int = 17_500, seed: int = 12) -> pd.DataFrame:
    """Synthetic hourly I-94 traffic + weather (>10k rows for DL)."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2016-01-01", periods=n_hours, freq="h")
    hour = idx.hour
    dow = idx.dayofweek

    daily_traffic = 2500 + 1800 * np.sin(2 * np.pi * (hour - 7) / 24)
    weekend = np.where(dow >= 5, -400, 0)
    traffic = daily_traffic + weekend + rng.normal(0, 200, n_hours)
    traffic = np.clip(traffic, 100, None)

    day_of_year = idx.dayofyear
    yearly = 15 + 12 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
    daily_temp = 5 * np.sin(2 * np.pi * (hour - 14) / 24)
    temp = yearly + daily_temp + rng.normal(0, 1.5, n_hours)

    rain = rng.choice([0.0, 0.0, 0.0, 0.2, 0.5], size=n_hours)
    snow = np.zeros(n_hours)

    return pd.DataFrame(
        {
            "date_time": idx.strftime("%Y-%m-%d %H:%M:%S"),
            TARGET_TRAFFIC: traffic,
            TARGET_TEMP: temp,
            "rain_1h": rain,
            "snow_1h": snow,
        }
    )


def cyclic_day_features(dt: pd.Series) -> pd.DataFrame:
    """Map time-of-day to sin/cos on a circle (book: preserve daily seasonality)."""
    ts = pd.to_datetime(dt)
    seconds = (ts - ts.dt.normalize()).dt.total_seconds().to_numpy()
    rad = 2 * np.pi * seconds / SECONDS_PER_DAY
    return pd.DataFrame(
        {"sin_time": np.sin(rad), "cos_time": np.cos(rad)},
        index=dt.index,
    )


def temporal_split(
    df: pd.DataFrame,
    train_ratio: float = 0.7,
    val_ratio: float = 0.2,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    n = len(df)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    train = df.iloc[:n_train]
    val = df.iloc[n_train : n_train + n_val]
    test = df.iloc[n_train + n_val :]
    return train, val, test


def drop_low_value_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if TARGET_TRAFFIC in out.columns:
        desc = out.describe()
        print("=== describe (before drop) ===")
        print(desc.loc[["mean", "max"], [c for c in DROP_COLS if c in out.columns]])
    for c in DROP_COLS:
        if c in out.columns:
            out = out.drop(columns=c)
    return out


def build_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    df = drop_low_value_columns(df)
    cyc = cyclic_day_features(pd.to_datetime(df["date_time"]))
    feat = pd.concat(
        [
            cyc,
            df[[TARGET_TRAFFIC, TARGET_TEMP]].reset_index(drop=True),
        ],
        axis=1,
    )
    return feat


class MinMaxScalerSimple:
    """Book uses sklearn.preprocessing.MinMaxScaler; this mirrors fit/transform."""

    def __init__(self) -> None:
        self.min_: pd.Series | None = None
        self.max_: pd.Series | None = None

    def fit(self, x: pd.DataFrame) -> MinMaxScalerSimple:
        self.min_ = x.min()
        self.max_ = x.max()
        return self

    def transform(self, x: pd.DataFrame) -> np.ndarray:
        assert self.min_ is not None and self.max_ is not None
        denom = (self.max_ - self.min_).replace(0, 1)
        return ((x - self.min_) / denom).to_numpy()


def scale_splits(
    train: pd.DataFrame,
    val: pd.DataFrame,
    test: pd.DataFrame,
    feature_cols: list[str],
):
    try:
        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(train[feature_cols])
        X_val = scaler.transform(val[feature_cols])
        X_test = scaler.transform(test[feature_cols])
        return X_train, X_val, X_test, scaler
    except ImportError:
        scaler = MinMaxScalerSimple().fit(train[feature_cols])
        X_train = scaler.transform(train[feature_cols])
        X_val = scaler.transform(val[feature_cols])
        X_test = scaler.transform(test[feature_cols])
        return X_train, X_val, X_test, scaler


def save_splits(
    path: Path,
    X_train: np.ndarray,
    X_val: np.ndarray,
    X_test: np.ndarray,
    feature_cols: list[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        path,
        X_train=X_train,
        X_val=X_val,
        X_test=X_test,
        feature_cols=np.array(feature_cols),
    )
    print(f"saved: {path}")


def main() -> None:
    raw = i94_hourly_like()
    print("=== 12.1 scale: n =", len(raw), "(book: >17000; DL-friendly) ===")

    print("\n=== 12.3.1 explore first ~400 hours ===")
    head = raw.iloc[:400]
    print(
        "traffic mean by hour (0-23):",
        head.assign(h=pd.to_datetime(head["date_time"]).dt.hour)
        .groupby("h")[TARGET_TRAFFIC]
        .mean()
        .round(0)
        .to_dict(),
    )

    print("\n=== 12.2 model output shapes (concept) ===")
    print("single-step:     y_hat shape (1,)")
    print("multi-step H=24: y_hat shape (24, 1)")
    print("multi-output:    y_hat shape (24, 2)  # traffic + temp")

    print("\n=== 12.3.2 feature engineering ===")
    full = build_feature_matrix(raw)
    feature_cols = list(full.columns)
    train, val, test = temporal_split(full)
    print(f"split sizes train={len(train)}, val={len(val)}, test={len(test)}")

    X_train, X_val, X_test, scaler = scale_splits(train, val, test, feature_cols)
    print("scaled ranges (train):", X_train.min().round(3), "to", X_train.max().round(3))
    print("scaled ranges (val):  ", X_val.min().round(3), "to", X_val.max().round(3), "(may exceed [0,1])")

    out = Path(__file__).resolve().parent / "train_val_test.npz"
    save_splits(out, X_train, X_val, X_test, feature_cols)

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import tempfile

        fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
        t = pd.to_datetime(raw["date_time"].iloc[:400])
        axes[0].plot(t, raw[TARGET_TRAFFIC].iloc[:400])
        axes[0].set_ylabel("traffic")
        axes[1].plot(t, raw[TARGET_TEMP].iloc[:400])
        axes[1].set_ylabel("temp")
        fig.autofmt_xdate()
        p = Path(tempfile.gettempdir()) / "tsf_ch12_i94_2w.png"
        fig.tight_layout()
        fig.savefig(p, dpi=120)
        plt.close(fig)
        print(f"plot saved: {p}")
    except ImportError:
        pass

    print("\n=== 12.4 next: ch.13 baselines + linear + DNN ===")
    print("=== 12.5 exercise: Beijing air dataset — same pipeline, save splits ===")


if __name__ == "__main__":
    main()
