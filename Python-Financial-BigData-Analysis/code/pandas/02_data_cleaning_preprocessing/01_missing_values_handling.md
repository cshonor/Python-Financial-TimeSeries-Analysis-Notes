# 数据清洗与预处理

> 覆盖：49-pandas数据类型练习 → 60-排序和随机抽样

## 一、pandas 数据类型练习

- 核心数据类型：数值型 `int64`/`float64`、文本型 `object`/`string`、时间型 `datetime64`、类别型 `category`
- 类型转换：`df['col'].astype(type)` / `pd.to_datetime()`

## 二、csv 文件和 txt 文件的读取

- 读取 CSV：`pd.read_csv(path, sep=',', header=0, encoding='utf-8')`
- 读取 TXT：`pd.read_csv(path, sep='\t')`
- 关键参数：`sep` / `header` / `encoding` / `na_values`

## 三、pandas IO 操作

- 写入文件：`df.to_csv(path, index=False)`
- 其他格式：Excel / JSON / SQL 等
- 分块读取：`chunksize` 参数避免内存溢出

## 四、常用数据探索方法

- 描述性统计：`df.describe()`
- 信息概览：`df.info()`
- 唯一值统计：`df['col'].value_counts()`
- 相关性分析：`df.corr()`

## 五、python 空类型和 numpy 空类型

- Python 空值：`None`
- NumPy/Pandas 空值：`np.nan`，判断用 `pd.isna()` / `pd.notna()`

## 六、pandas 空值查找

- 检测：`df.isna()` / `df.isnull()`
- 统计：`df.isna().sum()` / `df.isna().mean() * 100`

## 七、pandas 空值批量填充

- 固定值填充：`df.fillna(value)`
- 统计值填充：`df.fillna(df.mean())` / `median()`
- 前向/后向填充：`ffill` / `bfill`
- 插值填充：`df.interpolate()`

## 八、空值过滤

- 删除行/列：`df.dropna(axis=0/1)`
- 阈值控制：`df.dropna(thresh=n)`

## 九、异常值处理

- 检测：分位数法、标准差法
- 处理：删除、截断 `clip()`、替换

## 十、离群点检测和过滤

- 箱线图：`df.boxplot()` 直观识别
- 处理原则：结合业务判断，避免盲目删除

## 十一、重复值处理

- 检测：`df.duplicated()`
- 删除：`df.drop_duplicates(keep='first', subset=['col1', 'col2'])`

## 十二、排序和随机抽样

- 排序：`df.sort_values(by='col')` / `df.sort_index()`
- 抽样：`df.sample(n=100)` / `df.sample(frac=0.1)`，`random_state=42` 可复现
