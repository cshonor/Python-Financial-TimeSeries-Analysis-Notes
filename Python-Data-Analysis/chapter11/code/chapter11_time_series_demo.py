"""
第 11 章配套：时间序列（切片 / shift / resample / rolling / ewm）

运行：
  python Python-Data-Analysis/code/chapter11_time_series_demo.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    print("=== 11.2.1 DatetimeIndex slice ===")
    idx = pd.date_range("2025-01-01", periods=10, freq="B")
    close = pd.Series(
        100 + np.cumsum(np.random.default_rng(0).normal(0, 0.5, len(idx))),
        index=idx,
        name="close",
    )
    print(close["2025-01"])
    print("truncate:\n", close.truncate(after="2025-01-08"))

    print("\n=== 11.2.2 duplicate index + groupby ===")
    dup_idx = pd.to_datetime(["2025-01-02", "2025-01-02", "2025-01-03"])
    dup = pd.Series([10.0, 10.1, 10.2], index=dup_idx)
    print("is_unique:", dup.index.is_unique)
    print("group mean:\n", dup.groupby(level=0).mean())

    print("\n=== 11.3.1 date_range / 11.3.3 shift returns ===")
    cal = pd.date_range("2025-01-01", periods=5, freq="B", normalize=True)
    print("business days:", list(cal.strftime("%Y-%m-%d")))
    ret = close / close.shift(1) - 1
    print("returns head:\n", ret.dropna().head(3))

    print("\n=== 11.6.1 resample OHLC (minute -> day) ===")
    minute_idx = pd.date_range("2025-01-02 09:30", periods=8, freq="5min")
    px = pd.Series(
        [10.0, 10.2, 10.1, 10.3, 10.25, 10.4, 10.35, 10.5],
        index=minute_idx,
    )
    ohlc = px.resample("1D").ohlc()
    print(ohlc)

    print("\n=== 11.6.4 Grouper + groupby ===")
    panel = pd.DataFrame(
        {
            "ts": np.tile(minute_idx[:4], 2),
            "code": ["A"] * 4 + ["B"] * 4,
            "vol": np.arange(8, dtype=float) + 1,
        }
    )
    panel = panel.set_index("ts")
    g = panel.groupby([pd.Grouper(freq="10min"), "code"])["vol"].sum()
    print(g)

    print("\n=== 11.7 rolling / ewm ===")
    print("rolling mean(3):\n", close.rolling(3, min_periods=2).mean().tail(3))
    print("ewm span=3:\n", close.ewm(span=3, adjust=False).mean().tail(3))

    print("\nDone. Deep dive: Python-Time-Series-Forecast/code/time_series_quant/")


if __name__ == "__main__":
    main()
