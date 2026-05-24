# Pandas 基础与核心对象

> 覆盖：27-Pandas简介 → 32-DataFrame结构理解

## 一、Pandas 简介

- Pandas 定位：Python 数据分析核心库，基于 NumPy 构建
- 核心优势：处理表格型数据、缺失值、时间序列更高效
- 与 NumPy 的区别：支持标签索引、混合数据类型、更丰富的操作

## 二、Series 对象的基本构造及注意事项

- Series 本质：带标签的一维数组
- 构造方式：`pd.Series(data, index=...)`
- 注意事项：
  - 索引与数据长度必须一致
  - 数据类型自动推断，可手动指定 `dtype`
  - 缺失值默认用 `NaN` 表示

## 三、Series 高级构造函数

- 从字典创建：`pd.Series(dict)`（键自动作为索引）
- 从标量创建：`pd.Series(5, index=[...])`（广播填充）
- 从 NumPy 数组创建：保留数组数据类型与结构

## 四、Series 的重要属性

- `values`：底层 NumPy 数组
- `index`：索引对象（`pd.Index`）
- `shape` / `size` / `dtype`：形状、元素个数、数据类型
- `name`：Series 名称，可用于 DataFrame 列名

## 五、Series 的运算

- 与标量运算：逐元素执行（如 `s + 2`）
- 与同长度 Series 运算：按索引对齐，缺失值自动传播
- 常用统计方法：`sum()` / `mean()` / `max()` / `min()` / `std()`

## 六、DataFrame 结构理解

- DataFrame 本质：带标签的二维表格，由多个 Series 共享同一索引
- 核心组成：
  - 行索引（`index`）：对应每行的标签
  - 列索引（`columns`）：对应每列的标签
  - 数据（`values`）：二维 NumPy 数组
- 直观类比：Excel 工作表 / SQL 表
