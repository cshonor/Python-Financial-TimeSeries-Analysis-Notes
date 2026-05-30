"""
《Python 时间序列预测》第 1 章配套：分解示意 + 时间顺序 train/test

运行：
  python Python-Time-Series-Forecast/code/chapter01_forecast_workflow_demo.py

可选：pip install statsmodels matplotlib
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def make_series(n: int = 120) -> pd.Series:
    rng = np.random.default_rng(0)
    t = np.arange(n)
    trend = 0.02 * t
    seasonal = 2 * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(0, 0.3, n)
    idx = pd.date_range("2020-01-01", periods=n, freq="MS")
    return pd.Series(trend + seasonal + noise, index=idx, name="y")


def time_split(y: pd.Series, test_ratio: float = 0.2) -> tuple[pd.Series, pd.Series]:
    """Never shuffle — hold out the last contiguous block."""
    n_test = max(1, int(len(y) * test_ratio))
    return y.iloc[:-n_test], y.iloc[-n_test:]


def naive_forecast(train: pd.Series, horizon: int) -> pd.Series:
    """Baseline: repeat last observed value."""
    last = train.iloc[-1]
    idx = pd.date_range(train.index[-1], periods=horizon + 1, freq=train.index.freq)[1:]
    return pd.Series(last, index=idx, name="forecast")


def mse(actual: pd.Series, pred: pd.Series) -> float:
    aligned = actual.align(pred, join="inner")
    diff = aligned[0] - aligned[1]
    return float((diff**2).mean())


def try_decompose(y: pd.Series, out_dir: Path) -> None:
    try:
        from statsmodels.tsa.seasonal import seasonal_decompose
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nseasonal_decompose: skipped (pip install statsmodels matplotlib)")
        return

    result = seasonal_decompose(y, model="additive", period=12)
    fig = result.plot()
    path = out_dir / "ch01_decompose.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print("\nSaved decomposition plot:", path)


def main() -> None:
    print("=== 1.1 synthetic series (trend + season + noise) ===")
    y = make_series()
    print(y.head(3), "\n...", y.tail(2))

    train, test = time_split(y, test_ratio=0.2)
    print(f"\n=== 1.2.5 time-ordered split (no shuffle): train={len(train)} test={len(test)} ===")
    fc = naive_forecast(train, horizon=len(test))
    print("naive MSE on test:", round(mse(test, fc), 4))

    print("\n=== 1.3.1 look-ahead warning ===")
    print("WRONG: shuffle rows before fit. RIGHT: use only train.index < test.index.min()")

    out_dir = Path(tempfile.gettempdir()) / "tsf_ch01"
    out_dir.mkdir(parents=True, exist_ok=True)
    try_decompose(y, out_dir)

    print("\nDone. Next: time_series_quant/05_shift_and_signal_alignment.md")


if __name__ == "__main__":
    main()
