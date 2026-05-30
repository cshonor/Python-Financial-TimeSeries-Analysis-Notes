# 第 13 章 数据窗口和创建深度学习基线

> 对应教材：**《Python 时间序列预测》** 第 13 章。  
> 深度学习必须把序列切成 **输入 (Inputs)** 与 **标签 (Labels)**。本章实现可复用的 **`DataWindow`**（基于 `timeseries_dataset_from_array` 或 NumPy 回退），并为 **单步 / 多步 / 多输出** 三种形态建立 **Baseline**，作为后续 DNN、CNN、LSTM 的底线标尺。统一 **MSE 损失**、**MAE 评估**。

**前置**：[第 12 章 预处理](./chapter12_deep_learning_intro.md)（缩放特征矩阵）

**下一章**：[第 14 章 线性模型与 DNN](./chapter14_linear_and_dnn.md)

**演示脚本**：[`./code/chapter13_data_window_baseline_demo.py`](./code/chapter13_data_window_baseline_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 13.1（2 子节）+ 13.2（3 子节）+ 小结，共 **10 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 13.1 | 窗口概念与 `DataWindow` |
| 13.2 | 单步 / 多步 / 多输出基线 |
| 13.3 | 引出第 14 章 |
| 13.4 | 练习与小结 |

---

## 一、书本原文核心知识点提炼

### 13.1 创建数据窗口

**13.1.1 训练逻辑与窗口**

- **统计 vs DL**：SARIMAX 拟合固定形式参数；神经网络从 **输入→标签** 学映射。  
- **窗口**：例如输入过去 24h、标签未来 24h → 总长度 48 步。  
- **滚动**：步长 1 平移起点，最大化样本数。  
- **批次**：如 Batch=32；**窗口内部**时间顺序不可打乱，**窗口之间**宜 `shuffle` 防过拟合。

**13.1.2 `DataWindow` 类**

| 参数 | 含义 |
|------|------|
| **input_width** | 输入历史步数 |
| **label_width** | 预测步数 |
| **shift** | 输入起点到标签起点间隔；紧邻未来时常 **shift = label_width** |

- 实现：`tf.keras.preprocessing.timeseries_dataset_from_array` + slice 分输入/标签。  
- 内置 `plot` 审查窗口。

**【个人扩展与补充】**  
<br><br><br><br>

### 13.2 应用基线模型

- **损失**：**MSE**（大误差惩罚更重，利于优化）。  
- **评估**：**MAE**（业务可读）。

**13.2.1 单步基线**

- `input_width=1, label_width=1, shift=1`；预测下一时刻流量。  
- **规则**：输出 = 输入最后一个已知值。  
- 书中验证集 **MAE ≈ 0.081**（缩放后尺度）。

**13.2.2 多步基线**

- `24 / 24 / 24`：用 24h 历史预测未来 24h。  
- **重复末值**：第 24 点复制 24 次 → MAE **≈ 0.347**（差）。  
- **重复整段输入序列**：利用日季节 → MAE **≈ 0.341**（更优）。

**13.2.3 多输出基线**

- 输入 1 步，同时预测 **流量 + 温度**（下一步）。  
- **规则**：返回输入中两目标最后已知值。  
- **MAE ≈ 0.047**。

**【个人扩展与补充】**  
<br><br><br><br>

### 13.3 下一步 & 13.4 练习小结

- 基线无需训练；第 14 章挂载 **线性层 + DNN**，须击败本章 MAE。  
- **小结**  
  1. 张量化前必须做 **数据窗口**。  
  2. `DataWindow` 可复用于单步/多步/多输出。  
  3. **MSE 优化 + MAE 汇报**。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| TF 窗口 | `timeseries_dataset_from_array(..., sequence_length=shift+label_width)` |
| 切片 | `inputs = w[:input_width]`；`labels = w[shift:shift+label_width]` |
| 打乱 | `shuffle=True`（仅窗口级） |
| 基线 | 末值 / 重复序列 / 多列末值 |

---

## 三、演示脚本

见 [`./code/chapter13_data_window_baseline_demo.py`](./code/chapter13_data_window_baseline_demo.py)

依赖：`numpy`；可选 `tensorflow`（未安装时用 NumPy 窗口）。

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| 日频收益 | `input_width=20` 预测 `label_width=1` |
| 多标的 | `label_indices` 多列；多输出头 |
| 防泄漏 | 窗口仅从 train/val 各自数组生成 |
| 回测 | 基线 ≈ 「昨收」「上周同刻」 |

---

## 五、与全书衔接

| 章 | 关系 |
|----|------|
| 2 | 统计基线 vs DL 窗口基线 |
| 12 | 特征矩阵 → 窗口 |
| 14+ | 可训练模型须胜基线 |

---

## 本章自检清单

- [ ] 能解释窗口内不打乱、批次间可打乱  
- [ ] 能说明 input_width / label_width / shift  
- [ ] 能比较多步「重复末值」与「重复序列」  
- [ ] 知道 MSE 与 MAE 的分工  

---

## 个人扩展与补充留白

（章节级留白）
