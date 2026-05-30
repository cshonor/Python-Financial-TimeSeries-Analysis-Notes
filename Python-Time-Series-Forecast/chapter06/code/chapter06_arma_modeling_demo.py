"""
《Python 时间序列预测》第 6 章配套：ARMA 网格 + AIC + Ljung-Box + 滚动预测

运行：
  python Python-Time-Series-Forecast/code/chapter06_arma_modeling_demo.py
"""

from __future__ import annotations

import itertools
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def simulate_bandwidth(n: int = 2000, seed: int = 2) -> pd.Series:
    from statsmodels.tsa.arima_process import ArmaProcess

    ar = np.array([1.0, -0.4, -0.1])
    ma = np.array([1.0, 0.7, 0.2])
    proc = ArmaProcess(ar, ma)
    diff = proc.generate_sample(nsample=n, burnin=200, scale=2.0)
    levels = 100 + np.cumsum(diff) + 0.005 * np.arange(n)
    idx = pd.date_range("2020-01-01", periods=n, freq="h")
    return pd.Series(levels, index=idx, name="mbps")


def optimize_arma(
    y: pd.Series, p_max: int = 3, q_max: int = 3
) -> tuple[tuple[int, int], float, pd.DataFrame]:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    rows: list[dict] = []
    best_aic = np.inf
    best_order = (0, 0)

    for p, q in itertools.product(range(p_max + 1), range(q_max + 1)):
        if p == 0 and q == 0:
            continue
        try:
            res = SARIMAX(
                y, order=(p, 0, q), enforce_stationarity=False, enforce_invertibility=False
            ).fit(disp=False)
            aic = res.aic
            rows.append({"p": p, "q": q, "aic": aic})
            if aic < best_aic:
                best_aic = aic
                best_order = (p, q)
        except Exception:
            continue

    table = pd.DataFrame(rows).sort_values("aic")
    return best_order, best_aic, table


def residual_diagnostics(res) -> None:
    from statsmodels.stats.diagnostic import acorr_ljungbox

    resid = res.resid.dropna()
    lb = acorr_ljungbox(resid, lags=[10], return_df=True)
    print("Ljung-Box lag=10 p-value:", float(lb["lb_pvalue"].iloc[0]))
    print("(want p > 0.05 => residuals look uncorrelated)")


def rolling_forecast_arma(
    train: pd.Series,
    test: pd.Series,
    order: tuple[int, int],
    steps: int,
    refit_every: int = 24,
) -> pd.Series:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    p, q = order
    history = train.copy()
    preds: list[float] = []
    fitted = None
    for i in range(0, len(test), steps):
        if fitted is None or (i // steps) % (refit_every // max(steps, 1)) == 0:
            fitted = SARIMAX(
                history,
                order=(p, 0, q),
                enforce_stationarity=False,
                enforce_invertibility=False,
            ).fit(disp=False)
        block = test.iloc[i : i + steps]
        fc = fitted.forecast(steps=len(block))
        preds.extend(fc.tolist())
        history = pd.concat([history, block])
    return pd.Series(preds[: len(test)], index=test.index, name="forecast")


def mse(a: pd.Series, b: pd.Series) -> float:
    return float(((a - b) ** 2).mean())


def main() -> None:
    levels = simulate_bandwidth(n=2000)
    diff = levels.diff().dropna()

    from statsmodels.tsa.stattools import adfuller

    print("=== 6.1 ADF levels vs diff ===")
    print(f"levels p={adfuller(levels)[1]:.4f}, diff p={adfuller(diff)[1]:.4f}")

    n_test = 168
    d_train, d_test = diff.iloc[:-n_test], diff.iloc[-n_test:]

    print("\n=== 6.4 AIC grid on differenced train ===")
    best, best_aic, table = optimize_arma(d_train, p_max=3, q_max=3)
    print(table.head(5).to_string(index=False))
    print(f"best order (p,q)={best}, AIC={best_aic:.2f}")

    from statsmodels.tsa.statespace.sarimax import SARIMAX

    p, q = best
    res = SARIMAX(
        d_train, order=(p, 0, q), enforce_stationarity=False, enforce_invertibility=False
    ).fit(disp=False)
    print("\n=== 6.4 residual diagnostics ===")
    residual_diagnostics(res)

    steps = max(p, q, 1)
    print(f"\n=== 6.6 rolling forecast steps={steps} ===")
    fc = rolling_forecast_arma(d_train, d_test, best, steps=steps, refit_every=48)
    print("MSE diff ARMA:", round(mse(d_test, fc), 3))
    print("MSE diff last-value:", round(mse(d_test, pd.Series(d_train.iloc[-1], index=d_test.index)), 3))

    y0 = float(levels.iloc[len(d_train)])
    lvl_fc = y0 + fc.cumsum()
    lvl_test = levels.iloc[-n_test:]
    print("MAE levels:", round(float((lvl_test - lvl_fc).abs().mean()), 2))

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import statsmodels.api as sm

        fig = plt.figure(figsize=(8, 6))
        ax1 = fig.add_subplot(211)
        sm.graphics.qqplot(res.resid.dropna(), line="45", ax=ax1)
        ax1.set_title("Residual Q-Q")
        ax2 = fig.add_subplot(212)
        from statsmodels.graphics.tsaplots import plot_acf

        plot_acf(res.resid.dropna(), lags=20, ax=ax2, alpha=0.05)
        ax2.set_title("Residual ACF")
        path = Path(tempfile.gettempdir()) / "tsf_ch06_diag.png"
        fig.tight_layout()
        fig.savefig(path, dpi=120)
        plt.close(fig)
        print("Saved diagnostics:", path)
    except ImportError:
        pass

    print("\nDone. Next: ARIMA with integration order d.")


if __name__ == "__main__":
    main()
