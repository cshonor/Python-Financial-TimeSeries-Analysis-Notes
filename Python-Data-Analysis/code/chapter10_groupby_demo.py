"""
第 10 章配套：数据聚合与分组（groupby / agg / transform / pivot_table）

运行：
  python Python-Data-Analysis/code/chapter10_groupby_demo.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    print("=== 10.1 groupby / 10.2 agg ===")
    df = pd.DataFrame(
        {
            "date": ["2025-01-02"] * 4 + ["2025-01-03"] * 4,
            "code": ["A", "B", "C", "D"] * 2,
            "industry": ["bank", "tech", "bank", "tech"] * 2,
            "ret": [0.01, 0.02, -0.01, 0.03, 0.005, -0.02, 0.01, 0.015],
            "pe": [8.0, 25.0, 9.0, 30.0, 8.1, 24.0, 9.2, 29.0],
        }
    )
    by_date = df.groupby("date")["ret"].mean()
    print("mean ret by date:\n", by_date)

    multi = df.groupby(["date", "industry"], as_index=False).agg(
        ret_mean=("ret", "mean"),
        pe_max=("pe", "max"),
    )
    print("agg as_index=False:\n", multi)

    print("\n=== 10.1.1 iterate groups ===")
    pieces = {name: grp for name, grp in df.groupby("industry")}
    print("keys:", list(pieces.keys()), "bank rows:", len(pieces["bank"]))

    print("\n=== 10.3.2 qcut + groupby / 10.4 transform ===")
    rng = np.random.default_rng(0)
    panel = pd.DataFrame(
        {
            "date": np.repeat(pd.date_range("2025-01-01", periods=3, freq="B"), 20),
            "factor": rng.normal(0, 1, 60),
            "ret": rng.normal(0.001, 0.02, 60),
        }
    )
    panel["bucket"] = pd.qcut(panel["factor"], 5, labels=False, duplicates="drop")
    bucket_ret = panel.groupby("bucket", observed=True)["ret"].mean()
    print("mean ret by factor bucket:\n", bucket_ret)

    panel["ret_demean"] = panel["ret"] - panel.groupby("date")["ret"].transform("mean")
    print("demean sample:\n", panel[["date", "ret", "ret_demean"]].head(3))

    print("\n=== 10.3 apply (group fillna) ===")
    miss = panel.copy()
    miss.loc[miss.sample(5, random_state=0).index, "ret"] = np.nan
    filled = miss.groupby("date", group_keys=False).apply(
        lambda g: g.assign(ret=g["ret"].fillna(g["ret"].mean()))
    )
    print("filled NA count:", filled["ret"].isna().sum())

    print("\n=== 10.5 pivot_table / crosstab ===")
    pt = df.pivot_table(
        index="date",
        columns="industry",
        values="pe",
        aggfunc="mean",
        margins=True,
    )
    print("pivot_table pe:\n", pt)
    ct = pd.crosstab(df["date"], df["industry"])
    print("crosstab counts:\n", ct)

    print("\nDone. OLS-per-group: see 02_groupby_and_aggregation.md + statsmodels.")
    print("Deep dive: Python-Financial-BigData-Analysis/.../08_groupby_basics.md")


if __name__ == "__main__":
    main()
