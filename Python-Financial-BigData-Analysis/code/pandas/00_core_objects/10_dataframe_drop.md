# 10 删除与清理（drop / dropna / duplicates）
  
量化数据处理里，“删什么、怎么删”很关键：删错一行，信号就可能对不齐；删错一列，特征就可能泄露。
  
## 1. `drop`：按标签删除行/列
  
- 删列：`df.drop(columns=['colA','colB'])`
- 删行：`df.drop(index=[...])`
  
常用参数：
  
- `errors='ignore'`：列不存在也不报错（批量处理中实用）
  
## 2. `dropna`：删除缺失
  
- `df.dropna()`：只要一行里有 NaN 就删（通常太激进）
- `df.dropna(subset=['close'])`：只看关键列
  
## 3. 去重 `drop_duplicates`
  
- `df.drop_duplicates()`：整行去重
- `df.drop_duplicates(subset=['date','code'])`：按关键键去重
  
## 4. 量化建议
  
- 删除前先 `df.isna().sum()`、`df.duplicated().sum()` 看问题规模
- 删除后再检查 index 是否还连续/对齐
  
