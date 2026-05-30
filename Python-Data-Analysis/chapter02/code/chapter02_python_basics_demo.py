"""
第 2 章配套：Python 语法基础演示（对应原书 2.3）

运行：
  python Python-Data-Analysis/code/chapter02_python_basics_demo.py

IPython/Jupyter 魔法命令（%run、?）请在 notebook 或 ipython 中交互使用。
"""

from __future__ import annotations

from datetime import datetime, timedelta


def demo_reference_vs_copy() -> None:
    print("\n=== 2.3.1 引用 vs 复制 ===")
    a = [1, 2, 3]
    b = a
    b.append(4)
    print("a after b.append(4):", a, "  # 同一列表对象")

    c = a.copy()
    c.append(99)
    print("a after c.append(99):", a, "  # copy 后互不影响")


def demo_is_vs_eq() -> None:
    print("\n=== is vs == / None ===")
    x = None
    print("x is None:", x is None)
    print("[] == []:", [] == [])
    print("[] is []:", [] is [])


def demo_scalars_and_datetime() -> None:
    print("\n=== 2.3.2 标量与 datetime ===")
    print("7 / 2 =", 7 / 2)
    print("7 // 2 =", 7 // 2)

    d0 = datetime(2025, 1, 2)
    d1 = d0 + timedelta(days=3)
    print("strftime:", d0.strftime("%Y-%m-%d"))
    print("parsed:", datetime.strptime("2025-01-06", "%Y-%m-%d"))
    print("d0 + 3 days:", d1)


def demo_control_flow() -> None:
    print("\n=== 2.3.3 控制流 ===")
    rets = [0.01, -0.02, 0.03, -0.01]
    for i, r in enumerate(rets):
        if r > 0:
            print(f"day {i}: up {r:.2%}")
        elif r < 0:
            print(f"day {i}: down {r:.2%}")

    # 链式比较
    x = 5
    print("1 < x < 10:", 1 < x < 10)

    # range 不含终点
    print("range(3):", list(range(3)))


def demo_duck_typing() -> None:
    print("\n=== 鸭子类型：可迭代即可 for ===")
    for item in ("open", "high", "low"):
        print(item, end=" ")
    print()


def main() -> None:
    print("Chapter 2 demo — run in Jupyter for %run / ? / Tab completion")
    demo_reference_vs_copy()
    demo_is_vs_eq()
    demo_scalars_and_datetime()
    demo_control_flow()
    demo_duck_typing()
    print("\nNext: chapter03/ then code/numpy/")


if __name__ == "__main__":
    main()
