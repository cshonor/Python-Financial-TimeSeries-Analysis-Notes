# 12.1 statsmodels 与 scikit-learn：量化分工

> 所属：[第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md) · 《利用 Python 进行数据分析》

原书第 12 章同时涉及 **statsmodels**（推断）与 **scikit-learn**（预测）。量化场景下两者分工明确，宜**配合使用**而非二选一。

---

## 一、核心区别（背诵）

| 库 | 侧重 | 量化回答的问题 |
|----|------|----------------|
| **statsmodels** | 统计推断 | 因子有没有解释力？逻辑成不成立？ |
| **scikit-learn** | 机器学习预测 | 下一期能不能预测准？信号能不能用？ |

---

## 二、量化分工速览

**statsmodels**：截面/时序 OLS、Logit、协整检验、异方差/序列相关诊断、面板回归 → **因子筛选与归因**。

**sklearn**：标准化、特征选择、Ridge/Lasso/随机森林、滚动时序训练 → **预测与信号生成**。

---

## 三、推荐落地流程

```
数据清洗 → statsmodels 因子检验 → sklearn 滚动预测 → 回测迭代
```

**原则**：先 statsmodels **统计把关**，再 sklearn **机器学习预测**；避免无根因子直接进黑盒模型。

---

## 四、完整专题笔记

详细案例（多因子选股、涨跌分类、配对交易）、语法速查、避坑清单见：

**[`../../code/statsmodels/statsmodels_vs_sklearn_quant.md`](../../code/statsmodels/statsmodels_vs_sklearn_quant.md)**

---

## 五、自检

- [ ] 能说出两库在因子研究 vs 预测交易阶段的分工  
- [ ] 能复述「先推断后预测」四步流程  

---

[← 返回第 12 章](../chapter12_modeling_libraries_patsy_statsmodels.md)
