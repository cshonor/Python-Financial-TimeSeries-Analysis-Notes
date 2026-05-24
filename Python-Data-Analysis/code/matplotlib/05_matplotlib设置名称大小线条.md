# Matplotlib 设置名称、大小、线条

## 轴标签

```python
plt.xlabel("X 轴标签", fontsize=12)
plt.ylabel("Y 轴标签", fontsize=12)
```

## 标题大小

```python
plt.title("图表标题", fontsize=16)
```

## 线条样式

`plt.plot()` 第三个参数可控制线条颜色、线型、标记：

```python
# 颜色：'r'红 'g'绿 'b'蓝 'k'黑
# 线型：'-'实线 '--'虚线 ':'点线 '-.'点划线
# 标记：'o'圆点 's'方块 '*'星形

plt.plot(x, y, 'r--')           # 红色虚线
plt.plot(x, y, 'g-o', ms=5)     # 绿色实线+圆点，点大小 5
plt.plot(x, y, color='blue', linestyle='-', linewidth=2)
```

## 常用参数

| 参数 | 说明 |
|------|------|
| `color` / `c` | 颜色 |
| `linestyle` / `ls` | 线型 |
| `linewidth` / `lw` | 线宽 |
| `marker` | 标记样式 |
| `markersize` / `ms` | 标记大小 |
| `label` | 图例标签（配合 legend 使用） |

## 示例

```python
plt.plot(x, y1, 'b-', lw=2, label='系列1')
plt.plot(x, y2, 'r--', lw=1.5, label='系列2')
plt.legend()
```
