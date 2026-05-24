"""
第 4 章配套：NumPy ndarray 与向量化（对应原书 4.1～4.7 精华）

运行：
  python Python-Data-Analysis/code/chapter04_numpy_basics_demo.py

更多专题见同目录 numpy/ 下 01～20 脚本。
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np


def demo_create_dtype_ops() -> None:
    print("\n=== 4.1 创建 / dtype / 元素级运算 ===")
    arr = np.array([1.0, 2.0, 3.0])
    print("array:", arr, "dtype:", arr.dtype)

    z = np.zeros((2, 3))
    print("zeros shape:", z.shape)

    as_int = arr.astype(np.int64)
    print("astype int:", as_int, "is new object:", as_int is not arr)

    print("arr * 2:", arr * 2)
    print("arr > 1.5:", arr > 1.5)


def demo_slice_view_vs_boolean_copy() -> None:
    print("\n=== 4.1.4～4.1.6 切片(视图) vs 布尔(副本) ===")
    a = np.arange(10)
    sl = a[2:5]
    sl[0] = 999
    print("after slice assign, a:", a)

    b = np.arange(10)
    mask = b % 2 == 0
    evens = b[mask]
    evens[0] = -1
    print("boolean copy unchanged b[0]:", b[0])


def demo_where_axis_ufunc() -> None:
    print("\n=== 4.3 ufunc / 4.4 where & axis ===")
    x = np.array([-2.0, -0.5, 0.3, 1.2])
    clipped = np.where(x < 0, 0, x)
    print("where clip negatives:", clipped)

    mat = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    print("col mean axis=0:", mat.mean(axis=0))
    print("row sum axis=1:", mat.sum(axis=1))
    print("cumsum 1d:", np.cumsum([0.01, -0.02, 0.03]))


def demo_random_walk() -> None:
    print("\n=== 4.7 随机漫步（向量化）===")
    rng = np.random.default_rng(42)
    n = 20
    steps = rng.integers(0, 2, size=n)  # 0/1
    steps = np.where(steps == 0, -1, 1)
    walk = np.cumsum(steps)
    print("steps:", steps)
    print("walk :", walk)
    print("max position:", walk.max(), "at index:", walk.argmax())


def demo_linalg_and_io() -> None:
    print("\n=== 4.5 save/load & 4.6 @ 矩阵乘 ===")
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    B = np.array([[1.0, 0.0], [0.0, 1.0]])
    print("A @ B:\n", A @ B)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "arr.npy"
        np.save(path, A)
        loaded = np.load(path)
        print("loaded shape:", loaded.shape)


def main() -> None:
    demo_create_dtype_ops()
    demo_slice_view_vs_boolean_copy()
    demo_where_axis_ufunc()
    demo_random_walk()
    demo_linalg_and_io()
    print("\nDone. Deep dive: code/numpy/03, 08, 09, 17, 18 ...")


if __name__ == "__main__":
    main()
