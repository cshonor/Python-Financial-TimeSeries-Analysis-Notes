import pandas as pd


def main() -> None:
    s1 = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"], name="s1")
    s2 = pd.Series([10.0, 30.0], index=["a", "c"], name="s2")
    print("s1:")
    print(s1)
    print("\ns2:")
    print(s2)

    print("\nAligned add (s1 + s2):")
    s3 = s1 + s2
    print(s3)

    print("\nisna:")
    print(s3.isna())

    print("\nfillna(0):")
    print(s3.fillna(0))

    # 时间序列常用：向前填充
    s_ts = pd.Series([1.0, None, None, 2.0, None], index=pd.date_range("2025-01-01", periods=5))
    print("\nTime series with missing:")
    print(s_ts)
    print("\nffill:")
    print(s_ts.ffill())


if __name__ == "__main__":
    main()

