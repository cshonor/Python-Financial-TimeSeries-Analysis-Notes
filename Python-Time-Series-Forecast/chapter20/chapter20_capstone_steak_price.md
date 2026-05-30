# 第 20 章 顶点项目：预测加拿大牛排的月平均零售价格

> 对应教材：**《Python 时间序列预测》** 第 20 章 · **全书收官顶点**。  
> 综合 **基线 / Prophet / SARIMA**：加拿大统计局 **1kg 圆形牛排** 月均价（约 323 行）。数据**强趋势、弱季节** → **Prophet 惨败**（MAE **1.163**）不如**末值基线**（**0.681**）；**SARIMA(2,1,3)(1,0,1)₁₂** 略胜（**0.678**）但提升极小 → 需**外生变量**与领域知识。

**前置**：[第 11 章 统计顶点](./chapter11_capstone_aus_drugs.md)、[第 19 章 Prophet](./chapter19_prophet.md)

**演示脚本**：[`./code/chapter20_capstone_steak_demo.py`](./code/chapter20_capstone_steak_demo.py)

**下一章**：[第 21 章 全书总结](./chapter21_beyond_self_summary.md)

---

## 章节总览

| 小节 | 主题 |
|------|------|
| 20.1 | 业务目标与路线图 |
| 20.2 | 清洗、可视化、弱季节洞察 |
| 20.3 | Prophet 失败案例 |
| 20.4 | SARIMA 对照 |
| 20.5 | 复盘与开放数据 |

---

## 一、书本原文核心知识点提炼

### 20.1 了解顶点项目

- **数据**：Statistics Canada，52 品项 → **Round steak, 1 kilogram**，1995 年起月均价。  
- **目标**：预测未来 **36 个月**。  
- **路线**：清洗 → `ds`/`y` → 月末日期 → Prophet CV/调参 → 测试 MAE vs 基线 → **SARIMA** 对照。

**【个人扩展与补充】**  
<br><br><br><br>

### 20.2 数据预处理与可视化

- 过滤商品行，保留 `REF_DATE` + `VALUE`（约 **323** 行）。  
- **洞察**：明显**上升趋势**，**无明显季节** → Prophet 可能不适配。

**【个人扩展与补充】**  
<br><br><br><br>

### 20.3 使用 Prophet 建模

- `MonthEnd(1)` 对齐月末；**不**加假日（无业务季节）。  
- 调参 `changepoint_prior_scale`、`seasonality_prior_scale`。  
- **基线**：训练集**最后一个月**平推 36 月 → MAE **0.681**。  
- **Prophet** → MAE **1.163**（**差于基线**）。  
- **原因**：高 `changepoint_prior_scale`（如 **1.0**）过拟合拐点；强行拟合“每年 9 月下跌”等**虚假年季节** → 超调。

**【个人扩展与补充】**  
<br><br><br><br>

### 20.4 可选：SARIMA 模型

- **ADF**：水平 **p=0.98**；一阶差分 **d=1** 平稳；**D=0**, **m=12**。  
- **AIC 最优**：**SARIMA(2,1,3)(1,0,1)₁₂**；残差诊断 + Ljung-Box 通过。  
- **MAE = 0.678**：略优于基线 **0.681**，远优于 Prophet；**单变量提升有限** → 需饲料价、通胀等 **X**。

**【个人扩展与补充】**  
<br><br><br><br>

### 20.5 下一步

- **无银弹**：领域知识 + 外生特征 + 创造性。  
- 练习：其余 51 商品、改预测跨度。  
- 数据源：NYC Open Data、Statistics Canada、Papers with Code。

**【个人扩展与补充】**  
<br><br><br><br>

---

## 二、关键语法速查表

| 场景 | 做法 |
|------|------|
| 过滤商品 | `df[df['Products'] == 'Round steak, 1 kilogram']` |
| 弱季节 Prophet | 可关 `yearly_seasonality=False` 做对照实验 |
| 趋势基线 | `yhat = train['y'].iloc[-1]` |
| SARIMA | `d=1`, `D=0`, 网格 AIC |

---

## 三、演示脚本

见 [`./code/chapter20_capstone_steak_demo.py`](./code/chapter20_capstone_steak_demo.py)

---

## 四、【量化专属改造】

| 场景 | 做法 |
|------|------|
| CPI 商品 | 同流程 + 宏观外生 |
| Prophet 失败 | 换 SARIMAX/DL 或关季节项 |
| 投产 | 残差白噪声 + 业务可解释性 |

---

## 五、全书自检（收官）

- [ ] 能解释本章 Prophet 为何输给基线  
- [ ] 会在无季节数据上谨慎使用 Prophet  
- [ ] 知道 SARIMA 略优但需外生变量突破  
- [ ] 掌握「工具箱 + 对照实验」思维  

---

## 个人扩展与补充留白

（全书收官留白）
