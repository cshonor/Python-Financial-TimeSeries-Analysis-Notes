# Matplotlib 显示线条数据值 text

在图表上标注数据点的数值，常用 `plt.text()` 或 `plt.annotate()`。

## plt.text()

在指定坐标处添加文本。

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.plot(x, y, 'o-')
for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')
plt.show()
```

## 语法

```python
plt.text(x, y, s, **kwargs)
```

| 参数 | 说明 |
|------|------|
| `x`, `y` | 文本位置坐标 |
| `s` | 文本内容 |
| `ha` | 水平对齐：'left'、'center'、'right' |
| `va` | 垂直对齐：'top'、'center'、'bottom' |
| `fontsize` | 字体大小 |

## plt.annotate()

带箭头的注释，适合突出某个点：

```python
plt.annotate('最大值', xy=(4, 17), xytext=(3, 18),
             arrowprops=dict(arrowstyle='->'))
```

## 常见用法

```python
# 在数据点上方显示数值
plt.text(2, 15, '15', ha='center', fontsize=10)
```
