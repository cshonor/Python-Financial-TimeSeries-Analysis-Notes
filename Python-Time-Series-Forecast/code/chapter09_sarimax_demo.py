"""
《Python 时间序列预测》第 9 章配套：SARIMAX + exog / 单步滚动 / MAPE vs baseline

运行：
  python Python-Time-Series-Forecast/code/chapter09_sarimax_demo.py
"""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd


def macro_panel(n: int = 200, seed: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    cons = 50 + 0.05 * t + rng.normal(0, 1, n)
    invest = 20 + 0.02 * t + rng.normal(0, 0.8, n)
    rate = 3 + 0.001 * t + rng.normal(0, 0.2, n)
    unemp = 5 - 0.002 * t + rng.normal(0, 0.1, n)
    gdp = 100 + 0.08 * t + 0.3 * cons + 0.2 * invest - 0.5 * unemp + rng.normal(0, 1.5, n)
    idx = pd.period_range("2000Q1", periods=n, freq="Q").to_timestamp()
    return pd.DataFrame(
        {
            "realgdp": gdp,
            "realcons": cons,
            "realinv": invest,
            "realrate": rate,
            "unemp": unemp,
        },
        index=idx,
    )


def adf_p(y: pd.Series) -> float:
    from statsmodels.tsa.stattools import adfuller

    return float(adfuller(y.dropna())[1])


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs((actual - pred) / actual)) * 100)


def best_sarimax_aic(
    y: pd.Series,
    exog: pd.DataFrame,
    d: int,
    p_max: int = 2,
    q_max: int = 2,
) -> tuple[tuple[int, int, int], float]:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    best_aic = np.inf
    best_order = (1, d, 1)
    for p, q in itertools.product(range(p_max + 1), range(q_max + 1)):
        if p == 0 and q == 0:
            continue
        try:
            res = SARIMAX(
                y,
                exog=exog,
                order=(p, d, q),
                seasonal_order=(0, 0, 0, 0),
                enforce_stationarity=False,
                enforce_invertibility=False,
            ).fit(disp=False)
            if res.aic < best_aic:
                best_aic = res.aic
                best_order = (p, d, q)
        except Exception:
            continue
    return best_order, best_aic


def rolling_sarimax_one_step(
    y_train: pd.Series,
    exog_train: pd.DataFrame,
    y_test: pd.Series,
    exog_test: pd.DataFrame,
    order: tuple[int, int, int],
    refit_every: int = 8,
) -> pd.Series:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    history_y = y_train.copy()
    history_x = exog_train.copy()
    preds: list[float] = []
    res = None

    for i in range(len(y_test)):
        if res is None or i % refit_every == 0:
            res = SARIMAX(
                history_y,
                exog=history_x,
                order=order,
                seasonal_order=(0, 0, 0, 0),
                enforce_stationarity=False,
                enforce_invertibility=False,
            ).fit(disp=False)
        x_next = exog_test.iloc[[i]]
        fc = res.forecast(steps=1, exog=x_next)
        preds.append(float(fc.iloc[0]))
        history_y = pd.concat([history_y, y_test.iloc[[i]]])
        history_x = pd.concat([history_x, x_next])

    return pd.Series(preds, index=y_test.index, name="forecast")


def main() -> None:
    df = macro_panel()
    exog_cols = ["realcons", "realinv", "realrate", "unemp"]
    y = df["realgdp"]

    print("=== 9.2 ADF on GDP ===")
    print(f"level p={adf_p(y):.4f}, diff1 p={adf_p(y.diff().dropna()):.4f}")
    d = 1

    n_test = 20
    train, test = df.iloc[:-n_test], df.iloc[-n_test:]
    y_tr, y_te = train["realgdp"], test["realgdp"]
    x_tr, x_te = train[exog_cols], test[exog_cols]

    order, aic = best_sarimax_aic(y_tr, x_tr, d=d)
    print(f"best ARIMAX-like order={order}, AIC={aic:.1f}")

    from statsmodels.tsa.statespace.sarimax import SARIMAX

    res = SARIMAX(
        y_tr,
        exog=x_tr,
        order=order,
        seasonal_order=(0, 0, 0, 0),
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)
    print("example exog coef p-values (do NOT use for feature drop):")
    print(res.pvalues.filter(like="real").head())

    fc = rolling_sarimax_one_step(y_tr, x_tr, y_te, x_te, order)
    last_val = pd.Series(y_tr.iloc[-1], index=y_te.index)

    print("\n=== MAPE on levels (hold-out; exog observed each step) ===")
    print(f"SARIMAX one-step MAPE: {mape(y_te.to_numpy(), fc.to_numpy()):.3f}%")
    print(f"last-value MAPE:       {mape(y_te.to_numpy(), last_val.to_numpy()):.3f}%")
    print("(book GDP: ~0.70% vs ~0.74%; multi-step needs forecasting exog -> error stacks)")

    print("\nDone. Next: VAR for bidirectional multivariate series.")


if __name__ == "__main__":
    main()
