# 第 1 章 准备工作（Getting Started）

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 1 章。  
> 本章不深入具体分析方法，而是介绍 **Python 数据分析库生态** 与 **环境准备**，为后续结构化数据的清洗、规整与建模打基础。

---

## 章节总览

本章侧重：编程语言与工具链，而非纯「数据分析方法论」。书中「数据」主要指 **结构化数据**：表格/关系型、多维数组、多表关联、时间序列等。

**小节统计**：6 个一级小节 + 11 个二级小节，共 17 个小节。

| 一级 | 二级 |
|------|------|
| 1.1 本书内容 | — |
| 1.2 为什么使用 Python 进行数据分析 | — |
| 1.3 重要的 Python 库 | 1.3.1～1.3.8 |
| 1.4 安装和设置 | — |
| 1.5 社区和相关会议 | — |
| 1.6 本书导航 | 1.6.1～1.6.3 |

---

## 一、书本原文核心知识点提炼

### 1.1 本书内容

- **目标**：用 Python 完成数据的操作、处理、清洗、规整；重点是 **语言 + 库 + 工具**，不是全套数据分析方法论。
- **数据范围**：结构化数据（表、矩阵、多表、时间序列）。
- **定位**：打好「把混乱数据变成规整表格」的能力，为机器学习、数据科学等进阶领域做准备。

### 1.2 为什么使用 Python 进行数据分析

- Python（1991 起）是主流解释型语言之一；2005 年后在 Web（如 Django）等领域广泛流行。
- **GIL**：纯 Python 多线程受限；C 扩展在少与 Python 对象交互时可并行，不受 GIL 影响。

### 1.3 重要的 Python 库（生态地图）

| 小节 | 库 | 一句话 |
|------|-----|--------|
| 1.3.1 | **NumPy** | 多维数组 `ndarray` + 向量化运算；库之间传递数据的「容器」 |
| 1.3.2 | **pandas** | `DataFrame` / `Series`；表格清洗与索引是本书核心 |
| 1.3.3～4 | **IPython / Jupyter** | 交互式探索；代码与 Markdown 融合 |
| 1.3.5 | **SciPy** | 科学计算问题集合（优化、积分、统计等） |
| 1.3.6 | **scikit-learn** | 机器学习（分类、回归、聚类、降维等）；本书仅简要涉及 |
| 1.3.7 | **statsmodels** | 统计推断、经典模型、时间序列；强调 p 值与不确定性 |
| 1.3.8 | **其他** | TensorFlow / PyTorch 等；建议先学好数据规整再学深度学习 |

**与本仓库 `code/` 的对应**：

- NumPy → [`../code/numpy/`](../code/numpy/)
- Matplotlib → [`../code/matplotlib/`](../code/matplotlib/)
- SciPy → [`../code/scipy/`](../code/scipy/)
- statsmodels → [`../code/statsmodels/`](../code/statsmodels/)
- pandas 专题 → [`../../Python-Financial-BigData-Analysis/code/pandas/`](../../Python-Financial-BigData-Analysis/code/pandas/)

### 1.4 安装和设置

- 没有「唯一正确」的 Python 环境；按用途（科研、Web、量化）选择 conda / venv / Docker 等均可。

### 1.5 社区和相关会议

- 建议参与开源社区与线下会议；常见会议：PyCon、EuroPython、SciPy、EuroSciPy、PyData 等。

### 1.6 本书导航

- **新手**：先读原书第 2、3 章（Python 基础 + Jupyter）。
- **主线**：NumPy → pandas → matplotlib 处理数据分析问题。

**数据分析五大类任务**（全书骨架）：

1. 与外部世界交互（读写文件/数据库）
2. 数据准备（清洗、整理、联合、重塑、切片）
3. 数据转换（统计/数学运算生成新数据集）
4. 建模和计算（统计模型、机器学习）
5. 演示（可视化、报告）

#### 1.6.1 代码示例

- 书中代码按 IPython/Jupyter 的 `In:` / `Out:` 形式排版。
- 为匹配书中输出，需调整 NumPy、pandas 显示选项（见配套脚本）。

#### 1.6.2 示例数据

- 数据集在 GitHub（国内可用 Gitee 镜像）；需解压并在终端 `cd` 到数据目录再运行示例。

#### 1.6.3 引用惯例

- 标准别名：`numpy as np`、`pandas as pd`、`matplotlib.pyplot as plt` 等。
- **避免** `from numpy import *` 这类一次性导入整包。

---

## 二、关键语法速查表

| 用途 | 写法 |
|------|------|
| 标准导入 | `import numpy as np` / `import pandas as pd` |
| 显示选项 | `pd.set_option(...)` / `np.set_printoptions(...)` |
| 查看工作目录 | `import os; os.getcwd()` |
| Jupyter | `%pwd`、`%ls`（魔法命令，仅 notebook 内） |

---

## 三、通用基础示例

环境与显示设置见：[`../code/chapter01_environment_setup.py`](../code/chapter01_environment_setup.py)

```python
import numpy as np
import pandas as pd

np.set_printoptions(precision=4, suppress=True)
pd.options.display.max_columns = 20

print(np.__version__)
print(pd.__version__)
```

---

## 四、【量化专属改造】金融实战衔接

1. **结构化数据即交易数据**：OHLCV 表、因子长表、`(date, code)` 多标的是本书「结构化数据」在量化中的具体形态（详见金融大数据册第 2 章笔记）。
2. **工具链优先级**：NumPy（向量化）→ pandas（表格）→ 时序专题（重采样、rolling、shift）→ statsmodels（回归/ARIMA）。
3. **环境建议**：单独 `venv` 或 conda 环境；固定 `requirements.txt`；随机实验固定 `np.random.default_rng(seed)`。
4. **勿跳过第 1 章**：量化项目失败常见原因不是模型，而是 **环境不一致、导入混乱、显示/路径错误导致复现失败**。

---

## 五、与 statsmodels 建模的衔接要点

- 第 1 章不建模，但已点名 **statsmodels** 与 **scikit-learn** 的分工：前者偏 **推断**（标准误、p 值），后者偏 **预测**。
- 学完本章应能做到：正确安装依赖、使用社区别名、统一控制台输出，保证后续 OLS/ARIMA 示例可复现。
- 建模前数据形态要求（预告）：二维 `DataFrame`、明确 `dtype`、时间索引有序、解释变量无未来泄漏——这些在 pandas 清洗章节中落实。

---

## 本章自检清单

- [ ] 能说出 NumPy / pandas / matplotlib / SciPy / statsmodels 各自解决什么问题  
- [ ] 能配置与书中一致的 `np.set_printoptions` / `pd.options.display`  
- [ ] 使用 `import numpy as np` 等别名，不用 `import *`  
- [ ] 能对照「五大类任务」规划自己仓库各章该放哪类笔记  

---

## 后续扩展留白

> 可在下方按小节补充你的读书批注、勘误、与国内数据源（聚宽/Tushare）环境的差异说明。

### 1.1 本书内容

（留白）

### 1.2 为什么使用 Python

（留白）

### 1.3.x 各库

（留白）

### 1.4～1.6

（留白）
