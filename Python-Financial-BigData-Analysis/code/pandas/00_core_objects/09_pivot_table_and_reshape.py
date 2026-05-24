import pandas as pd


def main() -> None:
    df_long = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02"]
            ),
            "code": ["000001", "000002", "000001", "000002"],
            "close": [10.0, 20.0, 10.5, 19.8],
        }
    )
    print("long:")
    print(df_long)

    wide = df_long.pivot(index="date", columns="code", values="close")
    print("\npivot -> wide:")
    print(wide)

    # 宽 -> 长：stack
    back_to_long = wide.stack().reset_index(name="close")
    print("\nwide -> long (stack):")
    print(back_to_long)

    # 多级索引 unstack 示例
    mi = df_long.set_index(["date", "code"])
    print("\nset MultiIndex:")
    print(mi)
    print("\nunstack by code:")
    print(mi.unstack("code"))


if __name__ == "__main__":
    main()

