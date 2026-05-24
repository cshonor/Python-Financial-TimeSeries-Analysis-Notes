"""
《Python 时间序列预测》第 16 章配套：Conv1D / CNN+LSTM 单步·多步·多输出

运行：
  python Python-Time-Series-Forecast/code/chapter16_cnn_demo.py

依赖：pip install numpy
推荐：pip install tensorflow  (Python 3.10–3.12)
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

np.random.seed(16)

KERNEL_WIDTH = 3

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


def baseline_multi_last_segment(inputs: np.ndarray, label_width: int = 24) -> np.ndarray:
    """Repeat last `label_width` steps of input traffic as forecast (for input>label windows)."""
    x = ch13._as_batch(inputs)
    seq = x[:, :, TRAFFIC_IDX]
    return seq[:, -label_width:]
baseline_multi_output = ch13.baseline_multi_output

MAX_EPOCHS = 50
PATIENCE = 3
BATCH = 32


def input_len(label_width: int, kernel: int = KERNEL_WIDTH) -> int:
    """book: input = label + kernel - 1"""
    return label_width + kernel - 1


def try_import_tf():
    try:
        import tensorflow as tf

        tf.random.set_seed(16)
        return tf
    except ImportError:
        return None


def compile_and_fit(model, train_ds, val_ds, tf):
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    cb = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=PATIENCE, restore_best_weights=True
    )
    model.fit(train_ds, validation_data=val_ds, epochs=MAX_EPOCHS, callbacks=[cb], verbose=0)


def val_mae(model, val_ds) -> float:
    _, mae = model.evaluate(val_ds, verbose=0)
    return float(mae)


def _conv_block(tf, n_features: int):
    return [
        tf.keras.layers.Conv1D(
            32,
            KERNEL_WIDTH,
            padding="same",
            activation="relu",
        ),
    ]


def build_cnn_single(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1),
        ],
        name="cnn_single",
    )


def build_cnn_lstm_single(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.LSTM(32, return_sequences=True),
            tf.keras.layers.Lambda(lambda x: x[:, -1, :]),
            tf.keras.layers.Dense(1),
        ],
        name="cnn_lstm_single",
    )


def build_cnn_multi(tf, input_width: int, label_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(label_width),
        ],
        name="cnn_multi",
    )


def build_cnn_lstm_multi(tf, input_width: int, label_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.LSTM(32, return_sequences=True),
            tf.keras.layers.Dense(1),
            tf.keras.layers.Reshape((label_width,)),
        ],
        name="cnn_lstm_multi",
    )


def build_cnn_multi_output(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(2),
        ],
        name="cnn_multi_output",
    )


def build_cnn_lstm_multi_output(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            *_conv_block(tf, n_features),
            tf.keras.layers.LSTM(32, return_sequences=True),
            tf.keras.layers.Lambda(lambda x: x[:, -1, :]),
            tf.keras.layers.Dense(2),
        ],
        name="cnn_lstm_mo",
    )


def eval_models(
    title: str,
    window: DataWindow,
    tf,
    builders: dict[str, callable],
    baseline_fn,
) -> None:
    train_ds = window.make_tf_dataset(window.train_data, shuffle=True)
    val_ds = window.make_tf_dataset(window.val_data, shuffle=False)
    _, mae_b = eval_baseline(window, window.val_data, baseline_fn)
    print(f"\n=== {title} (input={window.input_width}, label={window.label_width}) ===")
    print(f"baseline MAE: {mae_b:.4f}")
    results: dict[str, float] = {}
    for name, build in builders.items():
        m = build()
        compile_and_fit(m, train_ds, val_ds, tf)
        results[name] = val_mae(m, val_ds)
        print(f"{name:12s} MAE: {results[name]:.4f}")
    best = min(results, key=results.get)
    print(f"best in demo: {best}")


def main_no_tf() -> None:
    X_train, X_val, cols = load_scaled_splits()
    print("=== 16.x features:", list(cols), "===\n")
    print("TensorFlow not available. Book conclusions (ch.16):")
    print("  16.2.1 single-step: CNN input=3 — often NOT better than LSTM (too short).")
    print("  16.2.2 multi-step:  input=26, label=24 — CNN+LSTM best MAE vs CNN or LSTM alone.")
    print("  16.2.3 multi-out:   input=24 — CNN / CNN+LSTM / LSTM may tie on MAE.")
    iw = input_len(1)
    w1 = DataWindow(iw, 1, iw, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    _, b1 = eval_baseline(w1, X_val, baseline_single_step)
    iw24 = input_len(24)
    w24 = DataWindow(iw24, 24, iw24, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    _, b24 = eval_baseline(
        w24, X_val, lambda inp: baseline_multi_last_segment(inp, label_width=24)
    )
    wmo = DataWindow(24, 1, 24, X_train, X_val, TARGET_IDXS, BATCH)
    _, bmo = eval_baseline(wmo, X_val, baseline_multi_output)
    print(f"\nbaselines: single={b1:.4f} multi={b24:.4f} multi-out={bmo:.4f}")
    print("\nInstall tensorflow (Python 3.10–3.12) to train Conv1D models.")


def main() -> None:
    X_train, X_val, cols = load_scaled_splits()
    n_features = X_train.shape[1]
    print("=== 16.2 CNN KERNEL_WIDTH =", KERNEL_WIDTH, "| features:", list(cols), "===")

    tf = try_import_tf()
    if tf is None:
        main_no_tf()
        print("\n=== 16.3 next: ch.17 ARLSTM step-by-step ===")
        return

    # 16.2.1 single-step: input 3
    iw1 = input_len(1)
    w1 = DataWindow(iw1, 1, iw1, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    eval_models(
        "16.2.1 single-step",
        w1,
        tf,
        {
            "CNN": lambda: build_cnn_single(tf, iw1, n_features),
            "CNN+LSTM": lambda: build_cnn_lstm_single(tf, iw1, n_features),
        },
        baseline_single_step,
    )

    # 16.2.2 multi-step: input 26, label 24
    lw = 24
    iw = input_len(lw)
    w24 = DataWindow(iw, lw, iw, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    eval_models(
        "16.2.2 multi-step (book: CNN+LSTM champion)",
        w24,
        tf,
        {
            "CNN": lambda: build_cnn_multi(tf, iw, lw, n_features),
            "CNN+LSTM": lambda: build_cnn_lstm_multi(tf, iw, lw, n_features),
        },
        lambda inp: baseline_multi_last_segment(inp, label_width=lw),
    )

    # 16.2.3 multi-output: input 24
    wmo = DataWindow(24, 1, 24, X_train, X_val, TARGET_IDXS, BATCH)
    eval_models(
        "16.2.3 multi-output (book: models may tie)",
        wmo,
        tf,
        {
            "CNN": lambda: build_cnn_multi_output(tf, 24, n_features),
            "CNN+LSTM": lambda: build_cnn_lstm_multi_output(tf, 24, n_features),
        },
        baseline_multi_output,
    )

    print("\n=== 16.3 next: ch.17 ARLSTM ===")


if __name__ == "__main__":
    main()
