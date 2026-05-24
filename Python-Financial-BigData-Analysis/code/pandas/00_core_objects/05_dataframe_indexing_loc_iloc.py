import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "open": [10.0, 10.5, 10.2, 10.4, 10.6],
            "close": [10.6, 10.3, 10.4, 10.8, 10.5],
            "volume": [1000, 1200, 900, 1500, 1100],
        },
        index=pd.date_range("2025-01-01", periods=5, freq="D"),
    )
    print("df:")
    print(df)

    print("\nloc single day:")
    print(df.loc["2025-01-03"])

    print("\nloc date slice (includes end):")
    print(df.loc["2025-01-02":"2025-01-04", ["close", "volume"]])

    print("\niloc first 3 rows:")
    print(df.iloc[0:3])

    print("\niloc rows/cols:")
    print(df.iloc[0:3, [0, 1]])

    print("\nboolean filter close > open:")
    print(df[df["close"] > df["open"]])

    print("\nquery close > open:")
    print(df.query("close > open"))


if __name__ == "__main__":
    main()

