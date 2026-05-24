# DataFrame 核心操作与数据访问

> 覆盖：33-DataFrame的基础构造方法 → 42-pandas高级查找

## 一、DataFrame 的基础构造方法

- 从字典创建：`pd.DataFrame(dict)`（键为列名，值为列数据）
- 从列表创建：`pd.DataFrame(list, columns=[...])`
- 从 NumPy 数组创建：`pd.DataFrame(arr, columns=[...], index=[...])`
- 从 Series 列表创建：多个 Series 拼接为列

## 二、DataFrame 的其他构造方法

- 从 CSV/Excel 读取：`pd.read_csv()` / `pd.read_excel()`
- 从字典列表创建：每行对应一个字典，自动对齐列
- 空 DataFrame 构造：`pd.DataFrame(columns=[...])`（用于后续填充）

## 三、DataFrame 的重要属性

- `index` / `columns`：行/列索引对象
- `shape`：(行数, 列数)
- `dtypes`：每列数据类型
- `T`：转置（行变列、列变行）
- `head(n)` / `tail(n)`：查看前/后 n 行数据

## 四、DataFrame 运算（一）

- 列级运算：按列执行（如 `df['col'] * 2`）
- 行级运算：通过 `axis` 参数控制（`axis=0` 列方向，`axis=1` 行方向）
- 广播机制：与标量/同维度数组运算自动对齐

## 五、DataFrame 运算（二）

- 与 NumPy 函数兼容：`np.sqrt(df)` / `np.exp(df)`
- 缺失值处理：运算中 `NaN` 自动传播，可通过 `skipna=True` 忽略
- 自定义函数：`df.apply(func)` 逐行/逐列应用函数

## 六、pandas 对象的显式访问和隐式访问

- 显式访问：`df['col_name']` / `df[['col1', 'col2']]`（推荐，避免歧义）
- 隐式访问：`df.col_name`（仅适用于列名无空格/特殊字符）
- 注意：隐式访问可能与属性名冲突，生产环境慎用

## 七、pandas 对象的 loc 访问详解

- `loc`：基于**标签**的索引（行标签、列标签）
- 语法：`df.loc[row_label, col_label]`
- 支持切片：`df.loc['a':'c', 'x':'z']`（包含两端）
- 支持布尔索引：`df.loc[df['age'] > 18, :]`

## 八、pandas 对象的 iloc 访问详解

- `iloc`：基于**位置**的索引（整数位置，从 0 开始）
- 语法：`df.iloc[row_pos, col_pos]`
- 支持切片：`df.iloc[0:3, 1:4]`（左闭右开）
- 与 NumPy 索引逻辑一致

## 九、pandas 对象访问的注意事项

- 链式索引问题：`df['col']['row']` 可能返回副本，避免赋值
- 赋值安全写法：`df.loc[row, col] = value` / `df.iloc[row, col] = value`
- 索引类型：避免混合整数与字符串索引，减少歧义

## 十、pandas 高级查找

- 条件筛选：`df[df['col'] > threshold]`（布尔索引）
- 多条件组合：`&`（且）/ `|`（或）/ `~`（非），需加括号
- 字符串匹配：`df[df['col'].str.contains('keyword')]`
- 范围查找：`df[df['col'].between(left, right)]`
