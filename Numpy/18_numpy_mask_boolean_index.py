"""
NumPy 18 - 布尔掩码 / 高级索引（量化信号生成必备）

目标：
  - 用布尔掩码做筛选与批量修改（替代 for 循环）
  - 多条件组合筛选（& / | / ~）
  - np.where 向量化条件分支
  - 典型量化用法：过滤异常收益、生成买卖信号
"""

from __future__ import annotations

import numpy as np


def demo_basic_mask_filter() -> None:
    print("\n=== 1) 掩码筛选 ===")
    x = np.array([1, 2, 3, 4, 5, 6])
    mask = x % 2 == 0
    print("x:", x)
    print("mask (even):", mask)
    print("x[mask]:", x[mask])


def demo_multi_condition() -> None:
    print("\n=== 2) 多条件组合（& / | / ~）===")
    ret = np.array([0.02, -0.03, 0.15, -0.25, 0.01, np.nan])

    # 注意：有 NaN 时，比较会返回 False；需要先处理 NaN 或额外条件
    mask_valid = ~np.isnan(ret)
    mask_in_range = (ret >= -0.1) & (ret <= 0.1)
    mask_keep = mask_valid & mask_in_range

    print("ret:", ret)
    print("mask_keep:", mask_keep)
    print("filtered:", ret[mask_keep])


def demo_where_signal() -> None:
    print("\n=== 3) np.where：向量化条件判断生成信号 ===")
    rng = np.random.default_rng(42)
    close = 100 * np.cumprod(1 + rng.normal(0.0003, 0.01, size=30))

    # 简单均线（用卷积得到与 close 同长度的近似均线，边缘会偏差，足够演示）
    window = 5
    ma = np.convolve(close, np.ones(window) / window, mode="same")

    # 信号：close > ma -> 1 else 0
    signal = np.where(close > ma, 1, 0).astype(int)

    # 量化关键：执行信号通常要滞后 1 天（避免未来函数）
    position = np.r_[0, signal[:-1]]

    ret = np.r_[np.nan, np.diff(close) / close[:-1]]
    strategy_ret = ret * position

    print("close[:8]:", np.round(close[:8], 3))
    print("ma[:8]   :", np.round(ma[:8], 3))
    print("signal[:8]:", signal[:8])
    print("pos[:8]   :", position[:8])
    print("nanmean(strategy_ret):", np.nanmean(strategy_ret))


def demo_masked_assignment() -> None:
    print("\n=== 4) 掩码批量修改：clip/修正异常 ===")
    ret = np.array([0.02, -0.03, 0.15, -0.25, 0.01])
    ret_clean = ret.copy()

    # 把绝对值超过 10% 的收益截断到 ±10%（演示风控式清洗）
    ret_clean[ret_clean > 0.1] = 0.1
    ret_clean[ret_clean < -0.1] = -0.1

    print("ret      :", ret)
    print("ret_clean:", ret_clean)


def main() -> None:
    demo_basic_mask_filter()
    demo_multi_condition()
    demo_where_signal()
    demo_masked_assignment()


if __name__ == "__main__":
    main()

