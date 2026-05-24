"""
《Python 时间序列预测》第 14 章配套：线性模型 vs DNN（单步/多步/多输出）

运行：
  python Python-Time-Series-Forecast/code/chapter14_linear_dnn_demo.py

依赖：pip install numpy
推荐：pip install tensorflow  # Python 3.10–3.12；无 TF 时用 sklearn 回退演示
前置：chapter12 npz 或 chapter13/chapter12 数据流水线
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

np.random.seed(14)

_CH13 = Path(__file__).resolve().parent / "chapter13_data_window_baseline_demo.py"
_spec = importlib.util.spec_from_file_location("ch13", _CH13)
ch13 = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(ch13)

DataWindow = ch13.DataWindow
TRAFFIC_IDX = ch13.TRAFFIC_IDX
TARGET_IDXS = ch13.TARGET_IDXS
load_scaled_splits = ch13.load_scaled_splits
eval_baseline = ch13.eval_baseline
baseline_single_step = ch13.baseline_single_step
baseline_multi_repeat_sequence = ch13.baseline_multi_repeat_sequence
baseline_multi_output = ch13.baseline_multi_output

MAX_EPOCHS = 40
PATIENCE = 3
BATCH = 32


def try_import_tf():
    try:
        import tensorflow as tf

        tf.random.set_seed(14)
        return tf
    except ImportError:
        return None


def compile_and_fit(model, train_ds, val_ds, tf, max_epochs: int = MAX_EPOCHS):
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    callback = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=PATIENCE,
        restore_best_weights=True,
    )
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=max_epochs,
        callbacks=[callback],
        verbose=0,
    )
    return history


def val_mae(model, val_ds) -> float:
    _, mae = model.evaluate(val_ds, verbose=0)
    return float(mae)


def build_linear_single(tf, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(1, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(1),
        ],
        name="linear_single",
    )


def build_linear_multi(tf, input_width: int, n_features: int, label_width: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            tf.keras.layers.TimeDistributed(
                tf.keras.layers.Dense(
                    1,
                    kernel_initializer=tf.keras.initializers.Zeros(),
                )
            ),
            tf.keras.layers.Reshape((label_width,)),
        ],
        name="linear_multi",
    )


def build_linear_multi_output(tf, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(1, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(2),
        ],
        name="linear_multi_output",
    )


def build_dnn_single(tf, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(1, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(1),
        ],
        name="dnn_single",
    )


def build_dnn_multi(tf, input_width: int, n_features: int, label_width: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(label_width),
        ],
        name="dnn_multi",
    )


def build_dnn_multi_output(tf, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(1, n_features)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(2),
        ],
        name="dnn_multi_output",
    )


def run_scenario(
    name: str,
    window: DataWindow,
    tf,
    build_linear,
    build_dnn,
    baseline_fn,
    n_features: int,
) -> None:
    train_ds = window.make_tf_dataset(window.train_data, shuffle=True)
    val_ds = window.make_tf_dataset(window.val_data, shuffle=False)

    _, mae_base = eval_baseline(window, window.val_data, baseline_fn)
    print(f"\n=== {name} ===")
    print(f"baseline MAE: {mae_base:.4f}")

    lin = build_linear()
    compile_and_fit(lin, train_ds, val_ds, tf)
    mae_lin = val_mae(lin, val_ds)
    print(f"linear   MAE: {mae_lin:.4f}")

    dnn = build_dnn()
    compile_and_fit(dnn, train_ds, val_ds, tf)
    mae_dnn = val_mae(dnn, val_ds)
    print(f"DNN      MAE: {mae_dnn:.4f}  (book: DNN best)")
    print(f"DNN beats linear: {mae_dnn < mae_lin}")


def stack_windows(window: DataWindow, data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    xs, ys = [], []
    for x, y in window.iter_numpy(data, shuffle=False):
        xs.append(x.reshape(-1))
        ys.append(y.reshape(-1))
    return np.stack(xs), np.stack(ys)


def run_sklearn_scenario(
    name: str,
    window: DataWindow,
    baseline_fn,
) -> None:
    from sklearn.linear_model import LinearRegression
    from sklearn.neural_network import MLPRegressor

    X_tr, y_tr = stack_windows(window, window.train_data)
    X_va, y_va = stack_windows(window, window.val_data)

    _, mae_base = eval_baseline(window, window.val_data, baseline_fn)
    print(f"\n=== {name} [sklearn fallback] ===")
    print(f"baseline MAE: {mae_base:.4f}")

    lin = LinearRegression()
    lin.fit(X_tr, np.asarray(y_tr).ravel() if y_tr.ndim > 1 and y_tr.shape[1] == 1 else y_tr)
    mae_lin = float(np.mean(np.abs(y_va - lin.predict(X_va))))
    print(f"linear   MAE: {mae_lin:.4f}")

    dnn = MLPRegressor(
        hidden_layer_sizes=(64, 64),
        activation="relu",
        max_iter=250,
        learning_rate_init=1e-3,
        random_state=14,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=8,
    )
    dnn.fit(X_tr, np.asarray(y_tr).ravel() if y_tr.ndim > 1 and y_tr.shape[1] == 1 else y_tr)
    mae_dnn = float(np.mean(np.abs(y_va - dnn.predict(X_va))))
    print(f"DNN(MLP) MAE: {mae_dnn:.4f}  (book: DNN best)")
    print(f"DNN beats linear: {mae_dnn < mae_lin}")


def main() -> None:
    X_train, X_val, cols = load_scaled_splits()
    n_features = X_train.shape[1]
    print("=== 14.x features:", list(cols), "===")

    tf = try_import_tf()
    if tf is None:
        print(
            "TensorFlow not available (use Python 3.10–3.12 + pip install tensorflow "
            "for Keras EarlyStopping demo). Using sklearn LinearRegression / MLPRegressor.\n"
        )
        w1 = DataWindow(1, 1, 1, X_train, X_val, label_indices=(TRAFFIC_IDX,), batch_size=BATCH)
        run_sklearn_scenario(
            "14.1.1 / 14.2.1 single-step",
            w1,
            baseline_single_step,
        )
        w24 = DataWindow(24, 24, 24, X_train, X_val, label_indices=(TRAFFIC_IDX,), batch_size=BATCH)
        run_sklearn_scenario(
            "14.1.2 / 14.2.2 multi-step 24h",
            w24,
            baseline_multi_repeat_sequence,
        )
        w_mo = DataWindow(1, 1, 1, X_train, X_val, label_indices=TARGET_IDXS, batch_size=BATCH)
        run_sklearn_scenario(
            "14.1.3 / 14.2.3 multi-output",
            w_mo,
            baseline_multi_output,
        )
        print("\n=== 14.3 next: ch.15 LSTM ===")
        return

    w1 = DataWindow(1, 1, 1, X_train, X_val, label_indices=(TRAFFIC_IDX,), batch_size=BATCH)
    run_scenario(
        "14.1.1 / 14.2.1 single-step (book linear MAE < baseline; DNN best)",
        w1,
        tf,
        lambda: build_linear_single(tf, n_features),
        lambda: build_dnn_single(tf, n_features),
        baseline_single_step,
        n_features,
    )

    w24 = DataWindow(24, 24, 24, X_train, X_val, label_indices=(TRAFFIC_IDX,), batch_size=BATCH)
    run_scenario(
        "14.1.2 / 14.2.2 multi-step 24h",
        w24,
        tf,
        lambda: build_linear_multi(tf, 24, n_features, 24),
        lambda: build_dnn_multi(tf, 24, n_features, 24),
        baseline_multi_repeat_sequence,
        n_features,
    )

    w_mo = DataWindow(1, 1, 1, X_train, X_val, label_indices=TARGET_IDXS, batch_size=BATCH)
    run_scenario(
        "14.1.3 / 14.2.3 multi-output (traffic + temp)",
        w_mo,
        tf,
        lambda: build_linear_multi_output(tf, n_features),
        lambda: build_dnn_multi_output(tf, n_features),
        baseline_multi_output,
        n_features,
    )

    print("\n=== 14.3 next: ch.15 LSTM for sequence memory ===")


if __name__ == "__main__":
    main()
