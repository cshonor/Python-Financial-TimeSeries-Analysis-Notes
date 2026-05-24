"""
第 2 章配套代码：pandas 数据结构 + 量化中的存储约定

运行：
  python Pandas/00_core_objects/chapter02_pandas_data_structures_quant.py
"""

from __future__ import annotations


def main() -> None:
    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(0)

    print("=== 1) 单标的 OHLCV：DatetimeIndex 升序 ===")
    idx = pd.date_range("2025-01-01", periods=5, freq="B")
    ohlcv = pd.DataFrame(
        {
            "open": [10.0, 10.1, 10.05, 10.2, 10.15],
            "high": [10.2, 10.25, 10.15, 10.3, 10.2],
            "low": [9.95, 10.0, 10.0, 10.1, 10.05],
            "close": [10.1, 10.05, 10.12, 10.18, 10.1],
            "volume": [1000, 1100, 900, 1300, 1050],
        },
        index=idx,
    )
    ohlcv.index.name = "date"
    print(ohlcv)
    print("index type:", type(ohlcv.index))
    print("index is monotonic increasing:", ohlcv.index.is_monotonic_increasing)

    print("\n=== 2) 多标的长表：(date, code) 唯一 ===")
    rows = []
    for d in pd.date_range("2025-01-01", periods=3, freq="B"):
        for code in ("000001", "000002"):
            rows.append(
                {
                    "date": d,
                    "code": code,
                    "close": float(10.0 + rng.normal(0, 0.05)),
                }
            )
    long_df = pd.DataFrame(rows)
    print(long_df)
    dup = long_df.duplicated(["date", "code"]).sum()
    print("duplicated (date, code) count:", dup)

    long_mi = long_df.set_index(["date", "code"]).sort_index()
    print("\nMultiIndex long table:")
    print(long_mi)

    print("\n=== 3) 宽表：pivot 后列 = code ===")
    wide = long_df.pivot(index="date", columns="code", values="close")
    print(wide)

    print("\n=== 4) 与 statsmodels 的输入形态（示意，不强制安装）===")
    xs = pd.DataFrame(
        {
            "ret": [0.01, -0.005, 0.002],
            "momentum": [0.2, -0.1, 0.05],
            "industry_A": [1, 0, 1],
        }
    )
    print("截面回归用表（示意）:")
    print(xs)
    print("dtypes:\n", xs.dtypes)


if __name__ == "__main__":
    main()
