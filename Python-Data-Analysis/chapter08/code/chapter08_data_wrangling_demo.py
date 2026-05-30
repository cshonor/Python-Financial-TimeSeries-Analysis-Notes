"""
第 8 章配套：数据规整（MultiIndex / merge / concat / reshape）

运行：
  python Python-Data-Analysis/code/chapter08_data_wrangling_demo.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    import pandas as pd

    print("=== 8.1 MultiIndex / set_index ===")
    long = pd.DataFrame(
        {
            "date": pd.to_datetime(["2025-01-02", "2025-01-02", "2025-01-03"]),
            "code": ["000001", "000002", "000001"],
            "close": [10.0, 20.0, 10.2],
        }
    )
    panel = long.set_index(["date", "code"]).sort_index()
    print("panel:\n", panel)
    print("slice one code:\n", panel.loc[(slice(None), "000001"), :])
    by_code = panel.groupby(level="code")["close"].mean()
    print("mean by code:\n", by_code)

    print("\n=== 8.2.1 merge ===")
    price = long[["date", "code", "close"]]
    factor = pd.DataFrame(
        {
            "date": pd.to_datetime(["2025-01-02", "2025-01-02", "2025-01-03"]),
            "code": ["000001", "000002", "000001"],
            "pe": [8.5, 12.0, 8.6],
        }
    )
    merged = pd.merge(price, factor, on=["date", "code"], how="left")
    print(merged)

    print("\n=== 8.2.3 concat(keys) ===")
    a = price[price["code"] == "000001"].drop(columns="code")
    b = price[price["code"] == "000002"].drop(columns="code")
    stacked = pd.concat([a, b], keys=["000001", "000002"], names=["code", "row"])
    print(stacked)

    print("\n=== 8.2.4 combine_first ===")
    primary = pd.Series([10.0, np.nan, 10.3], index=["2025-01-01", "2025-01-02", "2025-01-03"])
    backup = pd.Series([np.nan, 10.1, np.nan], index=["2025-01-01", "2025-01-02", "2025-01-03"])
    print(primary.combine_first(backup))

    print("\n=== 8.3.2 pivot / 8.3.3 melt ===")
    wide = merged.pivot(index="date", columns="code", values="close")
    print("wide close:\n", wide)
    melted = wide.reset_index().melt(id_vars="date", var_name="code", value_name="close")
    print("melted back:\n", melted.sort_values(["date", "code"]))

    print("\n=== 8.3.1 stack / unstack ===")
    st = wide.stack()
    print("stacked head:\n", st.head())
    print("unstack round-trip equals wide:\n", st.unstack().equals(wide))

    print("\nDone. See also: Python-Financial-BigData-Analysis/.../03_merge_and_concat.md")


if __name__ == "__main__":
    main()
