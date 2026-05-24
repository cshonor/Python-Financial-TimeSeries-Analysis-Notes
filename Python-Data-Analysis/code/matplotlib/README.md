# Matplotlib 示例

## 1.0 数据可视化是什么

数据可视化就是将数据转换成图或表等，以**更直观的方式**展现和呈现数据。通过“可视化”的方式，我们看不懂的数据通过图形化手段**有效地表达**，**准确高效、简洁全面地传递**某种信息，甚至帮助我们发现**规律和特征**，挖掘**数据背后的价值**。

## 1.1 什么是 Matplotlib

- Matplotlib 是 Python 的**数据可视化**库，最广泛使用的绘图工具之一
- 开源、支持多种输出格式（PNG、PDF、SVG、交互式等）
- 提供类似 **MATLAB** 的 `pyplot` 接口，上手简单
- 可与 **NumPy**、**Pandas** 无缝配合，直接对数组/DataFrame 绘图
- 支持科研图表、业务报表、交互式仪表盘等多种场景

Matplotlib 的核心是**图形对象（Figure、Axes）**，通过 `plt.plot`、`plt.bar`、`plt.scatter` 等函数快速生成折线图、柱状图、散点图等，是 Python 数据分析可视化的基础。

## 1.2 下载和安装

**什么是 pip？** pip 是 Python 的包管理工具，用于安装、卸载第三方库。Python 3.4+ 通常自带 pip。

- **pip 安装**：`pip install matplotlib`
- **Anaconda**：Conda 环境中通常已自带，或 `conda install matplotlib`
- **验证安装**：
  ```python
  import matplotlib
  matplotlib.__version__  # 如 '3.10.8'
  ```

## 主要功能

- **pyplot**：类似 MATLAB 的绘图接口
- 折线图、柱状图、散点图
- 饼图、直方图
- 子图布局（subplot）
- 图例、标题、坐标轴标注
- 保存图片（PNG、PDF、SVG 等）

## 学习资源

- [Matplotlib 官方文档](https://matplotlib.org/stable/)
- [Matplotlib 示例画廊](https://matplotlib.org/stable/gallery/index.html)
