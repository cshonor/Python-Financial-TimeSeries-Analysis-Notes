# 多子图 subplot：按网格布局快速创建子图

## plt.subplot()

按行、列、索引创建子图。

## 语法

```python
plt.subplot(nrows, ncols, index)
# 或 plt.subplot(323) 表示 3 行 2 列第 3 个
```

## 示例

```python
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('子图1')

plt.subplot(2, 1, 2)
plt.plot([1, 2, 3], [1, 2, 3])
plt.title('子图2')

plt.tight_layout()
plt.show()
```

## plt.subplots()

```python
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 1].plot([1, 2, 3], [1, 2, 3])
plt.tight_layout()
plt.show()
```

## 常用参数

sharex sharey 共享轴，figsize 图形大小。
