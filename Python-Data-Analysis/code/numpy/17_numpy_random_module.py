"""
NumPy 17 - 随机数模块（随机模拟 / 复现 / 采样）

目标：
  - 固定随机种子，保证结果可复现
  - 常用分布：uniform / normal
  - 抽样与打乱：choice / permutation
  - 蒙特卡洛：多路径模拟的雏形

提示：
  - 新代码建议使用 np.random.default_rng()（Generator API）
"""

from __future__ import annotations

import numpy as np


def demo_reproducibility() -> None:
    print("\n=== 1) 固定随机种子（复现）===")
    rng1 = np.random.default_rng(42)
    rng2 = np.random.default_rng(42)
    print("rng1.normal(0,1,5):", rng1.normal(0, 1, 5))
    print("rng2.normal(0,1,5):", rng2.normal(0, 1, 5))


def demo_distributions() -> None:
    print("\n=== 2) 常用分布采样 ===")
    rng = np.random.default_rng(7)

    u = rng.uniform(low=0.0, high=1.0, size=5)
    n = rng.normal(loc=0.0, scale=1.0, size=5)
    print("uniform:", u)
    print("normal :", n)


def demo_shuffle_and_sample() -> None:
    print("\n=== 3) 打乱与抽样（不放回/放回/带权重）===")
    rng = np.random.default_rng(123)

    idx = np.arange(10)
    print("idx:", idx)
    print("permutation:", rng.permutation(idx))

    # 不放回抽样（抽 3 个不同元素）
    sample_wo = rng.choice(idx, size=3, replace=False)
    print("choice replace=False:", sample_wo)

    # 放回抽样（可能重复）
    sample_w = rng.choice(idx, size=10, replace=True)
    print("choice replace=True :", sample_w)

    # 带权重抽样（例如按概率选股/分层）
    p = np.array([0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.15, 0.15, 0.1, 0.1])
    p = p / p.sum()
    weighted = rng.choice(idx, size=5, replace=False, p=p)
    print("choice weighted:", weighted)


def demo_monte_carlo_price_paths() -> None:
    print("\n=== 4) 蒙特卡洛雏形：用正态收益模拟价格路径 ===")
    rng = np.random.default_rng(2025)

    n_days = 252
    n_paths = 3

    mu = 0.0005
    sigma = 0.01

    # (paths, days) 的日收益率
    rets = rng.normal(loc=mu, scale=sigma, size=(n_paths, n_days))
    prices = 100.0 * np.cumprod(1.0 + rets, axis=1)

    print("prices shape:", prices.shape)
    print("last prices:", prices[:, -1])
    print("path0 first5:", prices[0, :5])


def main() -> None:
    demo_reproducibility()
    demo_distributions()
    demo_shuffle_and_sample()
    demo_monte_carlo_price_paths()


if __name__ == "__main__":
    main()

