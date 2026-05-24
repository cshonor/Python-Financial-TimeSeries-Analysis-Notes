"""
《Python 时间序列预测》第 10 章配套：VAR(p) / Granger 因果 / 滚动预测 / MAPE

运行：
  python Python-Time-Series-Forecast/code/chapter10_var_demo.py

依赖：pip install numpy pandas statsmodels
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def macro_bivariate(n: int = 200, seed: int = 6) -> pd.DataFrame:
    """Synthetic realdpi <-> realcons feedback."""
    rng = np.random.default_rng(seed)
    dpi = np.zeros(n)
    cons = np.zeros(n)
    for t in range(1, n):
        eps1, eps2 = rng.normal(0, 0.5, 2)
        dpi[t] = 0.4 * dpi[t - 1] + 0.15 * cons[t - 1] + eps1
        cons[t] = 0.15 * dpi[t - 1] + 0.35 * cons[t - 1] + eps2
    idx = pd.period_range("2000Q1", periods=n, freq="Q").to_timestamp()
    return pd.DataFrame(
        {"realdpi": 100 + np.cumsum(dpi), "realcons": 80 + np.cumsum(cons)},
        index=idx,
    )


def adf_p(s: pd.Series) -> float:
    from statsmodels.tsa.stattools import adfuller

    return float(adfuller(s.dropna())[1])


def granger_p(effect: str, cause: str, df: pd.DataFrame, maxlag: int) -> float:
    """effect caused by cause: columns [effect, cause] per statsmodels convention."""
    from statsmodels.tsa.stattools import grangercausalitytests

    data = df[[effect, cause]].dropna()
    res = grangercausalitytests(data, maxlag=[maxlag], verbose=False)
    return float(res[maxlag][0]["ssr_ftest"][1])


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs((actual - pred) / actual)) * 100)


def rolling_var_forecast(
    train: pd.DataFrame,
    test: pd.DataFrame,
    p: int,
) -> pd.DataFrame:
    from statsmodels.tsa.api import VAR

    history = train.copy()
    rows: list[np.ndarray] = []
    for _ in range(len(test)):
        res = VAR(history).fit(p)
        fc = res.forecast(res.endog[-res.k_ar :], steps=1)
        rows.append(fc[0])
        history = pd.concat([history, test.iloc[[len(rows) - 1]]])
    return pd.DataFrame(rows, index=test.index, columns=train.columns)


def diff_to_levels(
    anchor: pd.Series,
    diff_fc: pd.DataFrame,
) -> pd.DataFrame:
    return anchor + diff_fc.cumsum()


def main() -> None:
    levels = macro_bivariate()
    diff = levels.diff().dropna()

    print("=== 10.3 ADF on levels vs diff ===")
    for col in diff.columns:
        print(f"{col}: level p={adf_p(levels[col]):.4f}, diff1 p={adf_p(diff[col]):.4f}")

    n_test = int(len(diff) * 0.2)
    train, test = diff.iloc[:-n_test], diff.iloc[-n_test:]

    from statsmodels.stats.diagnostic import acorr_ljungbox
    from statsmodels.tsa.api import VAR

    sel = VAR(train).select_order(maxlags=8)
    p = int(sel.aic)
    print(f"\n=== VAR order by AIC: p={p} (book: VAR(3)) ===")

    res = VAR(train).fit(p)
    print(f"fitted VAR({res.k_ar}), nobs={res.nobs}")

    print("\n=== 10.2 Granger (p<0.05 => reject H0, cause helps predict effect) ===")
    lag = int(res.k_ar)
    p_cons_dpi = granger_p("realdpi", "realcons", train, lag)
    p_dpi_cons = granger_p("realcons", "realdpi", train, lag)
    print(f"realcons -> realdpi p={p_cons_dpi:.4f}")
    print(f"realdpi -> realcons p={p_dpi_cons:.4f}")

    print("\n=== Ljung-Box on VAR residuals (p>0.05 => white noise) ===")
    for col in train.columns:
        lb = acorr_ljungbox(res.resid[col], lags=[lag], return_df=True)
        print(f"{col}: Ljung-Box p={lb['lb_pvalue'].iloc[0]:.4f}")

    fc_diff = rolling_var_forecast(train, test, p=p)
    anchor = levels.loc[train.index[-1]]
    fc_levels = diff_to_levels(anchor, fc_diff)
    test_levels = levels.loc[test.index]

    print("\n=== MAPE on levels vs last-value baseline ===")
    for col in levels.columns:
        base_val = float(levels[col].iloc[len(train)])
        base = np.full(len(test), base_val)
        print(
            f"{col}: VAR MAPE={mape(test_levels[col].to_numpy(), fc_levels[col].to_numpy()):.2f}% "
            f"| baseline={mape(test_levels[col].to_numpy(), base):.2f}%"
        )

    print("\nDone. If one series MAPE loses to baseline, consider SARIMAX per series (book).")


if __name__ == "__main__":
    main()
