"""
《Python 时间序列预测》第 11 章配套：澳大利亚抗糖尿病处方 Capstone
STL / ADF+季节差分 / SARIMA 网格 / 残差 / 12 月块滚动 / MAPE vs 季节朴素

运行：
  python Python-Time-Series-Forecast/code/chapter11_capstone_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
"""

from __future__ import annotations

import itertools
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

np.random.seed(11)

BOOK_ORDER = (2, 1, 3)
BOOK_SEASONAL = (1, 1, 3, 12)
M = 12


def aus_antidiabetic_like(
    start: str = "1991-01",
    end: str = "2008-12",
    seed: int = 11,
) -> pd.Series:
    """Seasonal random-walk + calendar season (I(1) x seasonal unit root flavor)."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, end, freq="MS")
    n = len(idx)
    month = idx.month
    seas = 10_000 * np.sin(2 * np.pi * (month - 1) / 12 - np.pi / 2)
    y = np.zeros(n)
    for t in range(n):
        if t < M:
            y[t] = 85_000 + seas[t] + rng.normal(0, 2_000)
        else:
            y[t] = y[t - M] + 380 + seas[t] - seas[t - M] + rng.normal(0, 1_800)
    return pd.Series(np.maximum(y, 5_000), index=idx, name="scripts")


def adf_p(y: pd.Series) -> float:
    from statsmodels.tsa.stattools import adfuller

    return float(adfuller(y.dropna())[1])


def seasonal_diff_once(y: pd.Series, m: int = M) -> pd.Series:
    return y.diff().diff(m).dropna()


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs((actual - pred) / actual)) * 100)


def seasonal_naive_forecast(train: pd.Series, test: pd.Series, m: int = M) -> pd.Series:
    cycle = train.iloc[-m:].to_numpy()
    reps = int(np.ceil(len(test) / m))
    vals = np.tile(cycle, reps)[: len(test)]
    return pd.Series(vals, index=test.index, name="seasonal_naive")


def fit_sarima(y: pd.Series, order: tuple, seasonal_order: tuple):
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    return SARIMAX(
        y,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)


def grid_candidates(full_book_grid: bool = False) -> list[tuple[int, int, int, int]]:
    """Book: p,q,P,Q in 0..4 (625 fits). Default: focused grid for demo speed."""
    if full_book_grid:
        return [
            (p, q, P, Q)
            for p, q, P, Q in itertools.product(range(5), repeat=4)
            if not (p == 0 and q == 0)
        ]
    return [
        (2, 3, 1, 3),
        (2, 2, 1, 3),
        (2, 3, 1, 2),
        (1, 3, 1, 3),
        (3, 3, 1, 3),
        (2, 1, 1, 1),
    ]


def best_sarima_aic(
    y: pd.Series,
    d: int,
    D: int,
    m: int,
    candidates: list[tuple[int, int, int, int]],
) -> tuple[tuple, tuple, float]:
    best_aic = np.inf
    best_order = (0, d, 0)
    best_seas = (0, D, 0, m)
    for p, q, P, Q in candidates:
        try:
            res = fit_sarima(y, (p, d, q), (P, D, Q, m))
            if res.aic < best_aic:
                best_aic = res.aic
                best_order = (p, d, q)
                best_seas = (P, D, Q, m)
        except Exception:
            continue
    return best_order, best_seas, best_aic


def ljungbox_report(res, lags: list[int] | None = None) -> None:
    from statsmodels.stats.diagnostic import acorr_ljungbox

    if lags is None:
        lags = [12, 24]
    lb = acorr_ljungbox(res.resid.dropna(), lags=lags, return_df=True)
    for lag in lags:
        p = float(lb.loc[lag, "lb_pvalue"])
        print(f"  lag {lag}: Ljung-Box p={p:.4f} ({'ok' if p > 0.05 else 'check'})")


def rolling_block_forecast(
    train: pd.Series,
    test: pd.Series,
    order: tuple,
    seasonal_order: tuple,
    block: int = 12,
) -> pd.Series:
    history = train.copy()
    chunks: list[pd.Series] = []
    for start in range(0, len(test), block):
        res = fit_sarima(history, order, seasonal_order)
        steps = min(block, len(test) - start)
        fc = res.forecast(steps)
        chunk = pd.Series(fc, index=test.index[start : start + steps])
        chunks.append(chunk)
        history = pd.concat([history, test.iloc[start : start + steps]])
    return pd.concat(chunks)


def main() -> None:
    y = aus_antidiabetic_like()
    n_test = 36
    train, test = y.iloc[:-n_test], y.iloc[-n_test:]

    print("=== 11.1 load: monthly scripts, test last 36 months ===")
    print(f"range {y.index[0].date()} .. {y.index[-1].date()}, n={len(y)}")

    print("\n=== 11.2 STL (train) ===")
    from statsmodels.tsa.seasonal import STL

    stl = STL(train, period=M, robust=True).fit()
    print(f"trend slope ~ {np.polyfit(np.arange(len(train)), stl.trend, 1)[0]:.1f}/month")
    print(f"seasonal std ~ {stl.seasonal.std():.0f}")

    print("\n=== 11.3 stationarity ADF (book: 1.0 -> 0.12 -> 0.0) ===")
    print(f"level       p={adf_p(y):.4f}")
    print(f"diff d=1    p={adf_p(y.diff().dropna()):.4f}")
    print(f"diff+seas   p={adf_p(seasonal_diff_once(y)):.4f}  -> SARIMA(p,1,q)(P,1,Q)12")

    d, D = 1, 1
    print("\n=== 11.3.1 SARIMA grid (AIC); book SARIMA(2,1,3)(1,1,3)12 ===")
    order, seas, aic = best_sarima_aic(train, d, D, M, grid_candidates())
    print(f"grid best order={order}, seasonal={seas}, AIC={aic:.1f}")

    res_book = fit_sarima(train, BOOK_ORDER, BOOK_SEASONAL)
    print(f"book  order={BOOK_ORDER}, seasonal={BOOK_SEASONAL}, AIC={res_book.aic:.1f}")

    use_order, use_seas = BOOK_ORDER, BOOK_SEASONAL
    print("\n=== 11.3.2 residuals (book model) ===")
    ljungbox_report(res_book)

    print("\n=== 11.4 rolling 3x12-month blocks on 36-month test ===")
    fc = rolling_block_forecast(train, test, use_order, use_seas, block=12)
    sn = seasonal_naive_forecast(train, test, m=M)
    m_sarima = mape(test.to_numpy(), fc.to_numpy())
    m_sn = mape(test.to_numpy(), sn.to_numpy())
    print(f"SARIMA MAPE: {m_sarima:.2f}%  (book ~7.90%)")
    print(f"seasonal naive MAPE: {m_sn:.2f}%  (book ~12.69%)")
    print("SARIMA beats baseline:", m_sarima < m_sn)

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(10, 4))
        test.plot(ax=ax, label="actual", color="black", lw=1.5)
        fc.plot(ax=ax, label="SARIMA rolling", ls="--")
        sn.plot(ax=ax, label="seasonal naive", ls=":", alpha=0.8)
        ax.legend()
        ax.set_title("Capstone hold-out (last 36 months)")
        path = Path(tempfile.gettempdir()) / "tsf_ch11_holdout.png"
        fig.tight_layout()
        fig.savefig(path, dpi=120)
        plt.close(fig)
        print(f"plot saved: {path}")
    except ImportError:
        pass

    print("\n=== 11.5 Part II complete -> ch.12 deep learning ===")
    print("Tip: set grid_candidates(full_book_grid=True) to reproduce 625-fit book search (slow).")


if __name__ == "__main__":
    main()
