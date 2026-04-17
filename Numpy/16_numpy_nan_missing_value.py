"""
NumPy 16 - NaN / 缺失值处理（量化必用）

目标：
  - 理解 np.nan 的核心特性
  - 掌握缺失值检测/填充/删除
  - 熟练使用 nan-safe 统计函数（nanmean/nanstd/...）
"""

from __future__ import annotations

import numpy as np


def demo_nan_properties() -> None:
    print("\n=== 1) np.nan 的特性 ===")
    x = np.nan
    print("np.nan == np.nan ?", x == x)
    print("np.isnan(np.nan) ?", np.isnan(x))

    arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
    print("arr:", arr)
    print("mask_isnan:", np.isnan(arr))


def demo_nan_safe_stats() -> None:
    print("\n=== 2) 忽略 NaN 的统计：nanmean/nanstd/nanmax/nanmin ===")
    r = np.array([0.01, np.nan, -0.02, 0.005, np.nan])

    # 普通 mean 会返回 nan
    print("mean:", r.mean())
    print("nanmean:", np.nanmean(r))
    print("nanstd:", np.nanstd(r))
    print("nanmax:", np.nanmax(r))
    print("nanmin:", np.nanmin(r))


def demo_fill_and_drop() -> None:
    print("\n=== 3) 检测/填充/删除 ===")
    a = np.array([100.0, np.nan, 102.0, np.nan, 105.0])

    # 3.1 删除 NaN：只保留有效值
    valid = a[~np.isnan(a)]
    print("valid:", valid)

    # 3.2 填充 NaN：nan_to_num
    filled_zero = np.nan_to_num(a, nan=0.0)
    print("filled nan->0:", filled_zero)

    # 3.3 用指定值填充（例如缺失收益当 0）
    filled_custom = np.nan_to_num(a, nan=100.0)
    print("filled nan->100:", filled_custom)


def demo_quant_style_return_with_missing() -> None:
    print("\n=== 4) 量化小例子：缺失价格导致收益缺失，如何稳健统计 ===")

    close = np.array([10.0, 10.2, np.nan, 10.1, 10.4, np.nan, 10.3])

    # 用 diff / close[:-1] 计算收益（中间会产生 NaN）
    ret = np.diff(close) / close[:-1]
    print("close:", close)
    print("ret:", ret)

    # 用 nan-safe 统计（避免整段变 nan）
    print("nanmean(ret):", np.nanmean(ret))
    print("nanstd(ret):", np.nanstd(ret))

    # 简单风控：把极端收益截断（前提：先把 NaN 排除或保持）
    ret_clip = np.clip(ret, -0.1, 0.1)
    print("ret clipped:", ret_clip)
    print("nanmean(ret clipped):", np.nanmean(ret_clip))


def main() -> None:
    demo_nan_properties()
    demo_nan_safe_stats()
    demo_fill_and_drop()
    demo_quant_style_return_with_missing()


if __name__ == "__main__":
    main()

