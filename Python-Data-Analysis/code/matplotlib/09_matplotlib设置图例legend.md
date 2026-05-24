# Matplotlib 设置图例 legend

## plt.legend()

显示图例，用于区分多条曲线。需在 `plot()` 中指定 `label`。

## 基本用法

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9], label='y=x^2')
plt.plot([1, 2, 3], [1, 2, 3], label='y=x')
plt.legend()
plt.show()
```

## 常用参数

| 参数 | 说明 |
|------|------|
| `loc` | 位置：'upper right'、'upper left'、'center' 等 |
| `fontsize` | 字体大小 |
| `ncol` | 图例列数 |
| `frameon` | 是否显示边框，默认 True |

## 位置字符串

```python
plt.legend(loc='upper right')   # 右上
plt.legend(loc='best')          # 自动选最佳位置
plt.legend(loc='center')        # 中心
```

## 示例

```python
plt.legend(loc='upper left', fontsize=10)
plt.legend(loc='lower center', ncol=2)  # 两列显示
```
