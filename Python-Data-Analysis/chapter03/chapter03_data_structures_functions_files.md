# 第 3 章 Python 的数据结构、函数和文件

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 3 章。  
> 本章介绍贯穿全书的 **Python 内置能力**：元组/列表/字典/集合、函数与作用域、异常处理、文件读写。NumPy、pandas 等扩展库的设计初衷是与这些内置工具 **协同使用**。  
> **前置**：建议先读 [第 2 章](../chapter02/chapter02_python_syntax_ipython_jupyter.md)（引用语义、控制流、Jupyter）。

---

## 章节总览

掌握内置数据结构、函数组织方式与本地文件交互，是高效 Python 编程与复杂数据分析的基础。

**模块统计**：3 个一级小节 + 约 7 个二级/子模块，共 **10 个核心模块**。

| 一级 | 二级 / 子模块 |
|------|----------------|
| 3.1 数据结构和序列 | 3.1.1 元组与切片；3.1.3 字典；3.1.4 集合；推导式 |
| 3.2 函数 | 命名空间与作用域；3.2.2 多返回值；生成器与 itertools；3.2.6 异常处理 |
| 3.3 文件和操作系统 | 打开模式、`with` 上下文管理器 |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [03_01_数据结构和序列](./sections/03_01_数据结构和序列.md) | 数据结构和序列 |
| [03_01_01_元组与列表切片](./sections/03_01_01_元组与列表切片.md) | 01 元组与列表切片 |
| [03_01_03_字典](./sections/03_01_03_字典.md) | 03 字典 |
| [03_01_04_集合](./sections/03_01_04_集合.md) | 04 集合 |
| [03_02_函数](./sections/03_02_函数.md) | 函数 |
| [03_02_06_错误和异常处理](./sections/03_02_06_错误和异常处理.md) | 06 错误和异常处理 |
| [03_03_文件和操作系统](./sections/03_03_文件和操作系统.md) | 文件和操作系统 |

## 二、关键语法速查表

| 主题 | 语法示例 |
|------|----------|
| 切片 | `seq[1:5]`, `seq[::2]`, `seq[::-1]` |
| 字典 | `d[k]`, `d.get(k, default)`, `d.pop(k)` |
| defaultdict | `from collections import defaultdict` |
| 集合 | `s1 \| s2`, `s1 & s2`, `set(lst)` |
| 列表推导 | `[f(x) for x in xs if cond]` |
| 生成器 | `(f(x) for x in xs)` |
| 多返回 | `return a, b` → `x, y = f()` |
| 异常 | `try: ... except ValueError: ... finally: ...` |
| 文件 | `with open(p, "r", encoding="utf-8") as f: f.read()` |

---

## 三、通用基础示例

完整演示见：[`./code/chapter03_data_structures_functions_files.py`](./code/chapter03_data_structures_functions_files.py)

```python
# 切片
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4], nums[::-1])

# 字典 + defaultdict
from collections import defaultdict
counts = defaultdict(int)
for ch in "aabbc":
    counts[ch] += 1

# 安全读文件
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
```

---

## 四、【量化专属改造】金融实战衔接

1. **切片思维 → 时间窗口**：`prices[-20:]` 与后面 `rolling(20)` 的「最近 20 个点」是同一直觉（注意 pandas 用标签切片时含终点规则不同）。
2. **字典 / defaultdict**：按 `code` 累加成交额、按 `industry` 分桶计数；读 CSV 前用 `dict` 做列名映射（中文列 → 英文列）。
3. **集合**：`universe = set(codes)` 做股票池；`set(df["code"])` 与昨日持仓求交/差，实现调仓 diff。
4. **推导式**：`[c for c in codes if c.startswith("60")]` 快速筛沪市；大规模数据优先 NumPy/pandas 向量化，少写深层嵌套推导。
5. **异常 + 文件**：读第三方 CSV/日志时，对 `float()`、`parse_dates` 用 `try/except` 或 `errors="coerce"`，避免一行脏数据拖垮整段回测脚本。
6. **生成器**：逐行读超大 tick 文件时用生成器，避免 `read()` 一次性载入内存。

---

## 五、与 statsmodels 建模的衔接要点

- 读入建模数据前，常用 **dict / 列表推导** 构造公式项名列表（如 `["const", "momentum", "size"]`），再传给 `sm.OLS`。
- **`with open`** 写出回归摘要、残差序列到文本报告，与 notebook 结果归档。
- 稳健的数据管道：`try/except` 清洗 → `DataFrame` → `statsmodels`；本章的「不崩溃」习惯直接决定批量回测能否跑完。

---

## 本章自检清单

- [ ] 能解释切片含头不含尾，并与 `iloc` 位置切片对照  
- [ ] 能说明 dict 键为何必须可散列  
- [ ] 会用集合做去重与集合运算  
- [ ] 能写单层列表推导，并知道何时该改用循环  
- [ ] 会用 `try/except/finally` 处理脏数据转换  
- [ ] 会用 `with open(..., encoding="utf-8")` 读写文本文件  

---

## 后续扩展留白

### 3.1.1 元组与切片

（留白）

### 3.1.3 字典

（留白）

### 3.1.4 集合

（留白）

### 推导式

（留白）

### 3.2 函数

（留白）

### 3.3 文件

（留白）
