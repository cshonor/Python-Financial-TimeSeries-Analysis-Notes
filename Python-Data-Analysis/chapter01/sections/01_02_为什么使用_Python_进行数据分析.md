# 1.2 为什么使用 Python 进行数据分析

> 所属：[第 1 章](../chapter01_getting_started.md) · 《利用 Python 进行数据分析》

**关联背景**：Python 1991 年诞生，2005 年后因 Django 等框架在 Web 领域流行；**GIL** 限制纯 Python 多线程并行，但 C 扩展（如 NumPy）在少交互 Python 对象时可绕开 GIL，实现高效计算。

---

## 一、书本原文核心知识点提炼

### 1.2 为什么使用 Python 进行数据分析

Python 成为数据分析首选，本质是 **简洁语法 + 全能生态 + 免费开源 + 强社区** 的组合：覆盖 **采集 → 清洗 → 分析 → 可视化 → 建模 → 部署** 全链路，低门槛上手、专家可深度定制。

#### 1. 核心优势：生态「全能」，覆盖全链路

| 领域 | 代表库 | 要点 |
|------|--------|------|
| 表格数据处理 | **pandas** | DataFrame / Series；清洗、聚合、透视、时间序列 |
| 数值计算 | **NumPy** | ndarray 向量化；矩阵运算、线代、随机数；pandas / SciPy 基石 |
| 可视化 | Matplotlib、Seaborn、Plotly | 静态定制 / 统计美化 / 交互式仪表盘 |
| 机器学习 | scikit-learn、TensorFlow、PyTorch | 经典 ML「全家桶」/ 深度学习 |
| 大数据扩展 | PySpark、Dask | TB 级、分布式，兼容 Spark 生态 |

各库详解见 [1.3 重要的 Python 库](./01_03_重要的_Python_库.md)；NumPy 专题见 [`../../code/numpy/`](../../code/numpy/)。

#### 2. 语法优势：简洁易学

- **可读性强**：缩进规范，接近伪代码，协作成本低。
- **动态类型**：灵活处理数值、字符串、日期、布尔等异构字段。
- **开发效率高**：同样任务通常比 Java/C++ 代码量更少，可专注分析逻辑。

#### 3. 社区与生态

- **开源免费**：核心栈无授权成本。
- **全球社区**：GitHub、Stack Overflow、Kaggle 资源密集。
- **Jupyter Notebook**：代码 + 文字 + 图表 + 公式一体化，适合探索与报告。

#### 4. 跨平台与集成

- Windows / Linux / macOS 通用。
- 可调用 C/C++/Java/R，也可嵌入现有系统。
- 连接 MySQL、PostgreSQL、MongoDB、SQLite 及 REST API / 爬虫。

#### 5. 与其他工具对比

| 工具 | 优势 | 劣势 | Python 胜出点 |
|------|------|------|----------------|
| Excel | 上手快、直观 | 行数受限、难自动化、复杂分析弱 | 大数据、可编程、可复用、可建模 |
| R | 统计传统强 | 工程化、Web 部署相对弱 | 全链路（分析+工程+AI）、就业面更广 |
| SAS / SPSS | 企业合规 | 收费、封闭、扩展差 | 开源、生态开放、云原生友好 |

#### 6. GIL（全局解释器锁）

- 纯 Python **同一进程内**多线程无法并行占用多核做 CPU 密集计算。
- **应对**：
  1. **多进程**（`multiprocessing`）绕过 GIL；
  2. **C 扩展**（NumPy、scikit-learn）在计算时释放 GIL；
  3. **分布式**（PySpark、Dask）突破单机。

---

## 二、关键语法速查表（核心库入门）

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression

# NumPy：向量与矩阵
arr = np.array([1, 2, 3])
mat = np.random.default_rng(0).standard_normal((100, 3))
mat.mean(axis=0)

# pandas：表格
df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
df.describe()
df.groupby("x")["y"].mean()

# 可视化
fig, ax = plt.subplots()
ax.plot(df["x"], df["y"], marker="o")
ax.set_title("demo")
plt.show()
```

| 库 | 常用导入 | 本仓库深入 |
|----|----------|------------|
| NumPy | `import numpy as np` | [`../../code/numpy/`](../../code/numpy/) · 第 4 章 |
| pandas | `import pandas as pd` | 第 5 章 · [金融大数据 pandas 专题](../../../Python-Financial-BigData-Analysis/chapter05/) |
| Matplotlib | `import matplotlib.pyplot as plt` | [`../../code/matplotlib/`](../../code/matplotlib/) · 第 9 章 |
| scikit-learn | `from sklearn...` | 推断向建模见 statsmodels 第 12 章 |
| statsmodels | `import statsmodels.api as sm` | [`../../code/statsmodels/`](../../code/statsmodels/) |

---

## 三、演示

环境检查与显示选项：[`../code/chapter01_environment_setup.py`](../code/chapter01_environment_setup.py)

```bash
python Python-Data-Analysis/chapter01/code/chapter01_environment_setup.py
```

---

## 四、【量化专属改造】

1. **选型结论**：量化日常 = **pandas（表）+ NumPy（向量化）+ Matplotlib（复盘图）**；推断用 statsmodels，预测用 sklearn / 深度学习按需加。
2. **GIL 实战**：回测循环、大规模矩阵运算优先写 **NumPy/pandas 向量化** 或 **多进程**，避免纯 Python 双层 for + 多线程。
3. **Excel 边界**：Excel 做 ad-hoc 查看；**百万行行情、多标的因子表、可复现 pipeline** 必须落 Python 脚本 + 版本管理。
4. **与 R 分工**：统计公式推导仍可读 Wooldridge / 计量教材；**工程化数据管道与部署**优先 Python（见 [`../../../Using-Python-for-Introductory-Econometrics/`](../../../Using-Python-for-Introductory-Econometrics/)）。

---

## 五、与 statsmodels 建模的衔接

- 第 1.2 节回答「为什么选 Python」；**statsmodels** 在第 12 章展开，负责 OLS、时间序列等 **带推断** 的估计。
- 学习路径：先认同工具链 → [1.3 库清单](./01_03_重要的_Python_库.md) → 第 4–5 章打 ndarray/DataFrame → 第 12 章接 statsmodels。

---

## 六、自检

- [ ] 能说出 pandas / NumPy / Matplotlib 各解决哪类问题  
- [ ] 能解释 GIL 对「纯 Python 多线程」与「NumPy 运算」的不同影响  
- [ ] 能对比 Python 与 Excel、R 在你场景下的取舍  
- [ ] 能写出 `import numpy as np` 与 `DataFrame.describe()` 一行示例  

---

## 七、留白

（补充：你所在团队的技术栈选型理由、国内数据源接口、conda/venv 实践等）

---

[← 返回第 1 章](../chapter01_getting_started.md)
