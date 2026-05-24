# 绘制网格 grid：添加背景网格线辅助读数

## plt.grid()

在图表上添加网格线，便于读取数据值。

## 基本用法

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [10, 15, 13, 17, 20])
plt.grid()  # 显示网格
plt.show()
```

## 常用参数

| 参数 | 说明 |
|------|------|
| `visible` | True/False，是否显示 |
| `axis` | 'x'、'y' 或 'both'，显示哪条轴的网格 |
| `linestyle` | 线型，如 '--'、':' |
| `alpha` | 透明度，0–1 |
| `color` | 颜色 |

## 示例

```python
plt.grid(True)                    # 显示网格
plt.grid(axis='y')                # 仅 y 轴网格
plt.grid(linestyle='--', alpha=0.7)
plt.grid(True, color='gray', alpha=0.3)
```
