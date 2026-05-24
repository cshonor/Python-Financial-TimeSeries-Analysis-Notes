"""
《Python 时间序列预测》第 5 章配套：AR(p) 模拟 / ACF vs PACF / SARIMAX(p,0,0) / 滚动预测

运行：
  python Python-Time-Series-Forecast/code/chapter05_ar_process_demo.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def simulate_ar3_with_trend(n: int = 1000, seed: int = 1) -> pd.Series:
    """Retail-like: random walk-ish levels + AR(3) stationary innovations on diff."""
    from statsmodels.tsa.arima_process import ArmaProcess

    ar = np.array([1.0, -0.5, -0.2, -0.1])  # AR(3) polynomial
    ma = np.array([1.0])
    proc = ArmaProcess(ar, ma)
    diff = proc.generate_sample(nsample=n, burnin=200, scale=0.8)
    levels = 50 + np.cumsum(diff) + 0.01 * np.arange(n)
    idx = pd.date_range("2000-01-07", periods=n, freq="W")
    return pd.Series(levels, index=idx, name="footfall")


def suggest_p_from_pacf(y: pd.Series, max_lag: int = 12) -> int:
    from statsmodels.tsa.stattools import pacf

    vals = pacf(y, nlags=max_lag, method="ywm")[1:]
    thresh = 2 / np.sqrt(len(y))
    sig = np.where(np.abs(vals) > thresh)[0]
    return int(sig[-1] + 1) if len(sig) else 1


def rolling_forecast_ar(
    train: pd.Series, test: pd.Series, p: int, refit_every: int = 13
) -> pd.Series:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    history = train.copy()
    preds: list[float] = []
    res = None
    for i in range(len(test)):
        if i % refit_every == 0 or res is None:
            res = SARIMAX(history, order=(p, 0, 0), enforce_stationarity=False).fit(
                disp=False
            )
        fc = res.forecast(steps=1)
        preds.append(float(fc.iloc[0]))
        history = pd.concat([history, test.iloc[[i]]])
    return pd.Series(preds, index=test.index, name="forecast")


def baselines(train: pd.Series, test: pd.Series) -> dict[str, pd.Series]:
    return {
        "historical mean": pd.Series(train.mean(), index=test.index),
        "last value": pd.Series(train.iloc[-1], index=test.index),
    }


def mse(actual: pd.Series, pred: pd.Series) -> float:
    return float(((actual - pred) ** 2).mean())


def mae(actual: pd.Series, pred: pd.Series) -> float:
    return float((actual - pred).abs().mean())


def main() -> None:
    levels = simulate_ar3_with_trend()
    diff = levels.diff().dropna()

    print("=== 5.1 levels non-stationary; work on first difference ===")
    from statsmodels.tsa.stattools import adfuller

    p_level = adfuller(levels)[1]
    p_diff = adfuller(diff)[1]
    print(f"ADF p-level: {p_level:.4f}, p-diff: {p_diff:.4f}")

    p_hint = suggest_p_from_pacf(diff)
    print(f"PACF heuristic suggests p={p_hint} (book uses AR(3))")
    p = 3

    n_test = 52
    d_train = diff.iloc[:-n_test]
    d_test = diff.iloc[-n_test:]
    lvl_train = levels.iloc[:-n_test]
    lvl_test = levels.iloc[-n_test:]
    y0 = float(lvl_train.iloc[-1])

    print("\n=== 5.4 rolling AR(p) on differenced series ===")
    ar_fc = rolling_forecast_ar(d_train, d_test, p=p, refit_every=13)
    print("MSE on diff — AR:", round(mse(d_test, ar_fc), 3))
    for name, pred in baselines(d_train, d_test).items():
        print(f"  {name}: {mse(d_test, pred):.3f}")

    lvl_fc = y0 + ar_fc.cumsum()
    print(f"\nMAE on levels (inverse transform): {mae(lvl_test, lvl_fc):.2f}")

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        plot_acf(diff, lags=24, ax=axes[0], alpha=0.05)
        axes[0].set_title("ACF (slow decay -> AR candidate)")
        plot_pacf(diff, lags=24, ax=axes[1], alpha=0.05, method="ywm")
        axes[1].set_title("PACF (cutoff -> choose p)")
        path = Path(tempfile.gettempdir()) / "tsf_ch05_acf_pacf.png"
        fig.tight_layout()
        fig.savefig(path, dpi=120)
        plt.close(fig)
        print("Saved:", path)
    except ImportError:
        pass

    print("\nDone. Next: ARMA when both ACF and PACF tail off.")


if __name__ == "__main__":
    main()
