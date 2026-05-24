"""
《Python 时间序列预测》第 17 章配套：自回归 LSTM (ARLSTM) — LSTMCell + 反馈循环

运行：
  python Python-Time-Series-Forecast/code/chapter17_arlstm_demo.py

依赖：pip install numpy
推荐：pip install tensorflow  (Python 3.10–3.12)
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

np.random.seed(17)

_CH13 = Path(__file__).resolve().parent / "chapter13_data_window_baseline_demo.py"
_spec = importlib.util.spec_from_file_location("ch13", _CH13)
ch13 = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(ch13)

DataWindow = ch13.DataWindow
TRAFFIC_IDX = ch13.TRAFFIC_IDX
load_scaled_splits = ch13.load_scaled_splits
eval_baseline = ch13.eval_baseline

OUT_STEPS = 24
INPUT_WIDTH = 24
UNITS = 32
MAX_EPOCHS = 50
PATIENCE = 3
BATCH = 32

BOOK_MAE_MULTI = {
    "arlstm": 0.049,
    "cnn_lstm": 0.055,
    "lstm": 0.058,
    "cnn": 0.063,
}


def try_import_tf():
    try:
        import tensorflow as tf

        tf.random.set_seed(17)
        return tf
    except ImportError:
        return None


def build_autoregressive_model(tf, units: int, out_steps: int):
    """Book-style AutoRegressive model using LSTMCell feedback."""

    class AutoRegressive(tf.keras.Model):
        def __init__(self, units: int, out_steps: int, **kwargs):
            super().__init__(**kwargs)
            self.out_steps = out_steps
            self.lstm_cell = tf.keras.layers.LSTMCell(units, name="ar_cell")
            self.lstm_rnn = tf.keras.layers.RNN(
                self.lstm_cell,
                return_state=True,
                name="ar_warmup_rnn",
            )
            self.dense = tf.keras.layers.Dense(1, name="ar_dense")

        def warmup(self, inputs):
            """Run over history; return first prediction and RNN state."""
            x, state = self.lstm_rnn(inputs)
            prediction = self.dense(x)
            prediction = tf.squeeze(prediction, axis=-1)
            return prediction, state

        def call(self, inputs, training=None):
            predictions = []
            prediction, state = self.warmup(inputs)
            predictions.append(prediction)
            for _ in range(self.out_steps - 1):
                x = tf.expand_dims(prediction, axis=1)
                x, state = self.lstm_cell(x, states=state, training=training)
                prediction = self.dense(x)
                prediction = tf.squeeze(prediction, axis=1)
                predictions.append(prediction)
            return tf.stack(predictions, axis=1)

    return AutoRegressive(units=units, out_steps=out_steps)


def baseline_multi_last_segment(inputs: np.ndarray, label_width: int = OUT_STEPS) -> np.ndarray:
    x = ch13._as_batch(inputs)
    seq = x[:, :, TRAFFIC_IDX]
    return seq[:, -label_width:]


def numpy_autoregressive_roll(
    window: DataWindow,
    data: np.ndarray,
    steps: int,
) -> tuple[float, float]:
    """Naive AR: repeat last traffic, feed prediction forward (illustrates error accumulation)."""
    se, ae, n = 0.0, 0.0, 0
    for inputs, labels in window.iter_numpy(data, shuffle=False):
        last = float(inputs[-1, TRAFFIC_IDX])
        preds = []
        x = last
        for _ in range(steps):
            preds.append(x)
            x = x  # identity feedback on scaled traffic (demo only)
        pred = np.array(preds)
        se += np.sum((labels - pred) ** 2)
        ae += np.sum(np.abs(labels - pred))
        n += labels.size
    return se / n, ae / n


def main() -> None:
    X_train, X_val, cols = load_scaled_splits()
    print("=== 17.2 ARLSTM multi-step | features:", list(cols), "===")

    window = DataWindow(INPUT_WIDTH, OUT_STEPS, INPUT_WIDTH, X_train, X_val, (TRAFFIC_IDX,), BATCH)
    _, mae_base = eval_baseline(
        window, X_val, lambda inp: baseline_multi_last_segment(inp, OUT_STEPS)
    )
    print(f"baseline (last-24 repeat) MAE: {mae_base:.4f}")

    tf = try_import_tf()
    if tf is None:
        mse_na, mae_na = numpy_autoregressive_roll(window, X_val, OUT_STEPS)
        print(f"numpy identity-feedback AR MAE: {mae_na:.4f} (demo only; not trained)")
        print("\nBook test MAE (ch.17):")
        for k, v in BOOK_MAE_MULTI.items():
            print(f"  {k:10s}: {v:.3f}")
        print("ARLSTM wins on traffic multi-step in the book.")
        print("\nInstall tensorflow on Python 3.10–3.12 to train custom AutoRegressive model.")
        print("=== 17.3 next: Prophet & capstone projects ===")
        return

    model = build_autoregressive_model(tf, UNITS, OUT_STEPS)
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    train_ds = window.make_tf_dataset(X_train, shuffle=True)
    val_ds = window.make_tf_dataset(X_val, shuffle=False)

    cb = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=PATIENCE, restore_best_weights=True
    )
    model.fit(train_ds, validation_data=val_ds, epochs=MAX_EPOCHS, callbacks=[cb], verbose=0)

    _, mae_ar = model.evaluate(val_ds, verbose=0)
    print(f"ARLSTM val MAE: {float(mae_ar):.4f}  (book test ~{BOOK_MAE_MULTI['arlstm']})")
    print("Book comparison (test MAE):")
    for k, v in BOOK_MAE_MULTI.items():
        print(f"  {k:10s}: {v:.3f}")

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import tempfile

        for inputs, labels in window.iter_numpy(X_val[:2000]):
            inp = tf.convert_to_tensor(inputs[None, ...], dtype=tf.float32)
            pred = model(inp, training=False).numpy()[0]
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.plot(labels, label="actual", lw=2)
            ax.plot(pred, "--", label="ARLSTM")
            ax.legend()
            fig.tight_layout()
            p = Path(tempfile.gettempdir()) / "tsf_ch17_arlstm_sample.png"
            fig.savefig(p, dpi=120)
            plt.close(fig)
            print(f"sample plot: {p}")
            break
    except ImportError:
        pass

    print("\n=== 17.3 ARLSTM is a tool, not always best; next: Prophet / steak capstone ===")


if __name__ == "__main__":
    main()
