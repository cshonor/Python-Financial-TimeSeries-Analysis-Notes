"""
第 4 章配套：用 NumPy 进行数值计算（《金融数据分析及其 Python 应用》）

运行：
  python Financial-Data-Python-Application/chapter04/code/chapter04_numpy_demo.py
"""

from __future__ import annotations

import array
import time
from copy import deepcopy

import numpy as np


def demo_list_reference_trap() -> None:
    print("\n=== 4.1.1 Python 列表引用陷阱 ===")
    v = [0.5, 0.75, 1.0, 1.5, 2.0]
    m_shallow = [v, v, v]
    v[0] = 999
    print("浅拷贝 m[0][0]:", m_shallow[0][0], "m[1][0]:", m_shallow[1][0])

    v2 = [0.5, 0.75, 1.0, 1.5, 2.0]
    m_deep = 3 * [deepcopy(v2),]
    v2[0] = 999
    print("深拷贝 m[0][0]:", m_deep[0][0], "m[1][0]:", m_deep[1][0])


def demo_python_array_module() -> None:
    print("\n=== 4.1.2 Python array 模块 ===")
    a = array.array("f", [0.5, 0.75, 1.0, 1.5, 2.0])
    print("array:", a, "typecode:", a.typecode)
    try:
        a.append("string")  # type: ignore[arg-type]
    except TypeError as exc:
        print("类型约束:", exc)


def demo_ndarray_basics() -> None:
    print("\n=== 4.2.1 ndarray 基础 ===")
    a = np.array([0, 0.5, 1.0, 1.5, 2.0])
    print("array:", a)
    print("2 * a:", 2 * a)
    print("a ** 2:", a ** 2)
    print("exp:", np.exp(a))
    print("sum / std / cumsum:", a.sum(), a.std(), a.cumsum())


def demo_multidim_and_axis() -> None:
    print("\n=== 4.2.2 多维数组与 axis ===")
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print("zeros:\n", np.zeros((2, 3)))
    print("eye:\n", np.eye(3))
    print("linspace:", np.linspace(0, 1, 5))
    print("col sum axis=0:", b.sum(axis=0))
    print("row sum axis=1:", b.sum(axis=1))


def demo_metadata_and_reshape() -> None:
    print("\n=== 4.2.3～4.2.4 元信息与变形 ===")
    g = np.arange(12).reshape(3, 4)
    print("ndim/shape/size/dtype:", g.ndim, g.shape, g.size, g.dtype)
    stacked = np.vstack([g, g])
    print("vstack shape:", stacked.shape)
    print("ravel is view:", np.shares_memory(g, g.ravel()))
    print("flatten is copy:", not np.shares_memory(g, g.flatten()))


def demo_boolean_and_where() -> None:
    print("\n=== 4.2.5 布尔数组与 np.where ===")
    h = np.arange(10)
    print("h > 8:", h > 8)
    labels = np.where(h % 2 == 0, "even", "odd")
    print("labels:", labels)


def demo_speed_comparison(n: int = 500) -> None:
    """默认 500×500 以便快速演示；原书用 5000×5000。"""
    print(f"\n=== 4.2.6 速度对比 ({n}×{n}) ===")
    mat = np.random.default_rng(0).random((n, n))

    t0 = time.perf_counter()
    total = 0.0
    for row in mat:
        for val in row:
            total += val
    py_sec = time.perf_counter() - t0

    t0 = time.perf_counter()
    np_total = mat.sum()
    np_sec = time.perf_counter() - t0

    print(f"Python loop sum: {total:.4f} in {py_sec:.3f}s")
    print(f"NumPy sum:       {np_total:.4f} in {np_sec:.3f}s")
    if np_sec > 0:
        print(f"Speedup: ~{py_sec / np_sec:.0f}x")


def demo_structured_array() -> None:
    print("\n=== 4.3 结构数组 ===")
    dt = np.dtype([("Name", "U10"), ("Age", "i4"), ("Height", "f4")])
    s = np.array([("Alice", 25, 1.68), ("Bob", 30, 1.75)], dtype=dt)
    print("Names:", s["Name"])


def demo_broadcasting() -> None:
    print("\n=== 4.4.1 广播 ===")
    a = np.ones((4, 3))
    b = np.array([1, 2, 3])
    print("broadcast add shape:", (a + b).shape)
    try:
        bad = np.array([1, 2, 3, 4])
        _ = a + bad
    except ValueError as exc:
        print("广播失败:", exc)


def demo_memory_layout() -> None:
    print("\n=== 4.4.2 内存布局 ===")
    c_arr = np.array([[1, 2, 3], [4, 5, 6]], order="C")
    f_arr = np.array([[1, 2, 3], [4, 5, 6]], order="F")
    print("C contiguous:", c_arr.flags["C_CONTIGUOUS"])
    print("F contiguous:", f_arr.flags["F_CONTIGUOUS"])


def main() -> None:
    demo_list_reference_trap()
    demo_python_array_module()
    demo_ndarray_basics()
    demo_multidim_and_axis()
    demo_metadata_and_reshape()
    demo_boolean_and_where()
    demo_speed_comparison()
    demo_structured_array()
    demo_broadcasting()
    demo_memory_layout()
    print("\nDone.")


if __name__ == "__main__":
    main()
