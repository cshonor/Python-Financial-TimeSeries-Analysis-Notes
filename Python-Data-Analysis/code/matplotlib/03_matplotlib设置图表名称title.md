# Matplotlib 设置图表名称 title

## plt.title()

为图表设置标题，可控制字体、大小、位置等。

## 基本用法

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.title("示例图表")
plt.show()
```

## 常用参数

| 参数 | 说明 |
|------|------|
| `label` | 标题文本 |
| `fontsize` | 字体大小，如 12、'large' |
| `fontdict` | 字体属性字典 |
| `loc` | 对齐方式：'left'、'center'、'right' |

## 示例

```python
plt.title("销售趋势", fontsize=16)
plt.title("月度数据", loc='left')
plt.title("标题", fontdict={'fontsize': 14, 'color': 'blue'})
```
