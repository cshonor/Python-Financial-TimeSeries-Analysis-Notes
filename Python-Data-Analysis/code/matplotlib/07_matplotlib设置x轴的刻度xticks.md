# Matplotlib 设置 x 轴的刻度 xticks

## plt.xticks()

自定义 x 轴刻度位置和标签。

## 基本用法

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.plot(x, y)
plt.xticks([1, 2, 3, 4, 5], ['一月', '二月', '三月', '四月', '五月'])
plt.show()
```

## 语法

```python
plt.xticks(ticks=None, labels=None, **kwargs)
```

| 参数 | 说明 |
|------|------|
| ticks | 刻度位置（列表） |
| labels | 刻度标签（列表，与 ticks 一一对应） |
| rotation | 标签旋转角度 |

## 常用示例

```python
# 仅设置刻度间隔
plt.xticks(np.arange(0, 11, 2))

# 设置刻度及中文标签
plt.xticks([0, 1, 2, 3], ['A', 'B', 'C', 'D'])

# 标签旋转 45 度
plt.xticks(rotation=45)
```

## y 轴

`plt.yticks()` 用法相同，用于设置 y 轴刻度。
