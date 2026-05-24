import numpy as np


def main() -> None:
    # 1) 列表创建：默认索引
    s1 = pd.Series([10, 20, 30])
    print("s1:")
    print(s1)

    # 2) 指定索引
    s2 = pd.Series([10, 20, 30], index=["a", "b", "c"], name="price")
    print("\ns2:")
    print(s2)
    print("s2.values:", s2.values)
    print("s2.index:", s2.index)
    print("s2.dtype:", s2.dtype)

    # 3) 字典创建：key 变索引
    s3 = pd.Series({"a": 1.0, "c": 3.0, "d": 4.0})
    print("\ns3:")
    print(s3)

    # 4) 索引访问：标签 vs 位置
    print("\nlabel access s2['b']:", s2["b"])
    print("position access s2.iloc[1]:", s2.iloc[1])
    print("label access s2.loc['b']:", s2.loc["b"])

    # 5) 对齐：按索引自动对齐（量化数据合并常见）
    aligned = s2 + s3
    print("\nAligned add (s2 + s3):")
    print(aligned)

    # 6) 与标量运算
    print("\ns2 * 2:")
    print(s2 * 2)

    # 7) 与 ndarray 运算：会丢失索引语义（不推荐在策略关键路径随便 values）
    arr = np.array([1, 2, 3])
    print("\ns2.values * arr:")
    print(s2.values * arr)


if __name__ == "__main__":
    import pandas as pd

    main()

