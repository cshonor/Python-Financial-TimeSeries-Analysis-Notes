# 多子图 add_axes 添加区域：自由定位子图位置与大小

## fig.add_axes([left, bottom, width, height])

left bottom 左下角，width height 宽高，范围 0-1 表示相对 Figure 比例。

```python
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # 主图
ax2 = fig.add_axes([0.6, 0.6, 0.3, 0.3])  # 右上插入图
```

适合任意位置和大小，subplot 适合规则网格。
