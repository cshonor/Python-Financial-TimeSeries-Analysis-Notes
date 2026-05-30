# 第 2 章 Python 语法基础、IPython 和 Jupyter Notebook

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 2 章。  
> 本章为数据处理打 **语言与环境** 基础：不深入 OOP，而聚焦数据分析最常用的 **Python 语法机制** 与 **IPython / Jupyter** 交互环境。

---

## 章节总览

要用 pandas、NumPy 等库把混乱数据规整成表格，须先掌握内置类型与语法，并熟练使用 Jupyter 做探索式分析。

**小节统计**：4 个一级小节 + 7 个二级小节，共 **11 个小节**。

| 一级 | 二级 |
|------|------|
| 2.1 Python 解释器 | — |
| 2.2 IPython 基础 | 2.2.1～2.2.4 |
| 2.3 Python 语法基础 | 2.3.1～2.3.3 |
| 2.4 总结 | — |

**建议阅读顺序**：第 1 章（生态）→ **本章** → 第 3 章（结构/函数/文件）→ `code/numpy/`。

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [02_01_Python_解释器](./sections/02_01_Python_解释器.md) | Python 解释器 |
| [02_02_IPython_基础](./sections/02_02_IPython_基础.md) | IPython 基础 |
| [02_02_01_运行_IPython_命令行](./sections/02_02_01_运行_IPython_命令行.md) | 01 运行 IPython 命令行 |
| [02_02_02_运行_Jupyter_Notebook](./sections/02_02_02_运行_Jupyter_Notebook.md) | 02 运行 Jupyter Notebook |
| [02_02_03_Tab_补全](./sections/02_02_03_Tab_补全.md) | 03 Tab 补全 |
| [02_02_04_自省](./sections/02_02_04_自省.md) | 04 自省 |
| [02_03_Python_语法基础](./sections/02_03_Python_语法基础.md) | Python 语法基础 |
| [02_03_01_语法的语义](./sections/02_03_01_语法的语义.md) | 01 语法的语义 |
| [02_03_02_标量类型](./sections/02_03_02_标量类型.md) | 02 标量类型 |
| [02_03_03_控制流](./sections/02_03_03_控制流.md) | 03 控制流 |
| [02_04_总结](./sections/02_04_总结.md) | 总结 |

## 二、关键语法速查表

| 主题 | 要点 |
|------|------|
| 环境 | `ipython`、`jupyter lab`、`%run file.py` |
| 自省 | `pd.read_csv?`、`np.*?` |
| 引用 | `b = a` 共享对象；复制用 `list.copy()` / `df.copy()` |
| 身份 | `x is None`，`a is b` |
| 除法 | `/` vs `//` |
| 日期 | `from datetime import datetime, timedelta` |
| 循环 | `for x in xs:`、`for i in range(n):` |

---

## 三、通用基础示例

见 [`./code/chapter02_python_basics_demo.py`](./code/chapter02_python_basics_demo.py)

```python
# 引用 vs 复制
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] — 同一对象

# 日期
from datetime import datetime, timedelta
d0 = datetime(2025, 1, 1)
d1 = d0 + timedelta(days=5)

# 控制流
for i, x in enumerate([10, 20, 30]):
  if x > 15:
    print(i, x)
```

---

## 四、【量化专属改造】金融实战衔接

1. **Jupyter 是默认工作台**：因子探索、画图、回测片段都在 notebook 里迭代；本仓库 `.py` 脚本可用 `%run` 或在终端 `python xxx.py` 复现。
2. **引用陷阱**：`df2 = df` 后改 `df2` 会改 `df`；策略管道里对行情表务必 **`df = df.copy()`** 或 `.copy(deep=True)`。
3. **`datetime` → `pd.Timestamp`**：读 CSV 后 `pd.to_datetime(df["date"])`，统一时区与交易日历在 pandas 章完成。
4. **`is None` vs `== NaN`**：缺失行情用 `pd.isna()`；不要用 `== None` 判断 NaN。
5. **Tab / `?`**：在 notebook 里对 `DataFrame.groupby`、`resample` 做自省，比翻书更快。

---

## 五、与 statsmodels 建模的衔接要点

- 在 Jupyter 中分 cell 跑：**清洗 → 描述统计 → OLS/ARIMA**，中间对象保持在同一内核，便于检查 `df.shape`、`df.dtypes`。
- 理解 **引用语义** 可避免「预处理误改全样本」导致回归系数不可复现。
- `datetime` 与 `range` 是构造 **滚动窗口索引**、**样本内外划分** 的语法基础。

---

## 本章自检清单

- [ ] 能说明 `python` / `ipython` / `jupyter` 的区别  
- [ ] 会用 `?` 查看函数文档  
- [ ] 能解释赋值是绑定引用，并知道何时 `.copy()`  
- [ ] 会用 `is None`、会用 `datetime` / `timedelta`  
- [ ] 能写 `for` + `range` / 拆包循环  

---

## 后续扩展留白

### 2.1 Python 解释器

（留白）

### 2.2 IPython / Jupyter

（留白）

### 2.3.1 语义与引用

（留白）

### 2.3.2 标量类型

（留白）

### 2.3.3 控制流

（留白）
