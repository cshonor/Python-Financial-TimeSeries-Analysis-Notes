import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02"]
            ),
            "code": ["000001", "000002", "000001", "000002"],
            "industry": ["bank", "tech", "bank", "tech"],
            "factor": [0.2, 1.1, 0.5, 0.7],
            "ret": [0.01, -0.02, 0.03, 0.01],
        }
    )
    print("df:")
    print(df)

    print("\nGroup mean return by industry:")
    print(df.groupby("industry")["ret"].mean())

    print("\nAggregate by date:")
    print(df.groupby("date").agg(ret_mean=("ret", "mean"), factor_mean=("factor", "mean")))

    # transform：行业内去均值（行业中性的一种简化思路）
    df["factor_industry_neutral"] = df["factor"] - df.groupby("industry")["factor"].transform(
        "mean"
    )
    print("\nAdd industry-neutral factor (transform):")
    print(df[["date", "code", "industry", "factor", "factor_industry_neutral"]])

    # 截面排名：每个交易日对 factor 排名（pct=True -> 0~1）
    df["factor_rank_pct"] = df.groupby("date")["factor"].rank(pct=True)
    print("\nCross-sectional rank by date:")
    print(df[["date", "code", "factor", "factor_rank_pct"]])


if __name__ == "__main__":
    main()

