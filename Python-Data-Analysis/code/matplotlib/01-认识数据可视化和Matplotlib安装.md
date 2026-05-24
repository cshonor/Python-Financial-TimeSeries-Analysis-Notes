# 认识数据可视化和 Matplotlib 安装

## 数据可视化

数据可视化将数据以图表形式呈现，便于发现规律、对比趋势、辅助决策。常见图表类型：

- **折线图**：趋势、时间序列
- **柱状图**：分类对比
- **散点图**：相关性、分布
- **饼图**：占比
- **直方图**：分布、频数

## Matplotlib 简介

Matplotlib 是 Python 最常用的绘图库，底层可控、功能丰富，可与 NumPy、Pandas 配合使用。

## 安装

```bash
pip install matplotlib
```

或使用 Conda：

```bash
conda install matplotlib
```

## 验证安装

```python
import matplotlib
print(matplotlib.__version__)
```

## 基本使用

```python
from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```
