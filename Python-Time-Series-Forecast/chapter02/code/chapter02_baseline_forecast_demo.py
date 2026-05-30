"""
《Python 时间序列预测》第 2 章配套：四种基线 + MAPE（J&J 风格合成季度 EPS）

运行：
  python Python-Time-Series-Forecast/code/chapter02_baseline_forecast_demo.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    actual = np.asarray(actual, dtype=float)
    pred = np.asarray(pred, dtype=float)
    return float(np.mean(np.abs((actual - pred) / actual)) * 100)


def make_jnj_like_eps() -> pd.Series:
    """84 quarters: 1960Q1–1980Q4, trend + Q4 dip seasonality."""
    n = 84
    rng = np.random.default_rng(42)
    trend = np.linspace(3.5, 13.0, n)
    season = np.tile([1.15, 1.08, 1.02, 0.75], n // 4 + 1)[:n]
    noise = rng.normal(0, 0.15, n)
    y = trend * season + noise
    idx = pd.period_range("1960Q1", periods=n, freq="Q")
    return pd.Series(y, index=idx, name="eps")


def split_train_test(y: pd.Series, test_quarters: int = 4) -> tuple[pd.Series, pd.Series]:
    return y.iloc[:-test_quarters], y.iloc[-test_quarters:]


def forecast_historical_mean(train: pd.Series, horizon: int) -> np.ndarray:
    return np.full(horizon, train.mean())


def forecast_last_year_mean(train: pd.Series, horizon: int, freq: int = 4) -> np.ndarray:
    return np.full(horizon, train.iloc[-freq:].mean())


def forecast_last_value(train: pd.Series, horizon: int) -> np.ndarray:
    return np.full(horizon, train.iloc[-1])


def forecast_naive_seasonal(train: pd.Series, horizon: int, season_len: int = 4) -> np.ndarray:
    last_cycle = train.iloc[-season_len:].to_numpy()
    reps = int(np.ceil(horizon / season_len))
    return np.tile(last_cycle, reps)[:horizon]


def main() -> None:
    y = make_jnj_like_eps()
    train, test = split_train_test(y, test_quarters=4)
    h = len(test)
    actual = test.to_numpy()

    baselines = {
        "2.2 historical mean": forecast_historical_mean(train, h),
        "2.3 last-year mean": forecast_last_year_mean(train, h),
        "2.4 last value": forecast_last_value(train, h),
        "2.5 naive seasonal": forecast_naive_seasonal(train, h),
    }

    print("Train:", train.index[0], "->", train.index[-1], f"(n={len(train)})")
    print("Test :", test.index[0], "->", test.index[-1])
    print(f"\n{'Baseline':<22}  MAPE %")
    print("-" * 32)

    results: list[tuple[str, float]] = []
    for name, pred in baselines.items():
        score = mape(actual, pred)
        results.append((name, score))
        print(f"{name:<22}  {score:6.2f}")

    best = min(results, key=lambda x: x[1])
    print(f"\nBest baseline: {best[0]} ({best[1]:.2f}%)")
    print("Book reference (J&J): seasonal ~11.56% — complex models must beat your best baseline.")
    print("\nNext: chapter03_random_walk_demo.py")


if __name__ == "__main__":
    main()
