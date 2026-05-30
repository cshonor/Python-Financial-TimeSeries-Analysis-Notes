# 第 1 章 Introduction

> 对应教材：《Using Python for Introductory Econometrics》（Using Python for Introductory Econometrics (Heiss & Brunner, Wooldridge-aligned)）  
> 第1部分 导读与 Python 基础  
> 本章 → [第 2 章](../chapter02/chapter02_notes.md)

**本章脚本**：[`./code/ch01_python_basics.py`](./code/ch01_python_basics.py)  

**共享专题**：[`../code/python_basics/`](../code/python_basics/)

---

## 章节总览

**小节统计**：42 个逻辑小节（含二级子节）。

| 一级 | 二级 / 子模块 |
|------|----------------|
| 1.1 Getting Started | Software；Python Scripts；Packages；File Names and Working Directory；Errors and Warnings；Other Resources |
| 1.2 Objects in Python | Scalars and Types；Lists and Vectors；Matrices and Arrays；Indexing and Subsetting |
| 1.3 Data Frames and Data Files | Data Frames；Import CSV and Excel；RData and Pickle；Basic Data Set Information；wooldridge Package |
| 1.4 Visualizing Data | matplotlib Basics；Customizing Graphs；Exporting Figures |
| 1.5 Data Manipulation with pandas | pandas Basics；Grouping and Aggregation；Merging |
| 1.6 Descriptive Statistics | Discrete Distributions；Histogram and Density；ECDF；Fundamental Statistics |
| 1.7 Probability Distributions | Discrete Distributions；Continuous Distributions |
| 1.8 Confidence Intervals and Statistical Inference | — |
| 1.9 More Advanced Python | Conditionals and Loops；Functions |
| 1.10 Monte Carlo Simulation | Finite Sample Properties；Asymptotic Properties；Simulation of CIs and t Tests |

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [01_01_Getting_Started.md](./sections/01_01_Getting_Started.md) | Getting Started |
| [01_01_01_Software.md](./sections/01_01_01_Software.md) | Software |
| [01_01_02_Python_Scripts.md](./sections/01_01_02_Python_Scripts.md) | Python Scripts |
| [01_01_03_Packages.md](./sections/01_01_03_Packages.md) | Packages |
| [01_01_04_File_Names_and_Working_Directory.md](./sections/01_01_04_File_Names_and_Working_Directory.md) | File Names and Working Directory |
| [01_01_05_Errors_and_Warnings.md](./sections/01_01_05_Errors_and_Warnings.md) | Errors and Warnings |
| [01_01_06_Other_Resources.md](./sections/01_01_06_Other_Resources.md) | Other Resources |
| [01_02_Objects_in_Python.md](./sections/01_02_Objects_in_Python.md) | Objects in Python |
| [01_02_01_Scalars_and_Types.md](./sections/01_02_01_Scalars_and_Types.md) | Scalars and Types |
| [01_02_02_Lists_and_Vectors.md](./sections/01_02_02_Lists_and_Vectors.md) | Lists and Vectors |
| [01_02_03_Matrices_and_Arrays.md](./sections/01_02_03_Matrices_and_Arrays.md) | Matrices and Arrays |
| [01_02_04_Indexing_and_Subsetting.md](./sections/01_02_04_Indexing_and_Subsetting.md) | Indexing and Subsetting |
| [01_03_Data_Frames_and_Data_Files.md](./sections/01_03_Data_Frames_and_Data_Files.md) | Data Frames and Data Files |
| [01_03_01_Data_Frames.md](./sections/01_03_01_Data_Frames.md) | Data Frames |
| [01_03_02_Import_CSV_and_Excel.md](./sections/01_03_02_Import_CSV_and_Excel.md) | Import CSV and Excel |
| [01_03_03_RData_and_Pickle.md](./sections/01_03_03_RData_and_Pickle.md) | RData and Pickle |
| [01_03_04_Basic_Data_Set_Information.md](./sections/01_03_04_Basic_Data_Set_Information.md) | Basic Data Set Information |
| [01_03_05_wooldridge_Package.md](./sections/01_03_05_wooldridge_Package.md) | wooldridge Package |
| [01_04_Visualizing_Data.md](./sections/01_04_Visualizing_Data.md) | Visualizing Data |
| [01_04_01_matplotlib_Basics.md](./sections/01_04_01_matplotlib_Basics.md) | matplotlib Basics |
| [01_04_02_Customizing_Graphs.md](./sections/01_04_02_Customizing_Graphs.md) | Customizing Graphs |
| [01_04_03_Exporting_Figures.md](./sections/01_04_03_Exporting_Figures.md) | Exporting Figures |
| [01_05_Data_Manipulation_with_pandas.md](./sections/01_05_Data_Manipulation_with_pandas.md) | Data Manipulation with pandas |
| [01_05_01_pandas_Basics.md](./sections/01_05_01_pandas_Basics.md) | pandas Basics |
| [01_05_02_Grouping_and_Aggregation.md](./sections/01_05_02_Grouping_and_Aggregation.md) | Grouping and Aggregation |
| [01_05_03_Merging.md](./sections/01_05_03_Merging.md) | Merging |
| [01_06_Descriptive_Statistics.md](./sections/01_06_Descriptive_Statistics.md) | Descriptive Statistics |
| [01_06_01_Discrete_Distributions.md](./sections/01_06_01_Discrete_Distributions.md) | Discrete Distributions |
| [01_06_02_Histogram_and_Density.md](./sections/01_06_02_Histogram_and_Density.md) | Histogram and Density |
| [01_06_03_ECDF.md](./sections/01_06_03_ECDF.md) | ECDF |
| [01_06_04_Fundamental_Statistics.md](./sections/01_06_04_Fundamental_Statistics.md) | Fundamental Statistics |
| [01_07_Probability_Distributions.md](./sections/01_07_Probability_Distributions.md) | Probability Distributions |
| [01_07_01_Discrete_Distributions.md](./sections/01_07_01_Discrete_Distributions.md) | Discrete Distributions |
| [01_07_02_Continuous_Distributions.md](./sections/01_07_02_Continuous_Distributions.md) | Continuous Distributions |
| [01_08_Confidence_Intervals_and_Statistical_Inference.md](./sections/01_08_Confidence_Intervals_and_Statistical_Inference.md) | Confidence Intervals and Statistical Inference |
| [01_09_More_Advanced_Python.md](./sections/01_09_More_Advanced_Python.md) | More Advanced Python |
| [01_09_01_Conditionals_and_Loops.md](./sections/01_09_01_Conditionals_and_Loops.md) | Conditionals and Loops |
| [01_09_02_Functions.md](./sections/01_09_02_Functions.md) | Functions |
| [01_10_Monte_Carlo_Simulation.md](./sections/01_10_Monte_Carlo_Simulation.md) | Monte Carlo Simulation |
| [01_10_01_Finite_Sample_Properties.md](./sections/01_10_01_Finite_Sample_Properties.md) | Finite Sample Properties |
| [01_10_02_Asymptotic_Properties.md](./sections/01_10_02_Asymptotic_Properties.md) | Asymptotic Properties |
| [01_10_03_Simulation_of_CIs_and_t_Tests.md](./sections/01_10_03_Simulation_of_CIs_and_t_Tests.md) | Simulation of CIs and t Tests |

---

## Wooldridge 理论衔接

（留白：本章在 Wooldridge《Introductory Econometrics》中的位置与核心假设）

---

## statsmodels / Python 速查

（留白）

---

## 自检

- [ ] 能解释本章估计量/检验在 Wooldridge 中的假设
- [ ] 能复现 UPfIE 至少一个 Script 示例
- [ ] 已完成重点小节笔记

---

## 留白

