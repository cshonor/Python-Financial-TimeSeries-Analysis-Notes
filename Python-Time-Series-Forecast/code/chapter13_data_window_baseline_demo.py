"""
《Python 时间序列预测》第 13 章配套：DataWindow + 单步/多步/多输出基线 (MSE/MAE)

运行：
  python Python-Time-Series-Forecast/code/chapter13_data_window_baseline_demo.py

依赖：pip install numpy pandas
可选：pip install tensorflow  # 使用 tf.data 窗口；未安装则用 NumPy
先运行 chapter12 生成 dataset/chapter12/train_val_test.npz（或本脚本自动重建）
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

np.random.seed(13)

# feature order from chapter 12: sin_time, cos_time, traffic_volume, temp
TRAFFIC_IDX = 2
TEMP_IDX = 3
TARGET_IDXS = (TRAFFIC_IDX, TEMP_IDX)


class DataWindow:
    """Sliding windows: inputs [:input_width], labels [shift:shift+label_width]."""

    def __init__(
        self,
        input_width: int,
        label_width: int,
        shift: int,
        train_data: np.ndarray,
        val_data: np.ndarray,
        label_indices: tuple[int, ...] = (TRAFFIC_IDX,),
        batch_size: int = 32,
        shuffle_train: bool = True,
    ) -> None:
        self.input_width = input_width
        self.label_width = label_width
        self.shift = shift
        self.label_indices = label_indices
        self.batch_size = batch_size
        self.total_size = shift + label_width
        if shift < input_width:
            raise ValueError("shift should be >= input_width for causal forecasting")
        self.train_data = train_data
        self.val_data = val_data
        self._shuffle_train = shuffle_train

    def _split_window(self, window: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        inputs = window[: self.input_width, :]
        labels = window[self.shift : self.shift + self.label_width, self.label_indices]
        if len(self.label_indices) == 1:
            labels = labels.squeeze(-1)
        return inputs, labels

    def iter_numpy(self, data: np.ndarray, shuffle: bool = False):
        n = len(data)
        starts = list(range(n - self.total_size + 1))
        if shuffle:
            rng = np.random.default_rng(13)
            rng.shuffle(starts)
        for i in starts:
            w = data[i : i + self.total_size]
            yield self._split_window(w)

    def batches(self, data: np.ndarray, shuffle: bool = False):
        batch_in, batch_lb = [], []
        for inputs, labels in self.iter_numpy(data, shuffle=shuffle):
            batch_in.append(inputs)
            batch_lb.append(labels)
            if len(batch_in) >= self.batch_size:
                yield np.stack(batch_in), np.stack(batch_lb)
                batch_in, batch_lb = [], []
        if batch_in:
            yield np.stack(batch_in), np.stack(batch_lb)

    def make_tf_dataset(self, data: np.ndarray, shuffle: bool = False):
        import tensorflow as tf

        ds = tf.keras.preprocessing.timeseries_dataset_from_array(
            data,
            targets=None,
            sequence_length=self.total_size,
            sequence_stride=1,
            batch_size=self.batch_size,
            shuffle=shuffle,
        )
        idx = list(self.label_indices)

        def _map_fn(win):
            inputs = win[:, : self.input_width, :]
            labels = win[:, self.shift : self.shift + self.label_width, idx]
            if len(idx) == 1:
                labels = labels[:, :, 0]
            elif self.label_width == 1:
                labels = labels[:, 0, :]
            return inputs, labels

        return ds.map(_map_fn)

    def plot(self, data: np.ndarray, n_show: int = 1, save_path: Path | None = None) -> None:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(n_show, 1, figsize=(10, 3 * n_show), squeeze=False)
        for ax_i, (inputs, labels) in zip(range(n_show), self.iter_numpy(data)):
            ax = axes[ax_i, 0]
            t_in = np.arange(inputs.shape[0])
            t_lb = np.arange(inputs.shape[0], inputs.shape[0] + labels.shape[0])
            ax.plot(t_in, inputs[:, TRAFFIC_IDX], label="input traffic")
            ax.plot(t_lb, labels[:, 0] if labels.ndim == 2 else labels, "o-", label="label")
            ax.legend()
            ax.set_title(f"window @ start (traffic only view)")
        fig.tight_layout()
        if save_path:
            fig.savefig(save_path, dpi=120)
        plt.close(fig)


def mse(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean((actual - pred) ** 2))


def mae(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs(actual - pred)))


def align_pred_labels(pred: np.ndarray, labels: np.ndarray) -> np.ndarray:
    if pred.shape == labels.shape:
        return pred
    if pred.ndim == 2 and pred.shape[0] == 1:
        pred = pred.squeeze(0)
    if labels.ndim == 2 and pred.ndim == 1:
        return pred[:, None]
    if labels.ndim == 2 and pred.ndim == 2 and labels.shape[1] == pred.shape[1]:
        return pred
    if labels.ndim == 3 and pred.ndim == 2:
        return pred[:, None, :]
    return np.broadcast_to(pred, labels.shape)


def eval_baseline(
    window: DataWindow,
    data: np.ndarray,
    predict_fn,
) -> tuple[float, float]:
    """Average MSE / MAE over all windows in data."""
    se, ae, n = 0.0, 0.0, 0
    for inputs, labels in window.iter_numpy(data, shuffle=False):
        pred = align_pred_labels(predict_fn(inputs), labels)
        se += np.sum((labels - pred) ** 2)
        ae += np.sum(np.abs(labels - pred))
        n += labels.size
    return se / n, ae / n


def load_scaled_splits() -> tuple[np.ndarray, np.ndarray, list[str]]:
    npz_path = Path(__file__).resolve().parents[1] / "dataset" / "chapter12" / "train_val_test.npz"
    if npz_path.is_file():
        z = np.load(npz_path, allow_pickle=True)
        return z["X_train"], z["X_val"], list(z["feature_cols"])
    # rebuild via chapter 12 helpers
    ch12 = Path(__file__).resolve().parent / "chapter12_dl_preprocess_demo.py"
    sys.path.insert(0, str(ch12.parent))
    import importlib.util

    spec = importlib.util.spec_from_file_location("ch12", ch12)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    raw = mod.i94_hourly_like()
    full = mod.build_feature_matrix(raw)
    train, val, _test = mod.temporal_split(full)
    cols = list(full.columns)
    X_train, X_val, _X_test, _sc = mod.scale_splits(train, val, _test, cols)
    return X_train, X_val, cols


def _as_batch(inputs: np.ndarray) -> np.ndarray:
    return inputs[None, ...] if inputs.ndim == 2 else inputs


def baseline_single_step(inputs: np.ndarray) -> np.ndarray:
    x = _as_batch(inputs)
    return x[:, -1, TRAFFIC_IDX]


def baseline_multi_repeat_last(inputs: np.ndarray, label_width: int) -> np.ndarray:
    x = _as_batch(inputs)
    last = x[:, -1, TRAFFIC_IDX]
    return np.tile(last[:, None], (1, label_width))


def baseline_multi_repeat_sequence(inputs: np.ndarray) -> np.ndarray:
    x = _as_batch(inputs)
    return x[:, :, TRAFFIC_IDX]


def baseline_multi_output(inputs: np.ndarray) -> np.ndarray:
    x = _as_batch(inputs)
    return x[:, -1, list(TARGET_IDXS)]


def main() -> None:
    X_train, X_val, cols = load_scaled_splits()
    print("=== 13.1 DataWindow (features:", cols, ") ===")
    print(f"train {X_train.shape}, val {X_val.shape}")

    try:
        import tensorflow as tf  # noqa: F401

        print("TensorFlow available: can use make_tf_dataset(shuffle=True) on train")
    except ImportError:
        print("TensorFlow not installed: using NumPy window iterator (book-equivalent logic)")

    # 13.2.1 single-step
    w1 = DataWindow(1, 1, 1, X_train, X_val, label_indices=(TRAFFIC_IDX,))
    try:
        import tempfile

        p = Path(tempfile.gettempdir()) / "tsf_ch13_window_single.png"
        w1.plot(X_val[:500], save_path=p)
        print(f"window plot: {p}")
    except ImportError:
        pass

    mse1, mae1 = eval_baseline(w1, X_val, baseline_single_step)
    print(f"\n=== 13.2.1 single-step baseline (book MAE ~0.081) ===")
    print(f"MSE={mse1:.4f}, MAE={mae1:.4f}")

    # 13.2.2 multi-step
    w24 = DataWindow(24, 24, 24, X_train, X_val, label_indices=(TRAFFIC_IDX,))

    mse_last, mae_last = eval_baseline(
        w24,
        X_val,
        lambda inp: baseline_multi_repeat_last(inp, 24),
    )
    mse_seq, mae_seq = eval_baseline(w24, X_val, baseline_multi_repeat_sequence)
    print("\n=== 13.2.2 multi-step 24h (book: last ~0.347, sequence ~0.341) ===")
    print(f"repeat last value:  MSE={mse_last:.4f}, MAE={mae_last:.4f}")
    print(f"repeat input seq:   MSE={mse_seq:.4f}, MAE={mae_seq:.4f}")
    print("sequence baseline better:", mae_seq < mae_last)

    # 13.2.3 multi-output
    w_mo = DataWindow(1, 1, 1, X_train, X_val, label_indices=TARGET_IDXS)
    mse_mo, mae_mo = eval_baseline(w_mo, X_val, baseline_multi_output)
    print(f"\n=== 13.2.3 multi-output (traffic+temp, book MAE ~0.047) ===")
    print(f"MSE={mse_mo:.4f}, MAE={mae_mo:.4f}")

    n_batches = sum(1 for _ in w1.batches(X_train, shuffle=True))
    print(f"\n=== 13.1.1 train batches (size={w1.batch_size}): {n_batches} ===")
    print("\n=== 13.3 next: ch.14 linear + DNN must beat these MAE values ===")


if __name__ == "__main__":
    main()
