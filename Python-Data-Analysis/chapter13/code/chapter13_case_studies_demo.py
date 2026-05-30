"""
第 13 章配套：五个案例的核心技法（合成小样本，无需原书数据文件）

运行：
  python Python-Data-Analysis/code/chapter13_case_studies_demo.py
"""

from __future__ import annotations

from collections import Counter

import numpy as np
import pandas as pd


def case_bitly() -> None:
    print("=== 13.1 Bitly tz counts ===")
    records = [
        {"tz": "America/New_York"},
        {"tz": "America/New_York"},
        {"tz": None},
        {"tz": "Europe/London"},
        {"tz": ""},
    ]
    # 13.1.1 pure Python
    cnt = Counter(r.get("tz") or "Missing" for r in records)
    print("Counter top:", cnt.most_common(2))

    # 13.1.2 pandas
    df = pd.DataFrame(records)
    vc = df["tz"].replace("", np.nan).fillna("Missing").value_counts()
    print("value_counts:\n", vc.head())


def case_movielens() -> None:
    print("\n=== 13.2 MovieLens-style merge / std / explode ===")
    ratings = pd.DataFrame(
        {"user_id": [1, 1, 2], "movie_id": [10, 20, 10], "rating": [5, 2, 4]}
    )
    movies = pd.DataFrame(
        {
            "movie_id": [10, 20],
            "title": ["Film A", "Film B"],
            "genres": ["Action|Drama", "Comedy"],
        }
    )
    merged = pd.merge(ratings, movies, on="movie_id")
    dispute = merged.groupby("title")["rating"].std().sort_values(ascending=False)
    print("rating std by title:\n", dispute)

    exploded = merged.assign(genre=merged["genres"].str.split("|")).explode("genre")
    print("explode genre counts:\n", exploded["genre"].value_counts())


def case_babynames() -> None:
    print("\n=== 13.3 baby names concat / prop ===")
    chunks = []
    for year in (2018, 2019):
        chunks.append(
            pd.DataFrame(
                {
                    "name": ["Ava", "Emma", "Liam"],
                    "sex": ["F", "F", "M"],
                    "count": [100, 80, 90],
                    "year": year,
                }
            )
        )
    names = pd.concat(chunks, ignore_index=True)

    def add_prop(g: pd.DataFrame) -> pd.DataFrame:
        total = g["count"].sum()
        return g.assign(prop=g["count"] / total)

    with_prop = names.groupby(["year", "sex"], group_keys=False).apply(add_prop)
    print(with_prop.head())


def case_usda() -> None:
    print("\n=== 13.4 USDA-style flatten / idxmax ===")
    nutrients = pd.DataFrame(
        {
            "id": [1, 1, 2],
            "nutrient": ["Zinc", "Protein", "Zinc"],
            "value": [2.0, 10.0, 5.0],
        }
    )
    info = pd.DataFrame({"id": [1, 2], "description": ["Food A", "Food B"]})
    merged = pd.merge(info, nutrients, on="id")

    def top_row(g: pd.DataFrame) -> pd.Series:
        return g.loc[g["value"].idxmax()]

    tops = merged.groupby("nutrient", group_keys=False).apply(top_row, include_groups=False)
    print(tops[["description", "value"]])


def case_fec() -> None:
    print("\n=== 13.5 FEC map / cut / groupby ===")
    occ_map = {"CEO": "Executive", "C.E.O.": "Executive", "TEACHER": "Education"}
    fec = pd.DataFrame(
        {
            "occupation": ["CEO", "C.E.O.", "TEACHER", "CEO"],
            "cand_nm": ["A", "A", "B", "B"],
            "contb_receipt_amt": [2500, 100, 50, 20],
            "contbr_st": ["CA", "CA", "NY", "TX"],
        }
    )
    fec["occ_clean"] = fec["occupation"].map(occ_map.get)
    pt = pd.pivot_table(
        fec, index="occ_clean", columns="cand_nm", values="contb_receipt_amt", aggfunc="sum"
    )
    print("pivot by occupation:\n", pt.fillna(0))

    bins = [0, 100, 1000, np.inf]
    fec["bucket"] = pd.cut(fec["contb_receipt_amt"], bins)
    print("cut counts:\n", fec["bucket"].value_counts().sort_index())

    by_state = fec.groupby(["cand_nm", "contbr_st"])["contb_receipt_amt"].sum().unstack(fill_value=0)
    pct = by_state.div(by_state.sum(axis=1), axis=0)
    print("state share within candidate:\n", pct.round(2))


def main() -> None:
    case_bitly()
    case_movielens()
    case_babynames()
    case_usda()
    case_fec()
    print("\nDone. Demo uses synthetic samples; see script comments for book data URLs.")


if __name__ == "__main__":
    main()
