"""
第 7 章配套：数据清洗和准备（缺失 / 去重 / 分箱 / 异常 / 分类）

运行：
  python Python-Data-Analysis/code/chapter07_data_cleaning_demo.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    import pandas as pd

    print("=== 7.1 缺失值 ===")
    df = pd.DataFrame(
        {
            "date": pd.date_range("2025-01-01", periods=4),
            "close": [10.0, np.nan, 10.3, 10.4],
            "volume": [1000, 1100, np.nan, 900],
        }
    )
    print("isna:\n", df.isna())
    print("dropna row any:\n", df.dropna())
    print("ffill close:\n", df.assign(close=df["close"].ffill()))

    print("\n=== 7.2.1 去重 ===")
    dup = pd.DataFrame(
        {
            "date": ["2025-01-01", "2025-01-01", "2025-01-02"],
            "code": ["000001", "000001", "000002"],
            "close": [10.0, 10.0, 20.0],
        }
    )
    print(dup.drop_duplicates(subset=["date", "code"], keep="first"))

    print("\n=== 7.2.2 map / 7.2.3 replace ===")
    exch = pd.Series(["000001.SZ", "600000.SH"])
    print(exch.map(lambda x: x.split(".")[0]))
    bad = pd.Series([10.0, -999.0, 10.2])
    print(bad.replace(-999, np.nan))

    print("\n=== 7.2.5 cut / qcut ===")
    factor = pd.Series(np.random.default_rng(0).normal(0, 1, 20))
    print("qcut labels:\n", pd.qcut(factor, 5, labels=False).value_counts().sort_index())

    print("\n=== 7.2.6 异常收益 clip ===")
    ret = pd.Series([0.01, -0.02, 0.25, -0.15, 0.03])
    print("clipped:\n", ret.clip(-0.1, 0.1))

    print("\n=== 7.4.3 str / 7.5 get_dummies ===")
    codes = pd.Series(["000001.XSHE", "000002.XSHE", None])
    print(codes.str.replace(".XSHE", "", regex=False))

    ind = pd.DataFrame({"code": ["A", "B", "A"], "industry": ["bank", "tech", "bank"]})
    dummies = pd.get_dummies(ind, columns=["industry"], drop_first=True)
    print("dummies:\n", dummies)

    print("\n=== 7.3 category ===")
    s = pd.Series(["bank", "tech", "bank", "tech"] * 50).astype("category")
    print(s.dtype, "categories:", s.cat.categories)

    print("\nDone. See also: Python-Financial-BigData-Analysis/.../02_data_cleaning_preprocessing/")


if __name__ == "__main__":
    main()
