# 第 6 章 数据加载、存储与文件格式

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 6 章。  
> **数据 I/O** 是分析全流程的入口与出口：把 CSV、Excel、JSON、数据库、Web API 等来源的数据载入 pandas，或将结果写回磁盘。

**前置**：[第 5 章 pandas 入门](../chapter05/chapter05_pandas_introduction.md)。

**本章演示脚本**：[`./code/chapter06_data_io_demo.py`](./code/chapter06_data_io_demo.py)

---

## 章节总览

**模块统计**：5 个一级模块 + 7 个二级小节，共 **12 个小节**。

| 一级 | 二级 |
|------|------|
| 6.1 文本格式 | 6.1.1 分块读；6.1.2 写入；6.1.3 其他分隔符；6.1.4 JSON；6.1.5 HTML/XML |
| 6.2 二进制格式 | 6.2.1 Excel；6.2.2 HDF5 |
| 6.3 Web API | — |
| 6.4 数据库 | SQLAlchemy + `read_sql` |
| 6.5 总结 | — |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [06_01_读写文本格式](./sections/06_01_读写文本格式.md) | 读写文本格式 |
| [06_01_01_逐块读取](./sections/06_01_01_逐块读取.md) | 01 逐块读取 |
| [06_01_02_写入文本](./sections/06_01_02_写入文本.md) | 02 写入文本 |
| [06_01_03_其他分隔符](./sections/06_01_03_其他分隔符.md) | 03 其他分隔符 |
| [06_01_04_JSON](./sections/06_01_04_JSON.md) | 04 JSON |
| [06_01_05_HTML_XML](./sections/06_01_05_HTML_XML.md) | 05 HTML XML |
| [06_02_二进制格式](./sections/06_02_二进制格式.md) | 二进制格式 |
| [06_02_01_Excel](./sections/06_02_01_Excel.md) | 01 Excel |
| [06_02_02_HDF5](./sections/06_02_02_HDF5.md) | 02 HDF5 |
| [06_03_Web_API](./sections/06_03_Web_API.md) | Web API |
| [06_04_数据库](./sections/06_04_数据库.md) | 数据库 |
| [06_05_总结](./sections/06_05_总结.md) | 总结 |

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 读 CSV | `pd.read_csv(path, parse_dates=[...], na_values=...)` |
| 分块 | `for chunk in pd.read_csv(path, chunksize=10000):` |
| 写 CSV | `df.to_csv(path, index=False, na_rep="NULL")` |
| JSON | `pd.read_json`, `df.to_json` |
| Excel | `pd.read_excel`, `df.to_excel(..., sheet_name=...)` |
| SQL | `pd.read_sql("SELECT ...", engine)` |
| API | `requests.get(url).json()` → `pd.DataFrame(data)` |

---

## 三、通用基础示例

见 [`./code/chapter06_data_io_demo.py`](./code/chapter06_data_io_demo.py)（CSV 分块、JSON、写出；Excel/SQL 见脚本内注释）。

---

## 四、【量化专属改造】金融实战衔接

1. **行情 CSV**：`read_csv` + `parse_dates=["date"]` + `index_col="date"`；`na_values` 处理 `--`、停牌标记。
2. **超大 tick/逐笔**：`chunksize` 逐块过滤、聚合，再 `pd.concat` 或落盘 parquet。
3. **因子表 / 财务表**：`read_excel` 多 sheet；注意 `index_col` 与列名中文映射。
4. **聚宽/Tushare API**：JSON → DataFrame，与 6.3 同构；务必 `raise_for_status` 与字段校验。
5. **本地因子库**：生产环境更常用 **Parquet/Feather**（比 CSV 快）；HDF5 适合历史矩阵「一次写多次读」。
6. **数据库**：Wind/内部 MySQL 用 `read_sql` 拉面板数据，注意 SQL 只 SELECT 需要的列以省内存。

---

## 五、与 statsmodels 建模的衔接要点

- 建模前 I/O 阶段就要固定：**样本区间、股票池、复权方式、缺失规则**（写进数据字典或 README）。
- `read_csv` 后立刻 `df.dtypes`、`df.isna().sum()`，避免字符串因子误入 OLS。
- 从 SQL 拉训练集时，在 SQL 层做 `WHERE date BETWEEN ...` 比全表进 pandas 再筛更省资源。

---

## 本章自检清单

- [ ] 会用 `read_csv` 的 `parse_dates`、`na_values`、`index_col`  
- [ ] 会用 `chunksize` 处理大文件  
- [ ] 会用 `to_csv` 控制 `index`/`na_rep`  
- [ ] 知道 Excel 需安装 `openpyxl`  
- [ ] 知道 HDF5 不宜多进程并发写  
- [ ] 能描述 API JSON → DataFrame 的路径  

---

## 后续扩展留白

### 6.1～6.4

（留白）
