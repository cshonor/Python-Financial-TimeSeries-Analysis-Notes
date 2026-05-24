# 第 6 章 数据加载、存储与文件格式

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 6 章。  
> **数据 I/O** 是分析全流程的入口与出口：把 CSV、Excel、JSON、数据库、Web API 等来源的数据载入 pandas，或将结果写回磁盘。

**前置**：[第 5 章 pandas 入门](./chapter05_pandas_introduction.md)。

**本章演示脚本**：[`../code/chapter06_data_io_demo.py`](../code/chapter06_data_io_demo.py)

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

## 一、书本原文核心知识点提炼

### 6.1 读写文本格式

- **核心函数**：`read_csv`（最常用）、`read_table`、`read_json`、`read_parquet` 等。
- **参数大类**：`index_col` / `header` / `names`；`dtype` / `na_values`；`parse_dates`；`chunksize` / `nrows`；`skiprows` 等。
- **`sep`**：可为正则，如 `sep=r"\s+"` 处理不定长空白分隔。
- **缺失值**：默认识别 `NA`、`NULL` 等；`na_values` 自定义；`keep_default_na=False` 关闭默认推断。

#### 6.1.1 逐块读取

- `nrows`：只读前若干行预览。
- `chunksize`：返回 `TextFileReader` 迭代器，for 循环逐块聚合，省内存。

#### 6.1.2 写入文本

- `df.to_csv`：`sep`、`na_rep`、`index=False`、`columns=[...]`。

#### 6.1.3 其他分隔符

- 极不规则文件：`csv.reader` + 自定义 `Dialect`；实在不行用 `split` / `re.split` 手工清洗。

#### 6.1.4 JSON

- `json.loads` / `json.dumps`；pandas：`read_json` / `to_json`。

#### 6.1.5 HTML/XML

- `read_html` 解析网页 `<table>`，返回 **DataFrame 列表**。

### 6.2 二进制格式

#### 6.2.1 Excel

- 依赖 `openpyxl`（xlsx）、`xlrd`（旧 xls）。
- `ExcelFile` + `parse` 或 `read_excel`；写出：`ExcelWriter` + `to_excel`。
- 指定 `index_col` 设索引列。

#### 6.2.2 HDF5

- 大型数组分层存储；pandas `HDFStore`；支持压缩与局部读取。
- **不是数据库**；适合一次写、多次读；**多进程并发写易损坏文件**。

### 6.3 Web API

- 推荐 `requests.get` + `raise_for_status()`。
- `resp.json()` → `pd.DataFrame(...)` 构造规整表。

### 6.4 数据库

- `SQLAlchemy` 引擎 + **`pd.read_sql(sql, engine)`** 直接得带列名的 DataFrame。

### 6.5 总结

- I/O 完成后进入数据规整、可视化、时序等章节。

---

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

见 [`../code/chapter06_data_io_demo.py`](../code/chapter06_data_io_demo.py)（CSV 分块、JSON、写出；Excel/SQL 见脚本内注释）。

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
