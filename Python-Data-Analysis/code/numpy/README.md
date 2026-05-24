# NumPy 学习笔记

NumPy 是 Python 科学计算的基础库，提供高性能的多维数组对象和数值计算工具。

**原书第 4 章总笔记**（章节脉络 + 与本目录文件对照表）：[`../../docs/chapter04_numpy_basics_arrays_vectorization.md`](../../docs/chapter04_numpy_basics_arrays_vectorization.md)  
**第 4 章一页综合演示**：[`../chapter04_numpy_basics_demo.py`](../chapter04_numpy_basics_demo.py)

## 目录结构

| 文件 | 说明 |
|------|------|
| 01_create_ndarray.py | 基础：数组创建 |
| 02.ndarray元素统一.py | 元素类型 |
| 02_numpy_data_types.py | 数据类型：float32/64 等 |
| 03_ndarray_indexing_slicing.py | 核心：索引与切片 |
| 04.ndarray读写.py | 读写、索引、切片 |
| 04_ndarray_shape_operations.py | reshape/flatten：形状操作 |
| 05_ndarray_basic_operations.md | 基本运算（加减乘除、点积等） |
| 06_concatenate_ndarrays.py | 数组拼接：concatenate |
| 07_split_ndarrays.md | 数组拆分：split |
| 08_broadcasting_mechanism.md | 广播机制 |
| 09_ndarray_aggregation_functions.md | 聚合函数：sum/mean/std 等 |
| 10_numpy_search_sort.md | 查找与排序：argsort/argmax 等 |
| 11_numpy_math_arithmetic_functions.md | 数学与算术函数：log/exp/where 等 |
| 12_ndarray_append_insert.md | append/insert（了解性能坑点） |
| 13_ndarray_delete_flatten_reshape.md | delete/flatten/reshape/flip |
| 14_numpy_routines.py | routines：随机数/矩阵生成等 |
| 15_numpy_routines_practice.py | routines 练习 |
| 16_numpy_nan_missing_value.py | 缺失值全套处理（量化必用） |
| 17_numpy_random_module.py | 随机数与随机模拟（复现/采样/蒙特卡洛） |
| 18_numpy_mask_boolean_index.py | 布尔掩码高级筛选（批量过滤/信号生成） |
| 19_numpy_matrix_linear_algebra.md | 线性代数极简入门（ML 打底） |
| 20_numpy_performance_tips.md | 性能避坑与最佳实践（视图/拷贝/TopK） |
| numpy查找排序.md | （旧名）已重命名为 10_numpy_search_sort.md |

## 量化实用优先级（推荐学习顺序）

1. `01_create_ndarray.py`
2. `02_numpy_data_types.py`、`02.ndarray元素统一.py`
3. `03_ndarray_indexing_slicing.py`、`04_ndarray_shape_operations.py`
4. `05_ndarray_basic_operations.md`、`08_broadcasting_mechanism.md`
5. `09_ndarray_aggregation_functions.md`、`11_numpy_math_arithmetic_functions.md`
6. `10_numpy_search_sort.md`（选股/因子排序常用）
7. `06_concatenate_ndarrays.py`、`07_split_ndarrays.md`
8. `12_ndarray_append_insert.md`、`13_ndarray_delete_flatten_reshape.md`（了解即可）
9. `16_numpy_nan_missing_value.py`（真实行情缺失必修）
10. `17_numpy_random_module.py`（模拟/复现/鲁棒性）
11. `18_numpy_mask_boolean_index.py`（信号与过滤核心）
12. `19_numpy_matrix_linear_algebra.md`（ML/回归/矩阵思维）
13. `20_numpy_performance_tips.md`（通读避坑）

## NumPy 完整体系补充说明

### 本次新增补充核心定位

原有目录已经覆盖 90% 通用基础，本次补充全部为 **量化交易 + 机器学习专属刚需短板**。

### 补充模块价值

1. 缺失值处理：真实行情数据清洗必备，杜绝回测失真
2. 随机数模块：模拟交易、策略验证、机器学习实验基础
3. 高级布尔索引：批量信号生成、异常数据过滤核心利器
4. 极简线性代数：轻松看懂机器学习底层逻辑
5. 性能最佳实践：避开新手常见坑，写出高效稳定代码

### 最终学习优先级

1. 吃透原有 01~13 基础核心
2. 优先学新增 16、17（量化日常天天用）
3. 再学 18、19（进阶信号 + 机器学习铺垫）
4. 最后通读 20 避坑总结

### 最终达成效果

学完全部内容后，NumPy 能力完全满足：

- 量化策略开发、批量回测
- Pandas 深度底层理解
- Sklearn 全系列机器学习入门

## 学习资源

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [NumPy 快速入门](https://numpy.org/doc/stable/user/quickstart.html)
