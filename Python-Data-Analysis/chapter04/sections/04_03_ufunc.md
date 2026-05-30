# 4.3 ufunc（通用函数）

> 所属：[第 4 章](../chapter04_numpy_basics_arrays_vectorization.md) · 《利用 Python 进行数据分析》  
> 配套专题：[`../../code/numpy/11_numpy_math_arithmetic_functions.md`](../../code/numpy/11_numpy_math_arithmetic_functions.md)、[`08_broadcasting_mechanism.md`](../../code/numpy/08_broadcasting_mechanism.md)

---

## 一句话定义

**ufunc = 对 ndarray 逐元素运算的向量化函数**（底层 C 循环，比 Python `for` 快几十倍）。

| 特点 | 说明 |
|------|------|
| **元素级** | 每个元素独立计算 |
| **向量化** | 不写显式循环 |
| **广播** | 不同形状可自动对齐（见广播专题） |
| **分类** | **一元**（1 输入）/ **二元**（2 输入） |

运算符 `+` `-` `*` `/` `**` 以及 `arr > 0` 等比较，底层也对应 ufunc。

---

## 一、一元 ufunc（1 个输入数组）

| 类别 | 常见函数 |
|------|----------|
| 数学 | `np.sqrt`、`np.exp`、`np.log`、`np.log10`、`np.log2` |
| 符号 | `np.abs`、`np.sign`、`np.negative`（`-arr`） |
| 取整 | `np.ceil`、`np.floor`、`np.rint`、`np.round` |
| 三角 | `np.sin`、`np.cos`、`np.tan` |

```python
import numpy as np

arr = np.array([1, 4, 9, 16], dtype=float)
np.sqrt(arr)    # [1., 2., 3., 4.]
np.exp(arr)     # e^x 逐元素
np.log(arr)     # ln(x)
np.abs(np.array([-1, 0, 2]))
```

---

## 二、二元 ufunc（2 个输入数组）

| 类别 | 函数 | 运算符等价 |
|------|------|------------|
| 算术 | `np.add`、`subtract`、`multiply`、`divide` | `+` `-` `*` `/` |
| 幂 | `np.power` | `**` |
| 比较 | `np.maximum`、`minimum` | 逐元素较大/较小 |
| 关系 | `np.greater`、`less`、`equal` | `>` `<` `==` |
| 逻辑 | `np.logical_and`、`logical_or` | 对布尔数组 |

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.add(a, b)           # [5, 7, 9]
np.maximum(a, b)       # [4, 5, 6]
np.greater(a, b)       # [False, False, False]
```

**与矩阵乘区分**：`@` / `np.dot` 是 **线性代数**（4.6），不是逐元素 ufunc。

---

## 三、关键参数：`out=`（必背）

| | 默认 `out=None` | 指定 `out=已有数组` |
|---|-----------------|---------------------|
| 行为 | **新建**结果数组 | 结果 **写入已有缓冲区** |
| 优点 | 简单 | **省内存、减少分配、略提速** |
| 要求 | — | `out` **形状必须可广播匹配** |

```python
arr = np.arange(5, dtype=float)
out_arr = np.empty(5)

np.sqrt(arr, out=out_arr)    # 结果直接进 out_arr，无新数组
print(out_arr)

# 二元同样可用
np.add(a, b, out=out_arr[:3])  # out 形状须匹配
```

**注意**：`out` 若与原输入 **内存重叠**，部分 ufunc 行为需查阅文档；稳妥做法用 **`np.empty_like(arr)`** 预分配。

---

## 四、一页式速查（含易错点）

### 必背清单

- **ufunc = 逐元素 + 向量化 + 快**
- **一元**：sqrt、exp、log、abs、sign、ceil、floor
- **二元**：add、multiply、maximum、minimum、greater
- **`out=`**：写入已有数组，省内存

### 易错点

| 易错 | 正确 |
|------|------|
| 用 for 算 `sqrt(x)` | **`np.sqrt(arr)`** |
| 混淆 `*` 与 `@` | `*` 逐元素；`@` 矩阵乘 |
| `out` 形状不对 | 预分配 **`np.empty_like(arr)`** |
| `log(0)` | 得 `-inf`；先处理无效值 |

### 记忆口诀

> **ufunc 逐元素快，一元 sqrt exp log；  
> 二元 add maximum，out 写入省内存。**

---

## 五、演示：量化常用 ufunc

```python
import numpy as np

close = np.array([10.0, 10.5, 10.2, 11.0])
rets = np.divide(np.diff(close), close[:-1])   # 收益率

# 对数收益
log_rets = np.log(np.divide(close[1:], close[:-1]))

# 截断极端值（二元 maximum/minimum）
winsor = np.minimum(np.maximum(rets, -0.05), 0.05)
```

---

## 六、【量化专属改造】

1. **对数价格 / 收益**：`np.log(close)`、`np.diff(np.log(close))` 比循环快且稳。
2. **信号比较**：`np.maximum(signal, 0)` 截断负仓位；配合 [`4.4 np.where`](./04_04_面向数组编程.md) 做三元逻辑。
3. **大数组热路径**：预分配 `out = np.empty_like(arr)`，循环内复用 `ufunc(..., out=out)` 减 GC。
4. **NaN 传播**：`sqrt(-1)` → `nan`；回归前必须 `np.isfinite` 或 pandas `dropna`。

---

## 七、与 4.4 / 全书衔接

- **`np.where`**：基于布尔 ufunc 的 **条件选择**（4.4.1）
- **聚合** `sum/mean`：多元素归约，与 ufunc 同属向量化体系（4.4.2）
- **pandas**：`Series` 算术底层调用 NumPy ufunc + 索引对齐

---

## 八、自检

- [ ] 能解释 ufunc 与 Python for 循环的性能差异  
- [ ] 能各举 3 个一元、二元 ufunc  
- [ ] 会用 `out=` 预分配写入  
- [ ] 能区分 `*`（逐元素）与 `@`（矩阵乘）  

---

## 九、留白

（记录：你策略里哪些计算已从 loop 改成 ufunc）

---

[← 返回第 4 章](../chapter04_numpy_basics_arrays_vectorization.md) · [4.3～4.6 合并速查](./chapter04_核心速查_4_3_4_6.md)
