"""
《Python 时间序列预测》第 15 章配套：LSTM 单步 / 多步 / 多输出

运行：
  python Python-Time-Series-Forecast/code/chapter15_lstm_demo.py

依赖：pip install numpy
推荐：pip install tensorflow  (Python 3.10–3.12)
前置：chapter12–14 数据与 DataWindow
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

np.random.seed(15)

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

INPUT_LSTM = 24
LSTM_UNITS = 32
MAX_EPOCHS = 50
PATIENCE = 3
BATCH = 32

# book reference MAE on scaled traffic (ch.15)
BOOK_MAE = {
    "multi_step": {"lstm": 0.058, "dnn": 0.064, "linear": 0.076},
    "multi_output": {"lstm": 0.017, "dnn": 0.020},
}


def try_import_tf():
    try:
        import tensorflow as tf

        tf.random.set_seed(15)
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
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=max_epochs,
        callbacks=[callback],
        verbose=0,
    )


def val_mae(model, val_ds) -> float:
    _, mae = model.evaluate(val_ds, verbose=0)
    return float(mae)


def build_lstm_single(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            tf.keras.layers.LSTM(LSTM_UNITS, return_sequences=True),
            tf.keras.layers.Lambda(lambda x: x[:, -1, :]),
            tf.keras.layers.Dense(1),
        ],
        name="lstm_single",
    )


def build_lstm_multi(tf, input_width: int, label_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            tf.keras.layers.LSTM(LSTM_UNITS, return_sequences=True),
            tf.keras.layers.Dense(1),
            tf.keras.layers.Reshape((label_width,)),
        ],
        name="lstm_multi",
    )


def build_lstm_multi_output(tf, input_width: int, n_features: int):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_width, n_features)),
            tf.keras.layers.LSTM(LSTM_UNITS, return_sequences=True),
            tf.keras.layers.Lambda(lambda x: x[:, -1, :]),
            tf.keras.layers.Dense(2),
        ],
        name="lstm_multi_output",
    )


def run_lstm_scenario(
    title: str,
    window: DataWindow,
    tf,
    builder,
    baseline_fn,
    book_note: str = "",
) -> float:
    train_ds = window.make_tf_dataset(window.train_data, shuffle=True)
    val_ds = window.make_tf_dataset(window.val_data, shuffle=False)
    _, mae_base = eval_baseline(window, window.val_data, baseline_fn)
    model = builder()
    compile_and_fit(model, train_ds, val_ds, tf)
    mae_lstm = val_mae(model, val_ds)
    print(f"\n=== {title} ===")
    print(f"baseline MAE: {mae_base:.4f}")
    print(f"LSTM     MAE: {mae_lstm:.4f}")
    if book_note:
        print(f"book ref:   {book_note}")
    return mae_lstm


def main_no_tf(X_train, X_val, n_features: int) -> None:
    print("TensorFlow not available — printing baseline MAE + book LSTM targets.\n")
    w24_1 = DataWindow(INPUT_LSTM, 1, INPUT_LSTM, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    _, b1 = eval_baseline(w24_1, X_val, baseline_single_step)
    print(f"15.3.1 single-step baseline MAE: {b1:.4f}")

    w24 = DataWindow(24, 24, 24, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    _, b2 = eval_baseline(w24, X_val, baseline_multi_repeat_sequence)
    ref = BOOK_MAE["multi_step"]
    print(f"15.3.2 multi-step  baseline MAE: {b2:.4f}")
    print(f"  book LSTM {ref['lstm']} | DNN {ref['dnn']} | linear {ref['linear']}")

    w_mo = DataWindow(INPUT_LSTM, 1, INPUT_LSTM, X_train, X_val, TARGET_IDXS, BATCH)
    _, b3 = eval_baseline(w_mo, X_val, baseline_multi_output)
    ref2 = BOOK_MAE["multi_output"]
    print(f"15.3.3 multi-output baseline MAE: {b3:.4f}")
    print(f"  book LSTM {ref2['lstm']} | DNN {ref2['dnn']}")
    print("\nInstall tensorflow on Python 3.10–3.12 to train LSTM locally.")


def main() -> None:
    X_train, X_val, cols = load_scaled_splits()
    n_features = X_train.shape[1]
    print("=== 15.3 LSTM on features:", list(cols), "===")

    tf = try_import_tf()
    if tf is None:
        main_no_tf(X_train, X_val, n_features)
        print("\n=== 15.4 next: ch.16 CNN (faster training) ===")
        return

    run_lstm_scenario(
        "15.3.1 single-step (input 24h -> next traffic)",
        DataWindow(INPUT_LSTM, 1, INPUT_LSTM, X_train, X_val, (TRAFFIC_IDX,), BATCH),
        tf,
        lambda: build_lstm_single(tf, INPUT_LSTM, n_features),
        baseline_single_step,
        "book: LSTM beats baseline, linear, DNN",
    )

    run_lstm_scenario(
        "15.3.2 multi-step 24h",
        DataWindow(24, 24, 24, X_train, X_val, (TRAFFIC_IDX,), BATCH),
        tf,
        lambda: build_lstm_multi(tf, 24, 24, n_features),
        baseline_multi_repeat_sequence,
        f"LSTM ~{BOOK_MAE['multi_step']['lstm']} vs DNN {BOOK_MAE['multi_step']['dnn']}",
    )

    run_lstm_scenario(
        "15.3.3 multi-output (24h -> next traffic+temp)",
        DataWindow(INPUT_LSTM, 1, INPUT_LSTM, X_train, X_val, TARGET_IDXS, BATCH),
        tf,
        lambda: build_lstm_multi_output(tf, INPUT_LSTM, n_features),
        baseline_multi_output,
        f"LSTM ~{BOOK_MAE['multi_output']['lstm']} vs DNN {BOOK_MAE['multi_output']['dnn']}",
    )

    print("\n=== 15.4 next: ch.16 CNN ===")


if __name__ == "__main__":
    main()
