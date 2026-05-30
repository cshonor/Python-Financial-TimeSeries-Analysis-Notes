"""
《Python 时间序列预测》第 20 章配套：加拿大牛排月均价 — 基线 vs Prophet vs SARIMA

运行：
  python Python-Time-Series-Forecast/code/chapter20_capstone_steak_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
可选：pip install prophet
"""

from __future__ import annotations

import itertools
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

SEED = 42
np.random.seed(SEED)
TEST_MONTHS = 36
BOOK_MAE = {"baseline": 0.681, "prophet": 1.163, "sarima": 0.678}
BOOK_SARIMA = ((2, 1, 3), (1, 0, 1, 12))


def try_import_prophet():
    try:
        from prophet import Prophet

        return Prophet
    except ImportError:
        try:
            from fbprophet import Prophet  # type: ignore

            return Prophet
        except ImportError:
            return None


def steak_monthly(n_months: int = 323, seed: int = SEED) -> pd.DataFrame:
    """Synthetic StatsCan round steak: strong trend, weak season (book pattern)."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("1995-01", periods=n_months, freq="MS") + pd.offsets.MonthEnd(1)
    t = np.arange(n_months)
    trend = 7.5 + 0.025 * t
    weak = 0.15 * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(0, 0.25, n_months)
    return pd.DataFrame({"ds": idx, "y": trend + weak + noise})


def mae(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean(np.abs(a - b)))


def adf_p(s: pd.Series) -> float:
    from statsmodels.tsa.stattools import adfuller

    return float(adfuller(s.dropna())[1])


def baseline_last_value(train: pd.DataFrame, n: int) -> np.ndarray:
    last = float(train["y"].iloc[-1])
    return np.full(n, last)


def optimize_sarima_aic(y: pd.Series, d: int = 1, m: int = 12, p_max: int = 2, q_max: int = 3):
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    best_aic = np.inf
    best = BOOK_SARIMA
    for p, q, P, Q in itertools.product(
        range(p_max + 1), range(q_max + 1), range(2), range(2)
    ):
        if p == 0 and q == 0:
            continue
        try:
            res = SARIMAX(
                y,
                order=(p, d, q),
                seasonal_order=(P, 0, Q, m),
                enforce_stationarity=False,
                enforce_invertibility=False,
            ).fit(disp=False)
            if res.aic < best_aic:
                best_aic = res.aic
                best = ((p, d, q), (P, 0, Q, m))
        except Exception:
            continue
    order, seas = best
    res = SARIMAX(
        y,
        order=order,
        seasonal_order=seas,
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)
    return order, seas, res


def ljungbox_ok(res, lags: int = 12) -> float:
    from statsmodels.stats.diagnostic import acorr_ljungbox

    lb = acorr_ljungbox(res.resid.dropna(), lags=[lags], return_df=True)
    return float(lb["lb_pvalue"].iloc[0])


def run_prophet_book_style(Prophet, train: pd.DataFrame, test: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """Book-like high flexibility -> can hurt on low-seasonality series."""
    params = {"changepoint_prior_scale": 1.0, "seasonality_prior_scale": 10.0}
    m = Prophet(
        **params,
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False,
    )
    m.fit(train)
    future = m.make_future_dataframe(periods=len(test), freq="MS")
    future["ds"] = pd.to_datetime(future["ds"]) + pd.offsets.MonthEnd(1)
    fc = m.predict(future)
    merged = test.merge(fc[["ds", "yhat"]], on="ds", how="left")
    return merged["yhat"].to_numpy(), params


def main() -> None:
    print("=== 20.1 Round steak 1kg monthly (synthetic StatsCan-like, n~323) ===")
    raw = steak_monthly()
    print(f"rows={len(raw)}  (book ~323)")

    print("\n=== 20.2 trend up, weak visible season ===")
    print(f"mean y={raw['y'].mean():.2f}, last y={raw['y'].iloc[-1]:.2f}")

    train = raw.iloc[:-TEST_MONTHS].copy()
    test = raw.iloc[-TEST_MONTHS:].copy()

    print("\n=== 20.4 ADF: level vs diff1 ===")
    print(f"level p={adf_p(train.set_index('ds')['y']):.4f}  (book ~0.98)")
    print(f"diff1 p={adf_p(train.set_index('ds')['y'].diff().dropna()):.4f}")

    base = baseline_last_value(train, len(test))
    mae_base = mae(test["y"].to_numpy(), base)
    print(f"\n=== 20.3 baseline (last value flat) MAE: {mae_base:.3f}  (book {BOOK_MAE['baseline']})")

    Prophet = try_import_prophet()
    if Prophet is not None:
        pro, params = run_prophet_book_style(Prophet, train, test)
        mae_pro = mae(test["y"].to_numpy(), pro)
        print(f"Prophet {params} MAE: {mae_pro:.3f}  (book {BOOK_MAE['prophet']})")
        print("Prophet worse than baseline:", mae_pro > mae_base)
    else:
        print(f"Prophet skipped (not installed). Book MAE {BOOK_MAE['prophet']} > baseline.")

    print("\n=== 20.4 SARIMA grid (target book order (2,1,3)(1,0,1)12) ===")
    y_tr = train.set_index("ds")["y"]
    order, seas, res = optimize_sarima_aic(y_tr, d=1, m=12)
    print(f"selected {order} x {seas}, AIC={res.aic:.1f}")
    print(f"Ljung-Box p (lag 12): {ljungbox_ok(res):.4f}")
    sar = res.forecast(len(test)).to_numpy()
    mae_sar = mae(test["y"].to_numpy(), sar)
    print(f"SARIMA MAE: {mae_sar:.3f}  (book {BOOK_MAE['sarima']})")

    print("\n=== 20.5 recap: no silver bullet; add exogenous features ===")
    print("Practice: other 51 products, NYC Open Data, Statistics Canada.")
    print("《Python 时间序列预测》全书流程至此收官。")


if __name__ == "__main__":
    main()
