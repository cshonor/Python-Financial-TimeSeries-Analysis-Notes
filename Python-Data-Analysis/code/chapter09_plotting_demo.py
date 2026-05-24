"""
第 9 章配套：绘图和可视化（matplotlib / pandas.plot / seaborn 可选）

运行（无 GUI 环境使用 Agg 后端并保存示例图到 /tmp 或当前目录）：
  python Python-Data-Analysis/code/chapter09_plotting_demo.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np
import pandas as pd


def _save(fig: plt.Figure, name: str, out_dir: Path) -> Path:
    path = out_dir / name
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return path


def demo_matplotlib(out_dir: Path) -> None:
    print("=== 9.1 matplotlib: subplots / plot / legend / savefig ===")
    rng = np.random.default_rng(0)
    dates = pd.date_range("2025-01-01", periods=60, freq="B")
    close = 100 * np.cumprod(1 + rng.normal(0.001, 0.02, len(dates)))

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(dates, close, color="steelblue", label="close")
    axes[0].set(title="Price", ylabel="close")
    axes[0].legend()

    ret = pd.Series(close, index=dates).pct_change().dropna()
    axes[1].hist(ret, bins=20, color="gray", alpha=0.8)
    axes[1].set(title="Daily returns", xlabel="return")

    fig.subplots_adjust(hspace=0.35)
    p = _save(fig, "ch09_matplotlib_price_ret.png", out_dir)
    print("saved:", p)


def demo_pandas_plot(out_dir: Path) -> None:
    print("\n=== 9.2.1 pandas line / 9.2.2 bar / 9.2.3 hist ===")
    df = pd.DataFrame(
        {
            "date": pd.date_range("2025-01-01", periods=5, freq="B"),
            "A": [1.0, 1.2, 1.1, 1.3, 1.25],
            "B": [2.0, 2.1, 2.3, 2.2, 2.4],
        }
    ).set_index("date")

    fig, ax = plt.subplots(figsize=(6, 4))
    df.plot(ax=ax, marker="o")
    ax.set(title="Multi-series line (pandas)")
    p1 = _save(fig, "ch09_pandas_line.png", out_dir)
    print("saved:", p1)

    counts = pd.Series({"bank": 40, "tech": 35, "energy": 25})
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    counts.plot.bar(ax=ax2, color="teal")
    ax2.set(title="Industry counts")
    p2 = _save(fig2, "ch09_pandas_bar.png", out_dir)
    print("saved:", p2)


def demo_seaborn(out_dir: Path) -> None:
    try:
        import seaborn as sns
    except ImportError:
        print("\n=== 9.2 seaborn: skipped (pip install seaborn) ===")
        return

    print("\n=== 9.2.4 regplot / 9.2.3 histplot (seaborn) ===")
    rng = np.random.default_rng(1)
    n = 80
    factor = rng.normal(0, 1, n)
    ret = 0.02 * factor + rng.normal(0, 0.03, n)
    df = pd.DataFrame({"factor": factor, "ret": ret})

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.regplot(data=df, x="factor", y="ret", ax=ax, scatter_kws={"s": 15, "alpha": 0.7})
    ax.set(title="Factor vs return")
    p = _save(fig, "ch09_seaborn_regplot.png", out_dir)
    print("saved:", p)


def main() -> None:
    out_dir = Path(tempfile.gettempdir()) / "pda_ch09_plots"
    out_dir.mkdir(parents=True, exist_ok=True)
    print("Output directory:", out_dir)

    demo_matplotlib(out_dir)
    demo_pandas_plot(out_dir)
    demo_seaborn(out_dir)

    print("\nDone. Deep dive: Python-Data-Analysis/code/matplotlib/")


if __name__ == "__main__":
    main()
