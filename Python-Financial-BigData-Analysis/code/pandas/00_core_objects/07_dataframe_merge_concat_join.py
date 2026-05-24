import pandas as pd


def main() -> None:
    # concat：纵向拼接（同字段）
    df_a = pd.DataFrame(
        {"close": [10.0, 10.2], "volume": [1000, 1100]},
        index=pd.to_datetime(["2025-01-01", "2025-01-02"]),
    )
    df_b = pd.DataFrame(
        {"close": [10.3, 10.1], "volume": [1200, 900]},
        index=pd.to_datetime(["2025-01-03", "2025-01-06"]),
    )
    df_concat = pd.concat([df_a, df_b], axis=0)
    print("concat axis=0:")
    print(df_concat)

    # concat：横向拼接（不同字段，按 index 对齐）
    factor = pd.DataFrame(
        {"momentum": [0.1, 0.2, -0.1]},
        index=pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]),
    )
    df_wide = pd.concat([df_concat, factor], axis=1)
    print("\nconcat axis=1 (aligned):")
    print(df_wide)

    # merge：按键（列）连接
    price = pd.DataFrame(
        {"date": ["2025-01-01", "2025-01-02"], "close": [10.0, 10.2]}
    )
    industry = pd.DataFrame(
        {"date": ["2025-01-01", "2025-01-02"], "industry": ["bank", "bank"]}
    )
    merged = pd.merge(price, industry, on="date", how="inner")
    print("\nmerge on date:")
    print(merged)

    # join：按 index 连接
    df1 = price.assign(date=pd.to_datetime(price["date"])).set_index("date")[["close"]]
    df2 = industry.assign(date=pd.to_datetime(industry["date"])).set_index("date")[["industry"]]
    joined = df1.join(df2, how="left")
    print("\njoin on index:")
    print(joined)


if __name__ == "__main__":
    main()

