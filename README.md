# Python-Financial-TimeSeries-Analysis-Notes

Python **金融时序分析**学习笔记仓库：按四本教材分册归档，每册统一采用 `docs / code / dataset / exercise / assets` 五层结构，便于长期维护、检索与扩展。

> 本地文件夹名可能仍为 `python-data-Analyze`（历史仓库名）；GitHub 远程仓库可逐步改名为与本标题一致。

---

## 四本书目录

| 文件夹 | 对应教材 | 当前主要内容 |
|--------|----------|----------------|
| [Python-Data-Analysis](./Python-Data-Analysis/) | 《利用 Python 进行数据分析》 | NumPy、Matplotlib、SciPy、statsmodels 示例与笔记 |
| [Python-Financial-BigData-Analysis](./Python-Financial-BigData-Analysis/) | 《Python 数据金融大数据分析》 | Pandas 量化预处理体系（核心对象、清洗、多标的等） |
| [Python-Time-Series-Forecast](./Python-Time-Series-Forecast/) | 《Python 时间序列预测》 | 时序量化专题（rolling / resample / shift 等） |
| [Financial-Data-Python-Application](./Financial-Data-Python-Application/) | 《金融数据分析及其 Python 应用》 | 预留：金融案例、应用向笔记与习题 |

---

## 单本书内部结构（统一规范）

```text
<书名文件夹>/
├── docs/       # Markdown 笔记、章节总结、知识图谱
├── code/       # 可运行脚本、模型与工具函数
├── dataset/    # 配套数据、离线样本（勿提交超大私密数据）
├── exercise/   # 课后习题、复盘与实战练习
└── assets/     # 截图、公式图、思维导图等资源
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

1. **Python-Data-Analysis**：NumPy 向量化 → Matplotlib 可视化 →（可选）SciPy / statsmodels 入门  
2. **Python-Financial-BigData-Analysis**：`code/pandas/` 数据结构 → 清洗 → 多标的  
3. **Python-Time-Series-Forecast**：`code/time_series_quant/` 重采样、窗口、信号对齐  
4. **Financial-Data-Python-Application**：综合案例与建模应用（持续填充）

---

## 环境安装

```bash
pip install numpy pandas matplotlib scipy statsmodels
```

运行示例（路径已按新结构更新）：

```bash
python Python-Data-Analysis/code/numpy/01_create_ndarray.py
python Python-Financial-BigData-Analysis/code/pandas/00_core_objects/chapter02_pandas_data_structures_quant.py
# 时序笔记见 Python-Time-Series-Forecast/code/time_series_quant/
```

---

## 学习资源

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [statsmodels 官方文档](https://www.statsmodels.org/)
