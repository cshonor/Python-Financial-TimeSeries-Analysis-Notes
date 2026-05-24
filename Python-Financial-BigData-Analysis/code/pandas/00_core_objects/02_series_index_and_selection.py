import pandas as pd


def main() -> None:
    s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"], name="x")
    print("s:")
    print(s)

    print("\nloc single:")
    print(s.loc["b"])

    print("\nloc list:")
    print(s.loc[["a", "d"]])

    print("\nloc slice (includes end):")
    print(s.loc["b":"d"])

    print("\niloc single:")
    print(s.iloc[1])

    print("\niloc list:")
    print(s.iloc[[0, 2]])

    print("\niloc slice (excludes end):")
    print(s.iloc[1:3])

    print("\nboolean filter:")
    print(s[s >= 30])

    # 条件来自同 index 的 Series（会自动对齐）
    cond = pd.Series([True, False, True, False], index=["a", "b", "c", "d"])
    print("\nboolean filter with aligned cond:")
    print(s[cond])


if __name__ == "__main__":
    main()

