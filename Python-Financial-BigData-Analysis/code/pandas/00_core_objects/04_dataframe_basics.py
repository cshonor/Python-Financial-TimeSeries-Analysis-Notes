import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "open": [10.0, 10.5, 10.2],
            "high": [10.8, 10.9, 10.6],
            "low": [9.9, 10.2, 10.0],
            "close": [10.6, 10.3, 10.4],
            "volume": [1000, 1200, 900],
        },
        index=pd.to_datetime(["2025-01-02", "2025-01-03", "2025-01-06"]),
    )
    print("df:")
    print(df)

    print("\nindex:", df.index)
    print("columns:", df.columns)

    print("\nselect one column df['close'] -> Series:")
    print(df["close"])

    print("\nselect multi columns df[['open','close']]:")
    print(df[["open", "close"]])

    df["ret"] = df["close"].pct_change()
    print("\nadd return column:")
    print(df)

    print("\nloc by date:")
    print(df.loc[pd.Timestamp("2025-01-03")])

    print("\niloc first row:")
    print(df.iloc[0])


if __name__ == "__main__":
    main()

