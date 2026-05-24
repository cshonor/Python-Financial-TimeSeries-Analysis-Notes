# 第 9 章 绘图和可视化

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 9 章。  
> 可视化用于探索异常、启发变换、构思模型，也是汇报结果的最终手段。本章覆盖 **`matplotlib` 底层 API**、**pandas 内置绘图**、**seaborn** 统计图，并简要介绍其他可视化库。

**前置**：[第 8 章 数据规整](./chapter08_data_wrangling_join_reshape.md) → 本章 → [第 10 章 数据聚合与分组](./chapter10_data_aggregation_groupby.md)。

**本仓库专题深化**：[`../code/matplotlib/`](../code/matplotlib/)（子图、中文、柱状图、散点图、保存图片等）

**演示脚本**：[`../code/chapter09_plotting_demo.py`](../code/chapter09_plotting_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 11 个二级小节，共 **15 个小节**。

| 一级 | 二级 |
|------|------|
| 9.1 matplotlib API | 9.1.1～9.1.6 |
| 9.2 pandas / seaborn | 9.2.1～9.2.5 |
| 9.3 其他工具 | — |
| 9.4 总结 | — |

---

## 一、书本原文核心知识点提炼

### 9.1 matplotlib API 入门

- 惯例：`import matplotlib.pyplot as plt`。
- Jupyter：`%matplotlib inline` 或 `%matplotlib notebook`。
- 高级定制需掌握底层 API，不能只会封装库。

#### 9.1.1 图和子图

- 图在 **`Figure`** 中：`plt.figure(figsize=...)`。
- 空 Figure 不能直接画，需 **`fig.add_subplot(nrows, ncols, index)`** 得到 **Axes**。
- Jupyter 中同一图的命令宜放在**同一单元格**（否则图形被重置）。
- 推荐 **`fig, axes = plt.subplots(nrows, ncols, sharex=, sharey=)`**。
- **`fig.subplots_adjust(wspace=, hspace=)`** 调节子图间距。

#### 9.1.2 颜色、标记和线型

- `plot(x, y, color=, linestyle=, marker=)`；可用十六进制色。
- **`drawstyle="steps-post"`** 阶梯线（无插值）。
- 传了 `label` 仍需 **`ax.legend()`** 才显示图例。

#### 9.1.3 刻度、标签和图例

- 无参调用如 `ax.xlim()` 为**读取**；传参为**设置**。
- **`set_xticks` / `set_xticklabels`**（`rotation` 防重叠）。
- **`ax.set(title=..., xlabel=..., ylabel=...)`** 批量设置。
- **`ax.legend(loc="best"|"upper left"|...)`**。

#### 9.1.4 注释和绘制子图

- **`ax.text`**、**`ax.annotate`**（带箭头标注数据点）。
- **`matplotlib.patches`**：`Rectangle`、`Circle` 等 → **`ax.add_patch()`**。

#### 9.1.5 保存图表

- **`fig.savefig("path.png")`**；扩展名决定格式（pdf/svg/png）。
- **`dpi=400`** 控制分辨率（出版/汇报）。

#### 9.1.6 matplotlib 配置

- **`plt.rc("figure", figsize=(10, 10))`** 等全局默认。
- 用户目录 **`.matplotlibrc`** 持久化样式。

### 9.2 使用 pandas 和 seaborn 绘图

#### 9.2.1 线形图

- **`Series/DataFrame.plot()`** 默认折线图；索引作 x 轴（`use_index=False` 可关）。
- DataFrame 每列一条线，列名作图例；可传 **`ax=`** 嵌入已有子图网格。

#### 9.2.2 柱状图

- **`plot.bar()`** / **`plot.barh()`**；DataFrame 多列并排；**`stacked=True`** 堆积柱。
- 常与 **`value_counts()`**、**`pd.crosstab()`** 联用。
- **`sns.barplot`** 可带均值与 95% 置信区间误差条。

#### 9.2.3 直方图和密度图

- **`plot.hist(bins=50)`**；**`plot.density()`** KDE（依赖 SciPy）。
- **`sns.histplot`** 可同时叠直方图与密度曲线。

#### 9.2.4 散点图或点图

- **`sns.regplot`**：散点 + 线性回归线 + 置信带。
- **`sns.pairplot`**：多变量两两散点矩阵，对角线为单变量分布。

#### 9.2.5 分面网格和分类数据

- **FacetGrid**：按类别拆成子图矩阵。
- **`sns.catplot(col=, row=, kind="box"|"bar"|...)`** 简化分面；`kind="box"` 为箱线图。

### 9.3 其他 Python 可视化工具

- 静态出版/报告：**matplotlib** + **pandas/seaborn**。
- 浏览器交互：**Altair**、**Bokeh**、**Plotly** 等。

### 9.4 总结

- 下一章：[第 10 章 数据聚合与分组操作](./chapter10_data_aggregation_groupby.md)。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 创建子图 | `fig, ax = plt.subplots(2, 2)` |
| 画线 | `ax.plot(x, y, label="...")` |
| 图例/标题 | `ax.legend()`, `ax.set(title=...)` |
| 保存 | `fig.savefig("out.png", dpi=150, bbox_inches="tight")` |
| 全局样式 | `plt.rc("font", size=12)` |
| pandas 折线 | `df.plot(ax=ax)` |
| 柱状图 | `df.plot.bar()`, `df.plot.barh(stacked=True)` |
| 直方图 | `s.plot.hist(bins=30)` |
| seaborn 回归散点 | `sns.regplot(data=df, x="x", y="y")` |
| 分面 | `sns.catplot(data=df, x="ind", y="ret", col="year")` |

---

## 三、通用基础示例

见 [`../code/chapter09_plotting_demo.py`](../code/chapter09_plotting_demo.py)

专题练习见 [`../code/matplotlib/README.md`](../code/matplotlib/README.md)

---

## 四、【量化专属改造】金融实战衔接

1. **价格/净值曲线**：`close.plot()` 或 `ax.plot(dates, nav)`；多标的同图对比需对齐交易日（第 8 章 merge 后再画）。
2. **收益率分布**：`ret.plot.hist(bins=50)` + `plot.density()` 看厚尾；极端值是否与第 7 章 clip 规则一致。
3. **因子分层柱状图**：`groupby` 分位后 `mean().plot.bar()`；行业用 `crosstab` + `bar`。
4. **散点：因子 vs 收益**：`sns.regplot` 看单调性；注意横轴为当期因子、纵轴为**下期**收益时才有预测含义。
5. **滚动指标双子图**：`subplots(2, 1, sharex=True)` 上价格下成交量或 MACD。
6. **回测净值图**：阶梯线 `drawstyle="steps-post"` 适合 discrete 调仓点；标注最大回撤区间可用 `annotate`。
7. **中文标签**：本仓库 [`code/matplotlib/04_matplotlib处理图形中的中文.md`](../code/matplotlib/04_matplotlib处理图形中的中文.md) 配置字体。
8. **报告导出**：`savefig(..., dpi=300, bbox_inches="tight")` 插入研报/PPT。

---

## 五、与 statsmodels 建模的衔接要点

- 探索阶段：残差图 `sns.residplot`、QQ 图、拟合线 `regplot` 检查线性假设与异方差。
- 不要仅凭散点“肉眼显著”下结论；与回归表（第 10 章+ statsmodels）对照。
- 分类变量可视化后，建模仍用 `get_dummies` / 公式接口，避免把图例类别顺序误当有序变量。
- 时间序列图注意 **x 轴为日期** 时使用 `plot` 索引或 `matplotlib.dates` 格式化，避免字符串轴导致间距错误。

---

## 本章自检清单

- [ ] 会用 `subplots` 与 `ax.plot` / `legend`  
- [ ] 会 `savefig` 与 `dpi`  
- [ ] 会用 `DataFrame.plot()`、`plot.bar`、`plot.hist`  
- [ ] 了解 `seaborn` 的 `regplot`、`histplot`、`catplot`  
- [ ] 知道静态图与 Plotly 等交互库的分工  

---

## 后续扩展留白

### 9.1～9.3

（留白）
