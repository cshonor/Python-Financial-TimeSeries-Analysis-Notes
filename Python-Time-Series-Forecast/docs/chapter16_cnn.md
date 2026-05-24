# 第 16 章 使用 CNN 过滤时间序列

> 对应教材：**《Python 时间序列预测》** 第 16 章。  
> 在 [第 15 章 LSTM](./chapter15_lstm.md) 之后，本章引入 **卷积神经网络（CNN）**：**抗噪**、**训练快于 LSTM**、通过 **Conv1D** 与 **核（Kernel）** 提取局部时序特征。演示纯 **CNN** 与 **CNN+LSTM** 在单步 / 多步 / 多输出上的 MAE 对比。

**前置**：第 12～15 章（`DataWindow`、LSTM）

**下一章**：[第 17 章 ARLSTM](./chapter17_arlstm.md)（自回归逐步预测）

**演示脚本**：[`../code/chapter16_cnn_demo.py`](../code/chapter16_cnn_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 16.2 含 3 子节 + 小结，共 **8 个逻辑小节**。

| 小节 | 主题 |
|------|------|
| 16.1 | 卷积、核、输出长度公式、Padding |
| 16.2 | 单步 / 多步 / 多输出 CNN 与 CNN+LSTM |
| 16.3 | CNN 是工具箱之一 → ARLSTM |
| 16.4 | 练习与小结 |

---

## 一、书本原文核心知识点提炼

### 16.1 研究卷积神经网络

- **卷积**：输入与 **核（Filter）** 沿时间轴滑动做点积，得到简化特征。  
- **作用**：滤噪、正则化、防过拟合。  
- **输出长度**（无 padding）：  
  \[
  L_{\text{out}} = L_{\text{in}} - L_{\text{kernel}} + 1
  \]
- **1D 时序**：`tf.keras.layers.Conv1D`。  
- **Padding**：两端补 0（常 `padding='same'`），使 \(L_{\text{out}}=L_{\text{in}}\)，可堆叠更多层。

**【个人扩展与补充】**  
<br><br><br><br>

### 16.2 实现 CNN

**开窗公式**（书中）：  
\[
L_{\text{input}} = L_{\text{label}} + L_{\text{kernel}} - 1
\]
设 `KERNEL_WIDTH = 3`。

**16.2.1 单步**

- 输入长度 **3**（\(1+3-1\)），`label_width=1`，`shift=3`。  
- `Conv1D` → `Dense` → 输出 1。  
- **结论**：纯 CNN 未优于 LSTM；CNN+LSTM 亦未必更好 — **输入仅 3 点过短**，卷积难以提取有效模式。

**16.2.2 多步**

- 预测 **24** 步 → 输入 **26**（\(24+3-1\)），`shift=26`。  
- **结论**：纯 CNN < LSTM；**CNN+LSTM 多步 MAE 最小**，成为多步**新冠军**。

**16.2.3 多输出**

- 输入 **24**，预测下一步流量 + 温度。  
- **结论**：CNN、CNN+LSTM、LSTM **MAE 相同** — CNN 未必带来增益。

**【个人扩展与补充】**  
<br><br><br><br>

### 16.3 下一步

- CNN **不总是**最优；须正确开窗 + 统一 MAE 协议。  
- 现有多步为**一次性**输出 24 点；第 17 章 **ARLSTM** 逐步自回归预测。

**【个人扩展与补充】**  
<br><br><br><br>

### 16.4 练习与本章小结

- **练习**：空气质量数据上 CNN vs CNN+LSTM vs 基线/DNN/LSTM。  
- **小结**  
  1. CNN 压缩特征空间、滤噪。  
  2. 时序用 **Conv1D** + 可学习核。  
  3. **Padding** 保持长度、加深网络。  
  4. 坚持开窗公式与基准对比，客观选型。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | 代码 |
|------|------|
| 1D 卷积 | `Conv1D(filters=32, kernel_size=3, padding='same', activation='relu')` |
| 输入长度 | `label_width + kernel_width - 1` |
| CNN+LSTM | `Conv1D` → `LSTM(32, return_sequences=True)` → `Dense` |
| 评估 | 与第 13～15 章相同：MSE 训练、**MAE** 对比 |

---

## 三、演示脚本

见 [`../code/chapter16_cnn_demo.py`](../code/chapter16_cnn_demo.py)

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| 高频噪声 | 先试 CNN 滤噪再 LSTM |
| 长输入 | `padding='same'` + 更大 `kernel_size` |
| 算力 | CNN 训练快，适合大规模调参 |

---

## 五、与全书衔接

| 章 | 关系 |
|----|------|
| 15 | LSTM 序列记忆 |
| 17 | ARLSTM 逐步预测 |
| 13 | `DataWindow` 开窗 |

---

## 本章自检清单

- [ ] 会算 \(L_{\text{out}} = L_{\text{in}} - k + 1\)  
- [ ] 知道 padding 的作用  
- [ ] 会用公式算 CNN 输入长度  
- [ ] 知道多步任务 CNN+LSTM 可能最优 |

---

## 个人扩展与补充留白

（章节级留白）
