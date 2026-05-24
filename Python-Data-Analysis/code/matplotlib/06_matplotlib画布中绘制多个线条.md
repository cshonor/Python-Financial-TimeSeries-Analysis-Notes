# Matplotlib 画布中绘制多个线条

在同一坐标系中绘制多条曲线，只需多次调用 `plt.plot()`。

## 基本用法

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.legend()
plt.show()
```

## 要点

- 每次 `plot()` 会添加一条新曲线，共用当前坐标轴
- 使用 `label` 参数便于图例区分
- 搭配 `plt.legend()` 显示图例

## 区分线条

通过颜色、线型、标记区分：

```python
plt.plot(x, y1, 'b-', lw=2, label='曲线1')
plt.plot(x, y2, 'r--', label='曲线2')
plt.plot(x, y3, 'g:', label='曲线3')
```

## 子图（多个独立坐标）

```python
fig, axes = plt.subplots(2, 1)  # 2 行 1 列
axes[0].plot(x, y1)
axes[1].plot(x, y2)
plt.show()
```
