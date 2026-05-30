# Using Python for Introductory Econometrics 学习笔记

对应教材：**《Using Python for Introductory Econometrics》**（Florian Heiss & Daniel Brunner，对齐 Wooldridge《Introductory Econometrics》章节结构）。

> 官方站点：[urfie.net](https://www.urfie.net/) · 配套数据包：`wooldridge`（Python）

---

## 一、仓库说明

本目录为计量经济学 Python 实证配套笔记，按 **四大部分 + 附录** 归档，采用 **按章文件夹 + 共享 code 专题** 统一规范。

| 项 | 说明 |
|----|------|
| 本地文件夹 | `Using-Python-for-Introductory-Econometrics/` |
| 建议远程仓库名 | `Using-Python-for-Introductory-Econometrics-Notes` |

---

## 二、目录架构

| 子目录 / 文件 | 说明 |
|---------------|------|
| `chapter01/` … `chapter19/` | 按章拆分 |
| `chapterNN_notes.md` | 章总览 + 小节索引 + Wooldridge 衔接 |
| `sections/` | 小节笔记（`02_01_*.md` 等） |
| `code/` | 本章 Python 实证脚本 |
| [`code/python_basics/`](./code/python_basics/) | 第 1 章：Python / pandas / 描述统计 |
| [`code/ols_regression/`](./code/ols_regression/) | 第 2–9 章：截面 OLS、推断、异方差 |
| [`code/time_series/`](./code/time_series/) | 第 10–12、18 章：时间序列 |
| [`code/panel_data/`](./code/panel_data/) | 第 13–14 章：面板 / DID / FE-RE |
| [`code/iv_2sls/`](./code/iv_2sls/) | 第 15–16 章：IV / 2SLS / 联立方程 |
| [`code/advanced_models/`](./code/advanced_models/) | 第 17 章：限值因变量 |
| [`appendix/`](./appendix/) | 各章脚本索引 |

---

## 三、四大部分 + 章节索引

### 第1部分 导读与 Python 基础

| 章 | 主题 | 总览 | 小节数 | 本章代码 |
|----|------|------|--------|----------|
| 1 | Introduction | [chapter01_notes.md](./chapter01/chapter01_notes.md) | 38 | [ch01_python_basics.py](./chapter01/code/ch01_python_basics.py) |

### 第2部分 截面数据回归（第 2–9 章）

| 章 | 主题 | 总览 | 小节数 | 本章代码 |
|----|------|------|--------|----------|
| 2 | Simple Regression | [chapter02_notes.md](./chapter02/chapter02_notes.md) | 11 | [ch02_simple_ols.py](./chapter02/code/ch02_simple_ols.py) |
| 3 | MR: Estimation | [chapter03_notes.md](./chapter03/chapter03_notes.md) | 4 | [ch03_multiple_ols.py](./chapter03/code/ch03_multiple_ols.py) |
| 4 | MR: Inference | [chapter04_notes.md](./chapter04/chapter04_notes.md) | 7 | [ch04_inference.py](./chapter04/code/ch04_inference.py) |
| 5 | OLS Asymptotics | [chapter05_notes.md](./chapter05/chapter05_notes.md) | 4 | [ch05_asymptotics_mc.py](./chapter05/code/ch05_asymptotics_mc.py) |
| 6 | MR: Further Issues | [chapter06_notes.md](./chapter06/chapter06_notes.md) | 9 | [ch06_prediction.py](./chapter06/code/ch06_prediction.py) |
| 7 | Qualitative Regressors | [chapter07_notes.md](./chapter07/chapter07_notes.md) | 5 | [ch07_dummy_variables.py](./chapter07/code/ch07_dummy_variables.py) |
| 8 | Heteroscedasticity | [chapter08_notes.md](./chapter08/chapter08_notes.md) | 3 | [ch08_robust_wls.py](./chapter08/code/ch08_robust_wls.py) |
| 9 | Specification & Data | [chapter09_notes.md](./chapter09/chapter09_notes.md) | 5 | [ch09_specification.py](./chapter09/code/ch09_specification.py) |

### 第3部分 时间序列回归（第 10–12 章）

| 章 | 主题 | 总览 | 小节数 | 本章代码 |
|----|------|------|--------|----------|
| 10 | TS Basics | [chapter10_notes.md](./chapter10/chapter10_notes.md) | 7 | [ch10_time_series_static.py](./chapter10/code/ch10_time_series_static.py) |
| 11 | TS OLS Issues | [chapter11_notes.md](./chapter11/chapter11_notes.md) | 4 | [ch11_unit_root_intro.py](./chapter11/code/ch11_unit_root_intro.py) |
| 12 | Serial Correlation | [chapter12_notes.md](./chapter12/chapter12_notes.md) | 4 | [ch12_serial_correlation.py](./chapter12/code/ch12_serial_correlation.py) |

### 第4部分 高级专题与实证（第 13–19 章）

| 章 | 主题 | 总览 | 小节数 | 本章代码 |
|----|------|------|--------|----------|
| 13 | Pooled / DID | [chapter13_notes.md](./chapter13/chapter13_notes.md) | 5 | [ch13_did_pooled.py](./chapter13/code/ch13_did_pooled.py) |
| 14 | Advanced Panel | [chapter14_notes.md](./chapter14/chapter14_notes.md) | 4 | [ch14_panel_fe_re.py](./chapter14/code/ch14_panel_fe_re.py) |
| 15 | IV & 2SLS | [chapter15_notes.md](./chapter15/chapter15_notes.md) | 6 | [ch15_iv_2sls.py](./chapter15/code/ch15_iv_2sls.py) |
| 16 | Simultaneous EQ | [chapter16_notes.md](./chapter16/chapter16_notes.md) | 4 | [ch16_simultaneous.py](./chapter16/code/ch16_simultaneous.py) |
| 17 | Limited DV | [chapter17_notes.md](./chapter17/chapter17_notes.md) | 9 | [ch17_binary_probit_logit.py](./chapter17/code/ch17_binary_probit_logit.py) |
| 18 | Advanced TS | [chapter18_notes.md](./chapter18/chapter18_notes.md) | 5 | [ch18_cointegration.py](./chapter18/code/ch18_cointegration.py) |
| 19 | Empirical Project | [chapter19_notes.md](./chapter19/chapter19_notes.md) | 6 | [ch19_empirical_workflow.py](./chapter19/code/ch19_empirical_workflow.py) |

**合计**：19 章 · **约 153 个小节节点**（含二级子节）

### 附录

| 附录 | 说明 |
|------|------|
| [appendix_scripts_index.md](./appendix/appendix_scripts_index.md) | 各章 `code/` 脚本索引（对齐 UPfIE Scripts） |

---

## 四、推荐学习顺序

1. `chapter01/` → 安装环境、`wooldridge` 数据、描述统计与 Monte Carlo  
2. `chapter02/` → `chapter09/` + [`code/ols_regression/`](./code/ols_regression/)  
3. `chapter10/` → `chapter12/` + [`code/time_series/`](./code/time_series/)  
4. `chapter13/` → `chapter18/` + 面板 / IV / 限值因变量专题  
5. `chapter19/` 综合实证项目（Jupyter + 可复现脚本）

**前置**（可选）：[`../Python-Data-Analysis/`](../Python-Data-Analysis/) NumPy / pandas 基础

---

## 五、环境安装

```bash
pip install numpy pandas matplotlib scipy statsmodels jupyter linearmodels wooldridge
```

---

## 六、运行示例

```bash
python Using-Python-for-Introductory-Econometrics/chapter01/code/ch01_python_basics.py
python Using-Python-for-Introductory-Econometrics/code/ols_regression/ch02_simple_ols.py
python Using-Python-for-Introductory-Econometrics/code/time_series/ch12_serial_correlation.py
```

---

## 七、学习资源

- [UPfIE 官网](https://www.urfie.net/)
- [statsmodels 文档](https://www.statsmodels.org/)
- [Wooldridge《Introductory Econometrics》](https://www.cengage.com/)（理论主教材）
- [wooldridge 数据包](https://pypi.org/project/wooldridge/)

---

## 八、与其他「Python for Finance / Econometrics」书的区分

| 书 | 作者 | 章数 | 本 mono-repo 路径 |
|----|------|------|-------------------|
| *Using Python for Introductory Econometrics* | Heiss & Brunner | **19** | **本目录** |
| *Python for Data Analysis* | Wes McKinney | 13 | [`Python-Data-Analysis/`](../Python-Data-Analysis/) |
| *Python for Finance* (Packt) | Yuxing Yan | 17 | （未建册） |
| *Mastering Data-Driven Finance* | Yves Hilpisch | 21 | [`Python-Financial-BigData-Analysis/`](../Python-Financial-BigData-Analysis/) |
