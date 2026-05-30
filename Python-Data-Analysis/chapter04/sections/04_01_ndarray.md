# 4.1 ndarray（NumPy 多维数组对象）

> 所属：[第 4 章](../chapter04_numpy_basics_arrays_vectorization.md) · 《利用 Python 进行数据分析》  
> 配套脚本：[`../../code/numpy/01_create_ndarray.py`](../../code/numpy/01_create_ndarray.py)、[`02_numpy_data_types.py`](../../code/numpy/02_numpy_data_types.py)、[`03_ndarray_indexing_slicing.py`](../../code/numpy/03_ndarray_indexing_slicing.py)

---

## 核心一句话

**ndarray 是 NumPy 的基础：同类型、连续内存、支持向量化运算，速度远快于 Python list。**

---

## 一、书本原文核心知识点提炼

### 4.1.1 创建 ndarray

| 函数 | 作用 |
|------|------|
| `np.array(seq)` | 从列表/元组创建 |
| `np.zeros(shape)` | 全 0 |
| `np.ones(shape)` | 全 1 |
| `np.empty(shape)` | 未初始化（快，值随机） |
| `np.arange(start, stop, step)` | 类似 `range` |
| `np.linspace(start, stop, num)` | 等间隔 num 个点 |
| `np.eye(N)` | N×N 单位矩阵 |

```python
import numpy as np

arr = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
arr.shape    # (2, 3)
arr.ndim     # 2
arr.size     # 6
```

---

### 4.1.2 dtype（数据类型）

- 常见：`int8/16/32/64`、`float32/64`、`bool_`
- `arr.dtype` 查看类型
- **`arr.astype(new_type)` 一定返回新数组**（不原地改 dtype）
- 整型 → 浮点：安全；浮点 → 整型：**截断小数**（不四舍五入）

```python
arr = np.array([1, 2, 3], dtype=np.float64)
arr2 = arr.astype(np.int32)   # [1, 2, 3]
arr_f = np.array([1.9, 2.1])
arr_f.astype(np.int32)        # [1, 2] 截断
```

---

### 4.1.3 数组运算（向量化）

- **同形状**：元素级 `+` `-` `*` `/` `**`（无需写循环）
- **与标量**：广播到所有元素
- **不同形状**：广播规则（详见 [`08_broadcasting_mechanism.md`](../../code/numpy/08_broadcasting_mechanism.md) / 原书附录 A）

```python
data = np.array([[1., 2., 3.], [4., 5., 6.]])
data * 10          # 标量广播
data + data        # 同形状元素级
1 / data           # 倒数
data > 2           # 比较 → 布尔数组
```

---

### 4.1.4 切片（视图！）

- 一维：`arr[start:stop:step]`
- 二维：`arr[i, j]`、`arr[:2, 1:]`
- **切片是视图（view）**：改切片 → **改原数组**（共享内存）

```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[:2, 1:]          # 前 2 行，第 1 列之后
arr2d[:2, 1:] = 0      # ⚠️ 原 arr2d 也被改
```

---

### 4.1.5 布尔索引（副本）

- `arr[mask]`：mask 是同形状布尔数组
- 多条件：`&`（与）、`|`（或），**每个条件要加括号**
- **结果是副本**，改结果不改原数组

```python
arr = np.arange(20).reshape(4, 5)
mask = arr > 10
arr[mask]

arr[(arr > 5) & (arr < 15)]    # 注意括号，不能用 and/or
```

---

### 4.1.6 花式索引（副本）

- 用 **整数数组/列表** 选行、列或元素
- `arr[[0, 2, 1]]`：按指定行号重排
- `arr[[0, 2], [1, 0]]`：选 (0,1)、(2,0) 两个位置
- **结果是副本**

```python
arr2d = np.arange(9).reshape(3, 3)
arr2d[[0, 2, 1]]              # 行重排
arr2d[[0, 2], [1, 0]]         # → [arr2d[0,1], arr2d[2,0]]
```

---

### 4.1.7 转置与换轴（多为视图）

- `.T`：转置（二维常用）
- `.transpose(axes)`：自定义轴顺序
- `.swapaxes(a, b)`：交换两个轴
- **大多返回视图，不复制数据**

```python
arr2d.T
arr2d.transpose((1, 0))
arr3d.swapaxes(0, 2)
```

---

## 二、一页式速查清单（含易错点对比）

### 创建速查

| API | 用途 |
|-----|------|
| `np.array` | 从序列 |
| `zeros/ones/empty` | 按形状填充 |
| `arange/linspace` | 数列 |
| `eye` | 单位矩阵 |

### 视图 vs 副本（必背）

| 操作 | 结果 | 改结果是否改原数组 |
|------|------|-------------------|
| **切片** `arr[1:5]`、`arr[:2, 1:]` | **视图** | ✅ 会 |
| **整数索引** `arr[0]`（单元素） | 标量/特殊 | 视情况 |
| **布尔索引** `arr[mask]` | **副本** | ❌ 不会 |
| **花式索引** `arr[[0,2]]` | **副本** | ❌ 不会 |
| **`.T` / transpose** | **多为视图** | ✅ 常会 |
| **`.astype()`** | **新数组** | ❌ 不会 |
| **`.copy()`** | **显式副本** | ❌ 不会 |

### 布尔条件写法

```python
# ✅ 正确
(arr > a) & (arr < b)
(arr == 0) | (arr == 1)

# ❌ 错误
arr > a and arr < b      # 不能用 and
arr > a & arr < b        # 优先级错，必须括号
```

### 记忆口诀（超浓缩）

> **创建用 array/zeros/arange，dtype astype 新数组，  
> 运算元素级 + 广播，切片视图、布尔花式副本，  
> 转置 .T/transpose，视图为主少复制。**

---

## 三、演示

```python
import numpy as np

# 创建 + dtype
prices = np.array([10.0, 10.5, 9.8, 11.2])
rets = np.diff(prices) / prices[:-1]   # 向量化收益（长度 n-1）

# 视图陷阱
view = prices[1:3]
view[:] = 0          # prices 也被改 → 回测中间结果要 .copy()

# 布尔筛选 + 副本安全
mask = rets > 0
pos_rets = rets[mask]   # 副本，改 pos_rets 不影响 rets
```

完整可运行示例见 [`../../code/numpy/03_ndarray_indexing_slicing.py`](../../code/numpy/03_ndarray_indexing_slicing.py)。

---

## 四、【量化专属改造】

1. **行情数组**：`close = df["close"].to_numpy(dtype=np.float64)`，再 `np.diff` / 向量化信号。
2. **视图陷阱**：对切片赋持仓信号会污染原价格数组 → 需要隔离时用 **`arr.copy()`**。
3. **因子截面**：二维 `(n_stock, n_factor)`，`axis=0` 跨股票、`axis=1` 跨因子。
4. **布尔选股**：`mask = (pe > 0) & (pe < 30) & (volume > vol_ma)`，注意括号。
5. **float64 默认**：与 pandas / statsmodels 衔接时优先 `float64`，避免隐式精度问题。

---

## 五、与 statsmodels / pandas 的衔接

- 回归前：`X = df[["x1", "x2"]].to_numpy()`；**必须先 `dropna`**，NaN 进 ndarray 会污染 OLS。
- `df.values` 在旧版 pandas 常用；新版推荐 **`.to_numpy()`**（可控 dtype）。
- 理解 ndarray 视图 → 明白为何 `df.loc[mask, "col"] = x` 有时链式赋值警告（pandas 索引层）。

---

## 六、自检

- [ ] 能列举 5 种创建 ndarray 的 API  
- [ ] 能解释 `astype` 为何总返回新数组  
- [ ] 能区分切片（视图）与布尔/花式索引（副本）  
- [ ] 会用 `(a > x) & (b < y)` 写多条件 mask  
- [ ] 能背诵「视图 vs 副本」口诀  
- [ ] 知道何时必须 `.copy()`  

---

## 七、留白

（补充：你的回测里哪些数组曾踩视图坑、dtype 选择记录）

---

[← 返回第 4 章](../chapter04_numpy_basics_arrays_vectorization.md)
