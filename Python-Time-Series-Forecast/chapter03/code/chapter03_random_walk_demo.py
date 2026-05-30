"""
《Python 时间序列预测》第 3 章配套：随机游走模拟 / ADF / 差分 ACF / 单步预测

运行：
  python Python-Time-Series-Forecast/code/chapter03_random_walk_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def simulate_random_walk(
    n: int = 500, drift: float = 0.0, seed: int = 0
) -> pd.Series:
    rng = np.random.default_rng(seed)
    eps = rng.normal(0, 1, n)
    y = drift + np.cumsum(eps)
    idx = pd.date_range("2018-01-01", periods=n, freq="B")
    return pd.Series(y, index=idx, name="price")


def adf_report(y: pd.Series, label: str) -> None:
    from statsmodels.tsa.stattools import adfuller

    stat, pvalue, *_ = adfuller(y.dropna())
    print(f"ADF [{label}]: stat={stat:.4f}, p={pvalue:.4f} ->", "stationary" if pvalue < 0.05 else "non-stationary")


def one_step_naive_mse(y: pd.Series, test_ratio: float = 0.2) -> float:
    n_test = max(1, int(len(y) * test_ratio))
    train, test = y.iloc[:-n_test], y.iloc[-n_test:]
    # predict each test point with previous observed (walk-forward on test block)
    pred = test.shift(1)
    pred.iloc[0] = train.iloc[-1]
    err = test - pred
    return float((err**2).mean())


def multi_step_last_value(y: pd.Series, horizon: int) -> pd.Series:
    """3.3.1: constant forecast — errors accumulate for RW."""
    last = y.iloc[-1]
    idx = pd.date_range(y.index[-1], periods=horizon + 1, freq=y.index.freq)[1:]
    return pd.Series(last, index=idx, name="forecast")


def save_acf_plot(diff: pd.Series, out_dir: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from statsmodels.graphics.tsaplots import plot_acf

    fig, ax = plt.subplots(figsize=(8, 4))
    plot_acf(diff.dropna(), lags=30, ax=ax, alpha=0.05)
    ax.set_title("ACF of first difference (RW should show no structure)")
    path = out_dir / "ch03_acf_diff.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print("Saved ACF plot:", path)


def main() -> None:
    print("=== 3.1 simulate random walk ===")
    y = simulate_random_walk(n=500, drift=0.02)
    print(y.head(3), "\n...", y.tail(2))

    print("\n=== 3.2.1-3.2.2 ADF: levels vs first difference ===")
    adf_report(y, "levels")
    diff = y.diff().dropna()
    adf_report(diff, "first difference")

    print("\n=== 3.3.2 one-step naive MSE (last value) ===")
    print("MSE:", round(one_step_naive_mse(y), 6))

    print("\n=== 3.3.1 long horizon constant forecast (illustrative) ===")
    fc = multi_step_last_value(y, horizon=50)
    print("flat forecast sample:", fc.iloc[0], "...", fc.iloc[-1])

    out_dir = Path(tempfile.gettempdir()) / "tsf_ch03"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        save_acf_plot(diff, out_dir)
    except ImportError as e:
        print("ACF plot skipped:", e)

    print("\nDone. Demo uses synthetic data; replace with book CSV paths if needed.")


if __name__ == "__main__":
    main()
