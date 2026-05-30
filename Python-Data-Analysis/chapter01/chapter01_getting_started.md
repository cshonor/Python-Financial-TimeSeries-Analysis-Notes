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

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [01_01_本书内容](./sections/01_01_本书内容.md) | 本书内容 |
| [01_02_为什么使用_Python_进行数据分析](./sections/01_02_为什么使用_Python_进行数据分析.md) | 为什么使用 Python 进行数据分析 |
| [01_03_重要的_Python_库](./sections/01_03_重要的_Python_库.md) | 重要的 Python 库 |
| [01_04_安装和设置](./sections/01_04_安装和设置.md) | 安装和设置 |
| [01_05_社区和相关会议](./sections/01_05_社区和相关会议.md) | 社区和相关会议 |
| [01_06_本书导航](./sections/01_06_本书导航.md) | 本书导航 |
| [01_06_01_代码示例](./sections/01_06_01_代码示例.md) | 01 代码示例 |
| [01_06_02_示例数据](./sections/01_06_02_示例数据.md) | 02 示例数据 |
| [01_06_03_引用惯例](./sections/01_06_03_引用惯例.md) | 03 引用惯例 |

## 二、关键语法速查表

| 用途 | 写法 |
|------|------|
| 标准导入 | `import numpy as np` / `import pandas as pd` |
| 显示选项 | `pd.set_option(...)` / `np.set_printoptions(...)` |
| 查看工作目录 | `import os; os.getcwd()` |
| Jupyter | `%pwd`、`%ls`（魔法命令，仅 notebook 内） |

---

## 三、通用基础示例

环境与显示设置见：[`./code/chapter01_environment_setup.py`](./code/chapter01_environment_setup.py)

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
