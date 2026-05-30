# Python-Financial-TimeSeries-Analysis-Notes

Python **金融时序与计量**学习笔记仓库：按多本教材分册归档，每册以 **按章文件夹** + **共享 code 专题** 为主结构。

> 本地文件夹名可能仍为 `python-data-Analyze`（历史仓库名）；GitHub 远程仓库可逐步改名为与本标题一致。

---

## 教材分册

| 文件夹 | 对应教材 | 当前主要内容 |
|--------|----------|----------------|
| [Python-Data-Analysis](./Python-Data-Analysis/) | 《利用 Python 进行数据分析》McKinney | 13 章分册 + NumPy / Matplotlib 等共享专题 |
| [Python-Financial-BigData-Analysis](./Python-Financial-BigData-Analysis/) | 《Python金融大数据分析（第2版）》Hilpisch | 21 章分册 + `code/pandas/` 深化专题 |
| [Python-Time-Series-Forecast](./Python-Time-Series-Forecast/) | 《Python 时间序列预测》 | 21 章分册 + `code/time_series_quant/` |
| [Using-Python-for-Introductory-Econometrics](./Using-Python-for-Introductory-Econometrics/) | 《Using Python for Introductory Econometrics》Heiss & Brunner | **19 章**分册 + OLS / 面板 / IV 等共享专题 |
| [Financial-Data-Python-Application](./Financial-Data-Python-Application/) | 《金融数据分析及其 Python 应用》 | 预留 |

---

## 单本书内部结构（统一规范）

```text
<书名文件夹>/
├── chapter01/ … chapterNN/   # 按章拆分
│   ├── chapterNN_*.md        # 章总览
│   ├── sections/             # 小节笔记（按需，如 Python-Data-Analysis）
│   └── code/                 # 本章脚本
└── code/                     # 跨章共享专题（numpy、time_series_quant、pandas 等）
```

---

## 完整层级预览

```text
Python-Financial-TimeSeries-Analysis-Notes/
├── Using-Python-for-Introductory-Econometrics/
├── Python-Time-Series-Forecast/
├── Python-Data-Analysis/
├── Python-Financial-BigData-Analysis/
└── Financial-Data-Python-Application/
```

---

## 五本书阅读顺序（总路线）

整体原则：**先打 Python 数据栈 → 再计量推断 → 再金融大数据工程 → 再预测专精 → 最后综合应用**。  
五本书角色不同，不必逐字读完一本再开下一本；下面标了 **可并行** 的段落。

```text
阶段 0 ── Python-Data-Analysis（McKinney）          ← 全库地基
    │
    ├─ 阶段 1 ── Using-Python-for-Introductory-Econometrics  ← 计量 / 回归主线
    │
    ├─ 阶段 2 ── Python-Financial-BigData-Analysis（Hilpisch）← 金融数据与策略
    │       └─ 阶段 3 ── Python-Time-Series-Forecast       ← 预测专精（可与阶段2后半并行）
    │
    └─ 阶段 4 ── Financial-Data-Python-Application           ← 综合案例（最后）
```

---

### 第 0 步：Python-Data-Analysis（必读地基）

| 顺序 | 章节 | 目的 |
|------|------|------|
| 1 | `chapter01/` → `chapter03/` | 环境、语法、数据结构 |
| 2 | `chapter04/` + [`code/numpy/`](./Python-Data-Analysis/code/numpy/) | NumPy 向量化 |
| 3 | `chapter05/` → `chapter08/` | pandas 读写、清洗、规整 |
| 4 | `chapter09/` + [`code/matplotlib/`](./Python-Data-Analysis/code/matplotlib/) | 可视化 |
| 5 | `chapter10/` → `chapter11/` | groupby、**pandas 时间序列**（后文多处会用到） |
| 6 | `chapter12/` + [`code/statsmodels/`](./Python-Data-Analysis/code/statsmodels/) | 建模库入门 |
| 7 | `chapter13/` | 端到端案例分析 |

**完成标志**：能独立读 CSV、清洗表格、画基础图、会用 `DatetimeIndex` / `resample` / `groupby`。

---

### 第 1 步：Using-Python-for-Introductory-Econometrics（计量主线）

> 理论侧配合 Wooldridge《Introductory Econometrics》；本册只负责 **Python 复现**。

| 顺序 | 章节 | 内容 | 与第 0 步的关系 |
|------|------|------|-----------------|
| 1 | `chapter01/` | Python + 描述统计 + Monte Carlo | 可与 McKinney 第 1–4 章 **并行** |
| 2 | `chapter02/` → `chapter09/` + [`code/ols_regression/`](./Using-Python-for-Introductory-Econometrics/code/ols_regression/) | 截面 OLS、推断、异方差、设定检验 | 需已掌握 pandas |
| 3 | `chapter10/` → `chapter12/` + [`code/time_series/`](./Using-Python-for-Introductory-Econometrics/code/time_series/) | 时间序列回归、单位根、序列相关 | 建议先读 McKinney `chapter11/` |
| 4 | `chapter13/` → `chapter16/` + [`code/panel_data/`](./Using-Python-for-Introductory-Econometrics/code/panel_data/)、[`code/iv_2sls/`](./Using-Python-for-Introductory-Econometrics/code/iv_2sls/) | 面板、DID、IV、2SLS、联立方程 | — |
| 5 | `chapter17/` → `chapter18/` + [`code/advanced_models/`](./Using-Python-for-Introductory-Econometrics/code/advanced_models/) | Logit/Probit、限值因变量、协整 | — |
| 6 | `chapter19/` | 实证项目：可复现脚本 + Jupyter 报告 | **本册收官** |

**完成标志**：能用 statsmodels / linearmodels 跑通 OLS、面板 FE、IV，并读懂 Wooldridge 例题的 Python 复现。

---

### 第 2 步：Python-Financial-BigData-Analysis（Hilpisch 金融大数据）

| 顺序 | 部分 | 章节 | 内容 |
|------|------|------|------|
| 1 | 第 1 部分 | `chapter01/` → `chapter02/` | 为什么用 Python、conda / Docker 环境 |
| 2 | 第 2 部分 | `chapter03/` → `chapter06/` | Python 数据结构、NumPy、pandas、OOP |
| 3 | 深化 | [`code/pandas/`](./Python-Financial-BigData-Analysis/code/pandas/) | 量化向 pandas 笔记（可与 McKinney 第 5–8 章 **对照精读**） |
| 4 | 第 3 部分 | `chapter07/` → `chapter13/` | 可视化、**金融时序**、I/O、高性能、数学工具、统计模拟 |
| 5 | 第 4 部分 | `chapter14/` → `chapter16/` | FXCM、交易策略、自动化交易 |
| 6 | 第 5 部分 | `chapter17/` → `chapter21/` | 衍生品定价、组合估值、市场校准 |

**完成标志**：能处理多标的行情表、做回测前预处理、理解 Hilpisch 案例代码结构。

---

### 第 3 步：Python-Time-Series-Forecast（预测专精）

> 建议在 **McKinney 第 11 章** 与 **Hilpisch 第 8 章** 之后进入；与计量书第 10–12 章 **互补**（计量重推断，本册重预测模型）。

| 顺序 | 章节 | 内容 |
|------|------|------|
| 1 | `chapter01/` → `chapter03/` | 预测工作流、基线、随机游走 |
| 2 | `chapter04/` → `chapter11/` | MA / AR / ARMA / ARIMA / SARIMA / SARIMAX / VAR + 综合案例 |
| 3 | 并行专题 | [`code/time_series_quant/`](./Python-Time-Series-Forecast/code/time_series_quant/) | resample、rolling、shift（量化预处理） |
| 4 | `chapter12/` → `chapter21/` | 深度学习时序、Prophet、顶点项目 |

**完成标志**：能为单变量/多变量序列选模型、做滚动验证、完成至少一个 capstone demo。

---

### 第 4 步：Financial-Data-Python-Application（综合应用）

| 说明 |
|------|
| 本册 **最后读**；在各册打牢基础后，按原书章节做 **A 股 / 业务向** 完整案例。 |
| 当前为预留结构；与 Hilpisch 第 4 章 NumPy 等内容已拆分至对应分册，勿重复学习。 |

---

### 并行与跳读建议

| 你的目标 | 建议路径 |
|----------|----------|
| **最快上手量化表格** | 第 0 步 `chapter01–08` → Hilpisch [`code/pandas/`](./Python-Financial-BigData-Analysis/code/pandas/) |
| **考研 / 计量经济学** | 第 0 步 `chapter01–05` → 第 1 步全书 |
| **因子 / 多标的策略** | 第 0 步 `chapter05–11` → Hilpisch `chapter05–16` |
| **价格预测 / 时序模型** | 第 0 步 `chapter11` → 第 3 步全书 + 计量 `chapter10–12` |
| **衍生品定价** | 第 0 步 + 第 1 步 `chapter12` → Hilpisch `chapter17–21` |

---

### 五本书一句话定位

| # | 分册 | 一句话 |
|---|------|--------|
| 1 | Python-Data-Analysis | **工具**：NumPy / pandas / 可视化 / 科学栈 |
| 2 | Using-Python-for-Introductory-Econometrics | **方法**：回归、面板、IV、限值因变量（Wooldridge 配套） |
| 3 | Python-Financial-BigData-Analysis | **工程**：金融数据、策略、定价的 Python 全栈 |
| 4 | Python-Time-Series-Forecast | **预测**：ARIMA → 深度学习 → Prophet |
| 5 | Financial-Data-Python-Application | **落地**：综合业务案例（待填充） |

---

## 环境安装

```bash
pip install numpy pandas matplotlib scipy statsmodels linearmodels wooldridge jupyter
```

运行示例（路径已按新结构更新）：

```bash
python Python-Data-Analysis/chapter01/code/chapter01_environment_setup.py
python Using-Python-for-Introductory-Econometrics/chapter01/code/ch01_python_basics.py
python Using-Python-for-Introductory-Econometrics/code/ols_regression/ch02_simple_ols.py
python Python-Financial-BigData-Analysis/code/pandas/00_core_objects/chapter02_pandas_data_structures_quant.py
python Python-Time-Series-Forecast/chapter01/code/chapter01_forecast_workflow_demo.py
```

---

## 学习资源

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [statsmodels 官方文档](https://www.statsmodels.org/)
