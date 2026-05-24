# 子图 subplots：更现代的多子图创建与管理方式

## plt.subplots(nrows, ncols)

一次创建 Figure 和 Axes 数组。

```python
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 1].plot([1, 2, 3], [1, 2, 3])
axes[1, 0].plot([1, 2, 3], [2, 3, 4])
axes[1, 1].plot([1, 2, 3], [3, 2, 1])
plt.tight_layout()
plt.show()
```

常用参数 figsize sharex sharey
