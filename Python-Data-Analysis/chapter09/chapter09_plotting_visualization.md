# 第 9 章 绘图和可视化

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 9 章。  
> 可视化用于探索异常、启发变换、构思模型，也是汇报结果的最终手段。本章覆盖 **`matplotlib` 底层 API**、**pandas 内置绘图**、**seaborn** 统计图，并简要介绍其他可视化库。

**前置**：[第 8 章 数据规整](../chapter08/chapter08_data_wrangling_join_reshape.md) → 本章 → [第 10 章 数据聚合与分组](../chapter10/chapter10_data_aggregation_groupby.md)。

**本仓库专题深化**：[`./code/matplotlib/`](./code/matplotlib/)（子图、中文、柱状图、散点图、保存图片等）

**演示脚本**：[`./code/chapter09_plotting_demo.py`](./code/chapter09_plotting_demo.py)

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

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [09_01_matplotlib_API_入门](./sections/09_01_matplotlib_API_入门.md) | matplotlib API 入门 |
| [09_01_01_图和子图](./sections/09_01_01_图和子图.md) | 01 图和子图 |
| [09_01_02_颜色_标记和线型](./sections/09_01_02_颜色_标记和线型.md) | 02 颜色 标记和线型 |
| [09_01_03_刻度_标签和图例](./sections/09_01_03_刻度_标签和图例.md) | 03 刻度 标签和图例 |
| [09_01_04_注释和绘制子图](./sections/09_01_04_注释和绘制子图.md) | 04 注释和绘制子图 |
| [09_01_05_保存图表](./sections/09_01_05_保存图表.md) | 05 保存图表 |
| [09_01_06_matplotlib_配置](./sections/09_01_06_matplotlib_配置.md) | 06 matplotlib 配置 |
| [09_02_使用_pandas_和_seaborn_绘图](./sections/09_02_使用_pandas_和_seaborn_绘图.md) | 使用 pandas 和 seaborn 绘图 |
| [09_02_01_线形图](./sections/09_02_01_线形图.md) | 01 线形图 |
| [09_02_02_柱状图](./sections/09_02_02_柱状图.md) | 02 柱状图 |
| [09_02_03_直方图和密度图](./sections/09_02_03_直方图和密度图.md) | 03 直方图和密度图 |
| [09_02_04_散点图或点图](./sections/09_02_04_散点图或点图.md) | 04 散点图或点图 |
| [09_02_05_分面网格和分类数据](./sections/09_02_05_分面网格和分类数据.md) | 05 分面网格和分类数据 |
| [09_03_其他_Python_可视化工具](./sections/09_03_其他_Python_可视化工具.md) | 其他 Python 可视化工具 |
| [09_04_总结](./sections/09_04_总结.md) | 总结 |

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

见 [`./code/chapter09_plotting_demo.py`](./code/chapter09_plotting_demo.py)

专题练习见 [`./code/matplotlib/README.md`](./code/matplotlib/README.md)

---

## 四、【量化专属改造】金融实战衔接

1. **价格/净值曲线**：`close.plot()` 或 `ax.plot(dates, nav)`；多标的同图对比需对齐交易日（第 8 章 merge 后再画）。
2. **收益率分布**：`ret.plot.hist(bins=50)` + `plot.density()` 看厚尾；极端值是否与第 7 章 clip 规则一致。
3. **因子分层柱状图**：`groupby` 分位后 `mean().plot.bar()`；行业用 `crosstab` + `bar`。
4. **散点：因子 vs 收益**：`sns.regplot` 看单调性；注意横轴为当期因子、纵轴为**下期**收益时才有预测含义。
5. **滚动指标双子图**：`subplots(2, 1, sharex=True)` 上价格下成交量或 MACD。
6. **回测净值图**：阶梯线 `drawstyle="steps-post"` 适合 discrete 调仓点；标注最大回撤区间可用 `annotate`。
7. **中文标签**：本仓库 [`code/matplotlib/04_matplotlib处理图形中的中文.md`](./code/matplotlib/04_matplotlib处理图形中的中文.md) 配置字体。
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
