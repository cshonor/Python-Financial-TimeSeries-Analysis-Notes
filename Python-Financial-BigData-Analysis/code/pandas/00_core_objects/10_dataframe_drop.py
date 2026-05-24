import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02"],
            "code": ["000001", "000001", "000001", "000002"],
            "close": [10.0, 10.0, None, 20.0],
            "volume": [1000, 1000, 900, 1200],
        }
    )
    print("raw df:")
    print(df)

    print("\ndrop duplicates by (date, code):")
    df_dedup = df.drop_duplicates(subset=["date", "code"], keep="first")
    print(df_dedup)

    print("\ndropna subset=['close']:")
    df_nonan = df_dedup.dropna(subset=["close"])
    print(df_nonan)

    print("\ndrop columns:")
    df_drop_col = df_nonan.drop(columns=["volume"])
    print(df_drop_col)

    # 删除行示例：删掉 code == '000002'
    print("\ndrop rows by condition:")
    to_drop_idx = df_nonan.index[df_nonan["code"] == "000002"]
    print(df_nonan.drop(index=to_drop_idx))


if __name__ == "__main__":
    main()

