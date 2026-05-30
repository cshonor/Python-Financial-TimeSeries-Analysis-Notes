# Python-Financial-TimeSeries-Analysis-Notes

Python **金融时序分析**学习笔记仓库：按四本教材分册归档，每册以 **按章文件夹** + **共享 code 专题** 为主结构。

> 本地文件夹名可能仍为 `python-data-Analyze`（历史仓库名）；GitHub 远程仓库可逐步改名为与本标题一致。

---

## 四本书目录

| 文件夹 | 对应教材 | 当前主要内容 |
|--------|----------|----------------|
| [Python-Data-Analysis](./Python-Data-Analysis/) | 《利用 Python 进行数据分析》 | 13 章分册（`chapter01/`～`chapter13/`）+ NumPy / Matplotlib 等共享专题 |
| [Python-Financial-BigData-Analysis](./Python-Financial-BigData-Analysis/) | 《Python金融大数据分析（第2版）》Hilpisch | **21 章**分册 + `code/pandas/` 深化专题 |
| [Python-Time-Series-Forecast](./Python-Time-Series-Forecast/) | 《Python 时间序列预测》 | 21 章分册 + `code/time_series_quant/` 时序专题 |
| [Financial-Data-Python-Application](./Financial-Data-Python-Application/) | 《金融数据分析及其 Python 应用》 | 预留：金融案例、应用向笔记与习题 |

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
├── Python-Time-Series-Forecast/
├── Python-Data-Analysis/
├── Python-Financial-BigData-Analysis/
└── Financial-Data-Python-Application/
```

---

## 推荐学习顺序

1. **Python-Data-Analysis**：`chapter01/` → `chapter13/` 按章精读；共享专题见 `code/numpy/`、`code/matplotlib/` 等  
2. **Python-Financial-BigData-Analysis**：`chapter01/` → `chapter21/`（Hilpisch 第2版）；深化见 `code/pandas/`  
3. **Python-Time-Series-Forecast**：`chapter01/` → `chapter21/` + `code/time_series_quant/` 重采样、窗口、信号对齐  
4. **Financial-Data-Python-Application**：综合案例与建模应用（持续填充）

---

## 环境安装

```bash
pip install numpy pandas matplotlib scipy statsmodels
```

运行示例（路径已按新结构更新）：

```bash
python Python-Data-Analysis/chapter01/code/chapter01_environment_setup.py
python Python-Data-Analysis/code/numpy/01_create_ndarray.py
python Python-Financial-BigData-Analysis/code/pandas/00_core_objects/chapter02_pandas_data_structures_quant.py
python Python-Time-Series-Forecast/chapter01/code/chapter01_forecast_workflow_demo.py
# 时序专题见 Python-Time-Series-Forecast/code/time_series_quant/
```

---

## 学习资源

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [statsmodels 官方文档](https://www.statsmodels.org/)
