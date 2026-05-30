"""
《Python 时间序列预测》第 7 章配套：定 d / ARIMA 网格(AIC) / 对比季节朴素 MAPE

运行：
  python Python-Time-Series-Forecast/code/chapter07_arima_demo.py
"""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd


def jj_quarterly_eps(n_years: int = 21, seed: int = 4) -> pd.Series:
    """Synthetic J&J-like quarterly EPS: trend + seasonality."""
    rng = np.random.default_rng(seed)
    n = n_years * 4
    t = np.arange(n)
    trend = 3 + 0.12 * t
    season = np.tile([0.5, 0.3, 0.2, -0.4], n // 4 + 1)[:n]
    noise = rng.normal(0, 0.15, n)
    idx = pd.period_range("1960Q1", periods=n, freq="Q").to_timestamp()
    return pd.Series(trend + season + noise, index=idx, name="eps")


def adf_pvalue(y: pd.Series) -> float:
    from statsmodels.tsa.stattools import adfuller

    return float(adfuller(y.dropna())[1])


def infer_d(y: pd.Series, max_d: int = 2) -> int:
    if adf_pvalue(y) < 0.05:
        return 0
    for d in range(1, max_d + 1):
        diff = y.copy()
        for _ in range(d):
            diff = diff.diff()
        if adf_pvalue(diff.dropna()) < 0.05:
            return d
    return max_d


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs((actual - pred) / actual)) * 100)


def seasonal_naive(train: pd.Series, test: pd.Series, m: int = 4) -> np.ndarray:
    return np.tile(train.iloc[-m:].to_numpy(), len(test) // m + 1)[: len(test)]


def optimize_arima_fixed_d(
    y: pd.Series, d: int, p_max: int = 3, q_max: int = 3
) -> tuple[tuple[int, int, int], float, pd.DataFrame]:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    rows: list[dict] = []
    best_aic = np.inf
    best = (0, d, 0)

    for p, q in itertools.product(range(p_max + 1), range(q_max + 1)):
        if p == 0 and q == 0:
            continue
        try:
            res = SARIMAX(
                y,
                order=(p, d, q),
                enforce_stationarity=False,
                enforce_invertibility=False,
            ).fit(disp=False)
            rows.append({"p": p, "d": d, "q": q, "aic": res.aic})
            if res.aic < best_aic:
                best_aic = res.aic
                best = (p, d, q)
        except Exception:
            continue

    return best, best_aic, pd.DataFrame(rows).sort_values("aic")


def ljungbox_ok(res, lags: int = 10) -> bool:
    from statsmodels.stats.diagnostic import acorr_ljungbox

    lb = acorr_ljungbox(res.resid.dropna(), lags=[lags], return_df=True)
    return float(lb["lb_pvalue"].iloc[0]) > 0.05


def main() -> None:
    y = jj_quarterly_eps()
    n_test = 4
    train, test = y.iloc[:-n_test], y.iloc[-n_test:]

    print("=== 7.3 ADF & choose d ===")
    print(f"level p={adf_pvalue(y):.4f}")
    print(f"diff1 p={adf_pvalue(y.diff().dropna()):.4f}")
    d = infer_d(y, max_d=2)
    print(f"inferred d={d} (book: d=2 for J&J)")

    print("\n=== 7.2 grid ARIMA(p,d,q) with FIXED d ===")
    best, aic, table = optimize_arima_fixed_d(train, d=d, p_max=3, q_max=3)
    print(table.head(5).to_string(index=False))
    print(f"best order={best}, AIC={aic:.1f}")

    from statsmodels.tsa.statespace.sarimax import SARIMAX

    res = SARIMAX(
        train, order=best, enforce_stationarity=False, enforce_invertibility=False
    ).fit(disp=False)
    print("Ljung-Box OK (p>0.05):", ljungbox_ok(res))

    fc = res.forecast(steps=len(test))
    sn = seasonal_naive(train, test, m=4)

    print("\n=== MAPE vs seasonal naive (1980 hold-out) ===")
    print(f"seasonal naive MAPE: {mape(test.to_numpy(), sn):.2f}%")
    print(f"ARIMA{best} MAPE:      {mape(test.to_numpy(), fc.to_numpy()):.2f}%")
    print("(book: ~11.56% vs ~2.19% on real J&J)")

    print("\nDone. Next: chapter08_sarima_demo.py for seasonal extension.")


if __name__ == "__main__":
    main()
