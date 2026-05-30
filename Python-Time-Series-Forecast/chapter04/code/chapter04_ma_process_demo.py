"""
《Python 时间序列预测》第 4 章配套：MA(q) 模拟 / ACF / SARIMAX(0,0,q) / 滚动预测 / 逆变换

运行：
  python Python-Time-Series-Forecast/code/chapter04_ma_process_demo.py

依赖：pip install numpy pandas statsmodels matplotlib
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd


def simulate_ma2(n: int = 400, seed: int = 0) -> pd.Series:
    from statsmodels.tsa.arima_process import ArmaProcess

    # MA(2): y_t = e_t + 0.6 e_{t-1} + 0.3 e_{t-2}
    ar = np.array([1.0])
    ma = np.array([1.0, 0.6, 0.3])
    proc = ArmaProcess(ar, ma)
    y = proc.generate_sample(nsample=n, burnin=100, scale=1.0)
    idx = pd.date_range("2015-01-01", periods=n, freq="B")
    return pd.Series(y, index=idx, name="y")


def choose_q_from_acf(y: pd.Series, max_lag: int = 10) -> int:
    from statsmodels.tsa.stattools import acf

    acf_vals = acf(y, nlags=max_lag, fft=True)[1:]  # drop lag 0
    # crude rule: last lag above 2/sqrt(n) before cutoff
    thresh = 2 / np.sqrt(len(y))
    sig = np.where(np.abs(acf_vals) > thresh)[0]
    return int(sig[-1] + 1) if len(sig) else 1


def rolling_forecast_ma(
    train: pd.Series, test: pd.Series, q: int, refit_every: int = 8
) -> pd.Series:
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    history = train.copy()
    preds: list[float] = []
    steps = min(q, 1) if q >= 1 else 1  # MA(1)+ use 1-step rolls

    for i in range(len(test)):
        if i % refit_every == 0 or i == 0:
            model = SARIMAX(history, order=(0, 0, q), enforce_stationarity=False)
            res = model.fit(disp=False)
        fc = res.forecast(steps=steps)
        preds.append(float(fc.iloc[-1] if hasattr(fc, "iloc") else fc[-1]))
        history = pd.concat([history, test.iloc[[i]]])

    return pd.Series(preds, index=test.index, name="forecast")


def diff_inverse(y0: float, diff_pred: pd.Series) -> pd.Series:
    return y0 + diff_pred.cumsum()


def mse(actual: pd.Series, pred: pd.Series) -> float:
    err = actual - pred
    return float((err**2).mean())


def main() -> None:
    print("=== 4.1 simulate MA(2) ===")
    y = simulate_ma2()
    print(y.head(3))

    print("\n=== 4.1 ACF suggest q ===")
    q_hint = choose_q_from_acf(y)
    print("suggested q (heuristic):", q_hint, "| fitting q=2 per chapter")

    q = 2
    n_test = 40
    train, test = y.iloc[:-n_test], y.iloc[-n_test:]

    print("\n=== 4.2 fit SARIMAX(0,0,q) one-step vs multi-step ===")
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    res = SARIMAX(train, order=(0, 0, q), enforce_stationarity=False).fit(disp=False)
    direct = res.forecast(steps=min(q, len(test)))
    print(f"direct forecast ({len(direct)} steps):", direct.values.round(4)[: q])
    beyond = res.forecast(steps=q + 5)
    print(f"forecast step q+5 (often ~mean):", float(beyond.iloc[-1]))

    print("\n=== 4.2 rolling forecast on test ===")
    roll = rolling_forecast_ma(train, test, q=q, refit_every=10)
    print("rolling MSE:", round(mse(test, roll), 6))

    print("\n=== 4.2 diff + inverse transform demo ===")
    levels = (100 + y.cumsum()).rename("level")
    diff = levels.diff().dropna()
    y0 = float(levels.iloc[len(train) - 1])
    d_train = diff.iloc[: len(train) - 1]
    d_test = diff.iloc[len(train) - 1 : len(train) - 1 + n_test]
    d_res = SARIMAX(d_train, order=(0, 0, 1), enforce_stationarity=False).fit(disp=False)
    d_fc = d_res.forecast(steps=len(d_test))
    level_fc = diff_inverse(y0, pd.Series(d_fc, index=d_test.index))
    level_actual = levels.loc[d_test.index]
    print("level MSE after inverse:", round(mse(level_actual, level_fc), 6))

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from statsmodels.graphics.tsaplots import plot_acf

        fig, ax = plt.subplots(figsize=(7, 4))
        plot_acf(y, lags=20, ax=ax, alpha=0.05)
        ax.set_title("ACF of simulated MA(2)")
        path = Path(tempfile.gettempdir()) / "tsf_ch04_acf.png"
        fig.savefig(path, dpi=120, bbox_inches="tight")
        plt.close(fig)
        print("\nSaved ACF:", path)
    except ImportError:
        pass

    print("\nDone. Next chapter: AR(p) when ACF decays slowly.")


if __name__ == "__main__":
    main()
