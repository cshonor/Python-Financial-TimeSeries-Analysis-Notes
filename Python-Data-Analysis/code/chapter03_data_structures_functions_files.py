"""
第 3 章配套：数据结构、函数、文件（对应原书 3.1～3.3）

运行：
  python Python-Data-Analysis/code/chapter03_data_structures_functions_files.py
"""

from __future__ import annotations

import itertools
import tempfile
from collections import defaultdict
from pathlib import Path


def demo_slice_and_tuple() -> None:
    print("\n=== 3.1.1 元组与切片 ===")
    tup = ("open", "high", "low", "close")
    print("tuple:", tup)
    print("slice [1:3]:", tup[1:3])
    print("reverse [:: -1]:", tup[::-1])

    prices = [10.0, 10.2, 9.8, 10.5, 10.1]
    print("last 3 prices:", prices[-3:])
    print("every 2nd:", prices[::2])


def demo_dict_set_comprehension() -> None:
    print("\n=== 3.1.3 字典 / 3.1.4 集合 / 推导式 ===")
    industry_map = {"000001": "bank", "000002": "tech", "000003": "bank"}
    by_industry: dict[str, list[str]] = defaultdict(list)
    for code, ind in industry_map.items():
        by_industry[ind].append(code)
    print("group by industry:", dict(by_industry))

    codes = ["000001", "000002", "000001", "000003"]
    unique_codes = set(codes)
    print("unique codes:", unique_codes)

    lengths = {s: len(s) for s in ["ma5", "ma20", "rsi"]}
    print("dict comprehension:", lengths)

    sh_codes = [c for c in unique_codes if c.startswith("000")]
    print("filter codes:", sh_codes)


def demo_functions_and_generators() -> None:
    print("\n=== 3.2 函数 / 生成器 / itertools ===")

    def ohlc_stats(o: float, h: float, l: float, c: float) -> tuple[float, float]:
        """返回多个值（实际是元组拆包）。"""
        return h - l, (c - o) / o if o else 0.0

    rng, ret = ohlc_stats(10, 10.5, 9.8, 10.2)
    print("range, return:", rng, ret)

    squares = (x * x for x in range(5))
    print("generator sum:", sum(squares))

    data = [("A", 1), ("A", 2), ("B", 3)]
    for key, group in itertools.groupby(data, key=lambda x: x[0]):
        print("groupby consecutive", key, list(group))


def safe_float(value: str) -> float | None:
    """3.2.6 异常处理：脏字符串转 float。"""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def demo_exceptions() -> None:
    print("\n=== 3.2.6 异常处理 ===")
    raw = ["10.5", "bad", "9.8", None]
    cleaned = [safe_float(str(x)) if x is not None else None for x in raw]
    cleaned = [x for x in cleaned if x is not None]
    print("cleaned floats:", cleaned)


def demo_files() -> None:
    print("\n=== 3.3 文件读写（with + utf-8）===")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sample.csv"
        lines = ["date,close\n", "2025-01-01,10.1\n", "2025-01-02,10.3\n"]
        with path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

        with path.open("r", encoding="utf-8") as f:
            content = f.read()
        print("read back:\n", content.strip())

        # 逐行生成器，适合大文件
        with path.open("r", encoding="utf-8") as f:
            header = next(f).strip()
            rows = (line.strip() for line in f)
            print("header:", header)
            print("rows:", list(rows))


def main() -> None:
    demo_slice_and_tuple()
    demo_dict_set_comprehension()
    demo_functions_and_generators()
    demo_exceptions()
    demo_files()
    print("\nDone. Next: code/numpy/03_ndarray_indexing_slicing.py")


if __name__ == "__main__":
    main()
