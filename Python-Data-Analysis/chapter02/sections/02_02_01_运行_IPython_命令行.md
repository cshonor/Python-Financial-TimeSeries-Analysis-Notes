# 2.2.1 运行 IPython 命令行

> 所属：[第 2 章](../chapter02_python_syntax_ipython_jupyter.md) · 《利用 Python 进行数据分析》

---

## 一、书本原文核心知识点提炼

### 2.2.1 运行 IPython 命令行

IPython 是增强型交互式 Python Shell，数据分析中常用于 **快速试代码、跑脚本、查文档**。与标准 `python` 的 `>>>` 不同，IPython 用带序号的 **`In [N]:` / `Out [N]:`** 追踪每次输入输出，便于回溯实验过程。

#### 1. 启动 IPython

| 项 | 说明 |
|----|------|
| 安装 | `pip install ipython` 或 `conda install ipython` |
| 启动 | 终端输入 `ipython` |
| 提示符 | `In [N]:` / `Out [N]:`（N 为递增序号） |
| 退出 | `quit()`、`exit()` 或 **Ctrl+D**（Windows 亦可用 **Ctrl+Z** 后 Enter） |

#### 2. 基本交互

```python
In [1]: a = 10
In [2]: a
Out[2]: 10

In [3]: import numpy as np
In [4]: [np.random.rand() for _ in range(3)]
Out[4]: [0.123, 0.456, 0.789]
```

- 最后一行表达式的值会 **自动显示**（不必 `print`），且 **格式化、可读性更强**。
- 自带语法高亮、Tab 补全、命令历史（↑↓ 翻阅）。

#### 3. 核心魔法命令（本节重点）

魔法命令以 **`%`**（单行）或 **`%%`**（整 cell，主要在 Jupyter）开头，由 IPython 解释，不是 Python 语法。

| 命令 | 作用 |
|------|------|
| **`%run script.py`** | 在当前 IPython **同一进程**内执行脚本；脚本内变量留在当前命名空间 |
| **`%quickref`** | 打印 IPython 快速参考卡 |
| **`%magic`** | 列出所有魔法命令 |
| **`%timeit expr`** | 多次运行并统计耗时（微基准测试） |
| **`%pwd` / `%cd dir`** | 查看/切换工作目录 |
| **`%who` / `%whos`** | 列出当前变量（`whos` 含类型与大小） |
| **`%history`** | 查看输入历史 |
| **`%reset`** | 清空命名空间（`-f` 跳过确认） |

```python
In [1]: %run hello.py
Hello World!

In [2]: %quickref   # 弹出速查
```

#### 4. 对象帮助（? / ??）

| 写法 | 作用 |
|------|------|
| **`obj?`** | 类型、文档字符串、文件位置 |
| **`obj??`** | 在 `?` 基础上尝试 **显示源码** |
| **`np.*load*?`** | 命名空间 **通配搜索**（见 2.2.4） |

#### 5. 系统 Shell 命令（!）

在 IPython 中用 **`!`** 前缀调用操作系统命令，输出捕获到当前会话：

```python
In [1]: !ls          # macOS / Linux
In [2]: !dir         # Windows
In [3]: !pip list    # 查看已装包
```

#### 6. 与标准 Python Shell 对比

| 能力 | 标准 `python` | IPython |
|------|---------------|---------|
| 提示符 | `>>>` | `In [N]:` / `Out [N]:` |
| 自动显示最后表达式 | 否 | 是 |
| Tab 补全 / 高亮 | 基础 | 强 |
| 魔法命令 | 无 | `%run`、`%timeit` 等 |
| 自省 | 有限 | `?` / `??` |
| Shell 集成 | 无 | `!cmd` |

---

## 二、速查清单（可直接复制）

### 启动与退出

```bash
ipython              # 启动
quit() / exit()      # 退出
# Ctrl+D（Unix）或 Ctrl+Z + Enter（Windows）
```

### 最常用魔法命令表

| 命令 | 一句话 |
|------|--------|
| `%run file.py` | 同进程跑脚本，变量可继续用 |
| `%timeit code` | 测性能 |
| `%who` / `%whos` | 看当前变量 |
| `%pwd` / `%cd path` | 目录 |
| `%quickref` | 速查卡 |
| `%history -n 5` | 最近 5 条输入 |
| `%reset -f` | 清空变量 |

### 帮助与 Shell

| 写法 | 作用 |
|------|------|
| `pd.read_csv?` | 函数文档 |
| `pd.DataFrame??` | 尝试看源码 |
| `!dir` / `!ls` | 系统命令 |

---

## 三、演示

### 在本仓库中试 `%run`

激活环境后：

```bash
ipython
```

```python
In [1]: %cd Python-Data-Analysis/chapter02/code   # 或 %cd 到绝对路径
In [2]: %run chapter02_python_basics_demo.py
In [3]: %whos    # 查看脚本是否留下变量
```

Jupyter / Lab 中对应写法：`%run chapter02_python_basics_demo.py`（同一内核）。

---

## 四、【量化专属改造】

1. **探索 vs 生产**：因子试算、API 探针用 **IPython / Jupyter**；定稿回测脚本用 **`python strategy.py`** 或 `%run` 后导出为 `.py`。
2. **`%run` 命名空间污染**：脚本里定义的 `df`、`model` 会留在当前会话；重复 `%run` 前用 `%reset -f` 或重启内核，避免 **旧变量覆盖新结果**。
3. **`%timeit` 测 pandas**：比较 `df.apply` vs 向量化时，在 IPython 里 `%timeit` 比手写 `time.time()` 更稳。
4. **`!` 拉数据**：临时 `!curl ... -o data.csv` 或 Windows `!powershell ...`，再用 `pd.read_csv` — 适合一次性下载，生产环境仍建议独立脚本。

---

## 五、与 statsmodels / 建模的衔接

- 在 IPython 里 `%run` 清洗脚本后，同一进程接着 `import statsmodels.formula.api as smf` 做 OLS，**中间 DataFrame 不必重复读盘**。
- 用 `%whos` 确认回归前 `df.shape`、`df.dtypes` 无误，再 `fit = smf.ols(...).fit()`。
- 建模前 `%reset -f` 可避免上次实验残留的全局变量干扰系数结果。

---

## 六、自检

- [ ] 能说出 `In [N]:` 与 `>>>` 的区别  
- [ ] 会用 `%run` 并在同一 session 继续操作变量  
- [ ] 会用 `obj?` 查 pandas / NumPy 函数  
- [ ] 知道 `!dir`（Windows）与 `!ls`（Unix）的用途  
- [ ] 能解释 `%run` 与终端 `python script.py` 的进程/命名空间差异（同进程 vs 子进程）  

---

## 七、留白

（记录：你的 ipython 配置文件路径、常用 `%run` 脚本列表、Jupyter 与 IPython 切换习惯）

---

**相关小节**：[2.2.3 Tab 补全](./02_02_03_Tab_补全.md) · [2.2.4 自省](./02_02_04_自省.md) · [2.2.2 Jupyter Notebook](./02_02_02_运行_Jupyter_Notebook.md)

[← 返回第 2 章](../chapter02_python_syntax_ipython_jupyter.md)
