# ndarray 的 delete、扁平处理、变形和翻转

## np.delete

删除指定位置的元素或子数组，返回新数组。

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 删除索引 2 的元素
np.delete(arr, 2)           # [1 2 4 5]

# 删除多个索引
np.delete(arr, [0, 2, 4])   # [2 4]

# 二维：指定 axis
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.delete(a, 1, axis=0)     # 删除第 1 行
np.delete(a, [0, 2], axis=1) # 删除第 0、2 列
```

## 扁平处理 (Flatten)

将多维数组展平为一维。

| 方法 | 说明 | 是否复制 |
|------|------|----------|
| `arr.flatten()` | 返回一维副本 | 是 |
| `arr.ravel()` | 返回一维视图（可能共享内存） | 通常否 |

```python
a = np.array([[1, 2], [3, 4]])
print(a.flatten())   # [1 2 3 4]
print(a.ravel())     # [1 2 3 4]
```

## 变形 (Reshape)

改变数组形状，元素总数不变。

```python
arr = np.arange(12)

# reshape 返回新数组（或视图）
arr.reshape(3, 4)        # (3, 4)
arr.reshape(2, 2, 3)     # (2, 2, 3)
arr.reshape(-1, 4)       # -1 表示自动推断，此处为 (3, 4)
```

| 方法 | 说明 |
|------|------|
| `arr.reshape(shape)` | 指定新形状 |
| `arr.reshape(-1)` | 展平为一维 |
| `np.reshape(arr, shape)` | 函数形式 |

## 翻转 (Transpose / Flip)

| 方法 | 说明 |
|------|------|
| `arr.T` | 转置（行列互换） |
| `np.transpose(arr)` | 转置 |
| `np.flip(arr, axis)` | 沿指定轴翻转 |
| `np.fliplr(arr)` | 左右翻转（水平） |
| `np.flipud(arr)` | 上下翻转（垂直） |

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)              # 转置
print(np.flip(a, 0))    # 上下翻转
print(np.flip(a, 1))    # 左右翻转
print(np.fliplr(a))     # 左右翻转
print(np.flipud(a))     # 上下翻转
```

## 要点

- `delete` 返回新数组
- `flatten` 总返回副本，`ravel` 通常返回视图
- `reshape` 不改变元素总数，`-1` 可自动推算该维度
- `T` / `transpose` 为转置，`flip` 系列为镜像翻转
