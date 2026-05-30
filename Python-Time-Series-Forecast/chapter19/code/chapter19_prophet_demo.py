"""
《Python 时间序列预测》第 19 章配套：Prophet vs 季节基线 vs SARIMA（chocolate 月度）

运行：
  python Python-Time-Series-Forecast/code/chapter19_prophet_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
推荐：pip install prophet  (Python 3.10–3.12; formerly fbprophet)
"""

from __future__ import annotations

import itertools
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

SEED = 42
np.random.seed(SEED)
TEST_MONTHS = 12
BOOK_MAE = {"baseline": 10.92, "sarima": 10.09, "prophet": 7.42}


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


def chocolate_monthly(n_months: int = 120, seed: int = SEED) -> pd.DataFrame:
    """Synthetic Google-Trends-like monthly 'chocolate' index."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2004-01", periods=n_months, freq="MS") + pd.offsets.MonthEnd(1)
    t = np.arange(n_months)
    trend = 50 + 0.15 * t
    yearly = 12 * np.sin(2 * np.pi * (idx.month - 1) / 12)
    xmas = np.where(idx.month == 12, -8, 0)
    noise = rng.normal(0, 2, n_months)
    y = trend + yearly + xmas + noise
    return pd.DataFrame({"ds": idx, "y": y})


def mae(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean(np.abs(actual - pred)))


def seasonal_naive_yoy(train: pd.DataFrame, test: pd.DataFrame) -> np.ndarray:
    """Repeat values from 12 months earlier (book baseline)."""
    hist = pd.concat([train, test]).sort_values("ds")
    preds = []
    for d in test["ds"]:
        ref = d - pd.DateOffset(months=12)
        val = hist.loc[hist["ds"] == ref, "y"]
        preds.append(float(val.iloc[0]) if len(val) else float(train["y"].iloc[-1]))
    return np.array(preds)


def fit_sarima_book(train: pd.Series) -> tuple:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    order = (1, 1, 1)
    seasonal = (1, 0, 1, 12)
    res = SARIMAX(
        train,
        order=order,
        seasonal_order=seasonal,
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)
    return order, seasonal, res


def sarima_forecast(res, steps: int) -> np.ndarray:
    return res.forecast(steps).to_numpy()


def small_prophet_grid(Prophet, train: pd.DataFrame) -> dict:
    """Compact CV grid (book: changepoint_prior_scale, seasonality_prior_scale)."""
    from prophet.diagnostics import cross_validation, performance_metrics

    grid = {
        "changepoint_prior_scale": [0.01, 0.05, 0.1],
        "seasonality_prior_scale": [1.0, 5.0, 10.0],
    }
    best_mae = np.inf
    best_params = {"changepoint_prior_scale": 0.05, "seasonality_prior_scale": 10.0}
    all_params = [
        dict(zip(grid.keys(), v)) for v in itertools.product(*grid.values())
    ]
    horizon_days = f"{min(365, len(train) // 3)} days"
    initial_days = f"{max(365, len(train) // 2)} days"
    period_days = "180 days"

    for params in all_params[:4]:  # limit for demo speed
        m = Prophet(**params, yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
        m.add_country_holidays(country_name="US")
        m.fit(train)
        try:
            cv = cross_validation(
                m,
                initial=initial_days,
                period=period_days,
                horizon=horizon_days,
                parallel=None,
            )
            pm = performance_metrics(cv, rolling_window=1)
            cv_mae = float(pm["mae"].mean())
            if cv_mae < best_mae:
                best_mae = cv_mae
                best_params = params
        except Exception:
            continue
    return best_params


def run_prophet(Prophet, train: pd.DataFrame, test: pd.DataFrame, tune: bool = True) -> tuple[np.ndarray, dict]:
    params = (
        small_prophet_grid(Prophet, train)
        if tune and len(train) > 48
        else {"changepoint_prior_scale": 0.05, "seasonality_prior_scale": 10.0}
    )
    m = Prophet(
        **params,
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False,
    )
    m.add_country_holidays(country_name="US")
    m.fit(train)
    future = m.make_future_dataframe(periods=TEST_MONTHS, freq="MS")
    future["ds"] = pd.to_datetime(future["ds"]) + pd.offsets.MonthEnd(1)
    fc = m.predict(future)
    merged = test.merge(fc[["ds", "yhat"]], on="ds", how="left")
    return merged["yhat"].to_numpy(), params


def main() -> None:
    print("=== 19.5 chocolate monthly (synthetic; book MAE on hold-out) ===")
    df = chocolate_monthly()
    print("=== 19.3 ds/y format, MonthEnd on ds ===")
    train = df.iloc[:-TEST_MONTHS].copy()
    test = df.iloc[-TEST_MONTHS:].copy()

    base_pred = seasonal_naive_yoy(train, test)
    mae_base = mae(test["y"].to_numpy(), base_pred)
    print(f"baseline (YoY season) MAE: {mae_base:.2f}  (book ~{BOOK_MAE['baseline']})")

    print("\n=== 19.5.2 SARIMA(1,1,1)(1,0,1)12 ===")
    order, seas, res = fit_sarima_book(train.set_index("ds")["y"])
    sar_pred = sarima_forecast(res, TEST_MONTHS)
    mae_sar = mae(test["y"].to_numpy(), sar_pred)
    print(f"SARIMA {order}{seas} MAE: {mae_sar:.2f}  (book ~{BOOK_MAE['sarima']})")

    Prophet = try_import_prophet()
    if Prophet is None:
        print("\nProphet not installed. pip install prophet (Python 3.10–3.12 recommended).")
        print(f"Book test MAE: Prophet {BOOK_MAE['prophet']} < SARIMA {BOOK_MAE['sarima']} < baseline {BOOK_MAE['baseline']}")
        print("=== 19.6 next: ch.20 steak price capstone ===")
        return

    print("\n=== 19.4–19.5 Prophet + US holidays + small CV grid ===")
    pro_pred, best = run_prophet(Prophet, train, test, tune=True)
    mae_pro = mae(test["y"].to_numpy(), pro_pred)
    print(f"best params (demo grid): {best}")
    print(f"Prophet MAE: {mae_pro:.2f}  (book ~{BOOK_MAE['prophet']})")

    m = Prophet(
        changepoint_prior_scale=best["changepoint_prior_scale"],
        seasonality_prior_scale=best["seasonality_prior_scale"],
        yearly_seasonality=True,
    )
    m.add_country_holidays(country_name="US")
    m.fit(train)
    fc = m.predict(m.make_future_dataframe(periods=TEST_MONTHS, freq="MS"))
    try:
        import tempfile

        import matplotlib

        matplotlib.use("Agg")
        fig = m.plot(fc)
        out = Path(tempfile.gettempdir()) / "tsf_ch19_prophet_forecast.png"
        fig.savefig(out, dpi=120)
        print(f"forecast plot: {out}")
    except Exception as e:
        print("plot skipped:", e)

    print("\n=== 19.6 Prophet is not a silver bullet; compare with SARIMAX/LSTM ===")
    print("=== next: ch.20 Canada steak retail price capstone ===")


if __name__ == "__main__":
    main()
