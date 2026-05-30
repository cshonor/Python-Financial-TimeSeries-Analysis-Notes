"""
第 5 章配套：pandas 入门（Series / DataFrame / loc / 对齐 / 描述统计）

运行：
  python Python-Data-Analysis/code/chapter05_pandas_intro_demo.py
"""

from __future__ import annotations


def main() -> None:
    import numpy as np
    import pandas as pd

    print("=== 5.1.1 Series ===")
    s = pd.Series([10.1, 10.3, 10.2], index=["2025-01-01", "2025-01-02", "2025-01-03"])
    print(s)
    s2 = pd.Series({"a": 1, "b": 2}, index=["b", "a", "c"])
    print("reindex order + NaN:\n", s2)

    print("\n=== 5.1.2 DataFrame & column view ===")
    df = pd.DataFrame(
        {
            "open": [10.0, 10.2],
            "close": [10.1, 10.4],
            "volume": [1000, 1200],
        },
        index=pd.to_datetime(["2025-01-01", "2025-01-02"]),
    )
    print(df)
    col = df["close"]
    col.iloc[0] = 999
    print("after col.iloc[0]=999, df:\n", df)

    df2 = df.copy()
    df2.loc[df2.index[0], "close"] = 10.1
    print("copy isolated ok")

    print("\n=== 5.2.3 loc (inclusive end) vs iloc ===")
    df3 = pd.DataFrame({"x": range(5)}, index=list("abcde"))
    print("loc b:c inclusive:", df3.loc["b":"c"])
    print("iloc 1:3 exclusive stop:", df3.iloc[1:3])

    print("\n=== 5.2.4 alignment ===")
    a = pd.Series([1, 2, 3], index=["x", "y", "z"])
    b = pd.Series([10, 20], index=["y", "z"])
    print("a + b (union index):\n", a.add(b))

    print("\n=== 5.2.1 reindex ffill ===")
    idx = pd.date_range("2025-01-01", periods=5, freq="D")
    s3 = pd.Series([1.0, np.nan, 3.0], index=idx[[0, 2, 4]])
    print(s3.reindex(idx, method="ffill"))

    print("\n=== 5.3 describe / corr / value_counts ===")
    df4 = pd.DataFrame({"ret": [0.01, -0.02, 0.03], "vol": [0.1, 0.2, 0.15]})
    print(df4.describe())
    print("corr:\n", df4.corr())

    labels = pd.Series(["buy", "hold", "buy", "sell"])
    print("value_counts:\n", labels.value_counts())

    print("\nDone. More: Python-Financial-BigData-Analysis/code/pandas/00_core_objects/")


if __name__ == "__main__":
    main()
