import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "date": ["2025-01-03", "2025-01-01", "2025-01-02"],
            "factor": ["1.2", "0.8", None],
            "close": ["10.3", "10.0", "10.1"],
        }
    )
    print("raw df:")
    print(df)

    # 类型处理：字符串 -> datetime/float
    df["date"] = pd.to_datetime(df["date"])
    df["close"] = df["close"].astype(float)
    df["factor"] = pd.to_numeric(df["factor"], errors="coerce")  # None / 非法 -> NaN

    # 设为索引并排序（时间序列强烈建议）
    df = df.set_index("date").sort_index()
    print("\nconverted + index sorted:")
    print(df)

    # 按列排序（因子选股）
    print("\nsort by factor desc (NaN last):")
    print(df.sort_values("factor", ascending=False))


if __name__ == "__main__":
    main()

