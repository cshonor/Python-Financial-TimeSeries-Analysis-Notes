"""
《Python 时间序列预测》第 8 章配套：STL 分解 / ARIMA vs SARIMA / AIC / Ljung-Box

运行：
  python Python-Time-Series-Forecast/code/chapter08_sarima_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
"""

from __future__ import annotations

import itertools
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def air_passengers_like(n: int = 144, seed: int = 3) -> pd.Series:
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    trend = 100 + 0.8 * t
    seasonal = 25 * np.sin(2 * np.pi * t / 12) + 10 * np.cos(2 * np.pi * t / 12)
    noise = rng.normal(0, 4, n)
    idx = pd.period_range("1949-01", periods=n, freq="M").to_timestamp()
    return pd.Series(trend + seasonal + noise, index=idx, name="passengers")


def seasonal_naive(train: pd.Series, test: pd.Series, m: int = 12) -> pd.Series:
    last_cycle = train.iloc[-m:].to_numpy()
    reps = int(np.ceil(len(test) / m))
    vals = np.tile(last_cycle, reps)[: len(test)]
    return pd.Series(vals, index=test.index, name="forecast")


def mae(actual: pd.Series, pred: pd.Series) -> float:
    return float((actual - pred).abs().mean())


def fit_aic(order, seasonal_order, y: pd.Series):
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    return SARIMAX(
        y,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)


def small_grid(y: pd.Series, m: int = 12) -> list[tuple]:
    """Compact grid for demo speed."""
    candidates = []
    for p, d, q in [(1, 1, 1), (2, 1, 1), (1, 2, 1)]:
        for P, D, Q in [(0, 0, 0), (1, 1, 1), (1, 1, 2)]:
            candidates.append(((p, d, q), (P, D, Q, m)))
    return candidates


def best_by_aic(y: pd.Series, candidates: list[tuple]) -> tuple:
    best = None
    best_aic = np.inf
    for order, seas in candidates:
        try:
            res = fit_aic(order, seas, y)
            if res.aic < best_aic:
                best_aic = res.aic
                best = (order, seas, res)
        except Exception:
            continue
    if best is None:
        raise RuntimeError("no model converged")
    return best


def ljungbox_min_p(res, lags: int = 10) -> float:
    from statsmodels.stats.diagnostic import acorr_ljungbox

    lb = acorr_ljungbox(res.resid.dropna(), lags=[lags], return_df=True)
    return float(lb["lb_pvalue"].iloc[0])


def main() -> None:
    y = air_passengers_like()
    m = 12
    n_test = 24
    train, test = y.iloc[:-n_test], y.iloc[-n_test:]

    print("=== 8.2 STL decomposition ===")
    from statsmodels.tsa.seasonal import STL

    stl = STL(train, period=m, robust=True).fit()
    print("seasonal component std:", round(float(stl.seasonal.std()), 3))

    print("\n=== 8.3 seasonal naive baseline MAE ===")
    sn = seasonal_naive(train, test, m=m)
    print("seasonal naive MAE:", round(mae(test, sn), 2))

    grid = small_grid(train, m=m)

    print("\n=== 8.3.1 ARIMA candidates (seasonal_order zeros) ===")
    arima_cands = [c for c in grid if c[1][:3] == (0, 0, 0)]
    o_a, s_a, res_a = best_by_aic(train, arima_cands)
    print(f"best ARIMA order={o_a}, AIC={res_a.aic:.1f}, LB p={ljungbox_min_p(res_a):.4f}")

    print("\n=== 8.3.2 SARIMA candidates ===")
    sarima_cands = [c for c in grid if c[1][:3] != (0, 0, 0)]
    o_s, s_s, res_s = best_by_aic(train, sarima_cands)
    print(f"best SARIMA order={o_s}, seasonal={s_s}, AIC={res_s.aic:.1f}, LB p={ljungbox_min_p(res_s):.4f}")

    fc_s = res_s.forecast(steps=len(test))
    print("SARIMA hold-out MAE:", round(mae(test, fc_s), 2))
    fc_a = res_a.forecast(steps=len(test))
    print("ARIMA hold-out MAE:", round(mae(test, fc_a), 2))

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(4, 1, figsize=(9, 8), sharex=True)
        axes[0].plot(train.index, train.values)
        axes[0].set_title("Train passengers (synthetic)")
        axes[1].plot(train.index, stl.trend)
        axes[1].set_title("STL trend")
        axes[2].plot(train.index, stl.seasonal)
        axes[2].set_title("STL seasonal")
        axes[3].plot(train.index, stl.resid)
        axes[3].set_title("STL residual")
        path = Path(tempfile.gettempdir()) / "tsf_ch08_stl.png"
        fig.tight_layout()
        fig.savefig(path, dpi=120)
        plt.close(fig)
        print("\nSaved STL plot:", path)
    except ImportError:
        pass

    print("\nDone. Next: SARIMAX with exogenous regressors.")


if __name__ == "__main__":
    main()
