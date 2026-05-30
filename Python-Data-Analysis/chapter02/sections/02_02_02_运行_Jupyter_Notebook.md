# 2.2.2 运行 Jupyter Notebook

> 所属：[第 2 章](../chapter02_python_syntax_ipython_jupyter.md) · 《利用 Python 进行数据分析》

---

## 一、IPython 能不能写代码？

**可以。** IPython 本身就是 **交互式代码运行环境**：

| 能力 | 说明 |
|------|------|
| 逐行写/跑 | 输入一行、执行一行，立刻看结果，反复改 |
| 多行粘贴 | 粘贴整段代码块一次执行 |
| Cell 魔法 | Jupyter 里用 **`%%`** 写整 cell 代码（如 `%%timeit`） |
| 脚本加载 | `%run script.py` 把 `.py` 载入当前会话 |

**局限**：不适合大型工程、长期维护完整项目（无项目树、断点调试面板弱）→ 定稿代码放 `.py` + IDE/CPython。

### 内存会话 vs 磁盘文件

| | IPython CLI | Jupyter |
|---|-------------|---------|
| 代码在哪 | **内核进程内存** | **同一 IPython 内核内存** |
| 像什么 | 内存里的巨型临时 `.py` | 同上，只是多了 cell 分区 + Web UI |
| 关闭后 | 变量 **全消失** | 关浏览器 **内核可能仍在**；Restart 后变量消失 |
| 持久化 | `%save out.py 1-N` | 存 `.ipynb`（结构+输出）；整库导出 `nbconvert --to script` |

你在 cell 里定义的 `df`、函数、模型 **不会自动变成独立 `.py`**，只驻留当前内核；要上线必须 **显式保存** 为脚本文件。

---

## 二、IPython 与 Jupyter 的关系

### 1. 起源

Jupyter **脱胎于 IPython**：早期 IPython 自带网页交互界面；后来项目拆分重构，前端独立为 **Jupyter**，IPython 专注 Python 交互与内核能力。

### 2. 核心分工

| 组件 | 角色 |
|------|------|
| **IPython** | Python **交互内核（Kernel）**：解析 cell 代码、维护会话状态、魔法命令、In/Out 历史；**底层仍由 CPython 执行字节码** |
| **Jupyter** | **通用交互框架** = 前端界面 + 内核调度协议（Jupyter Notebook / **JupyterLab** = Web 操作台） |
| **多语言** | Jupyter 前端可对接 R、Julia 等几十种内核；跑 **Python** 时默认内核名 **`python3`**，实现上即 **IPython（ipykernel）** |

### 3. 通俗类比

```
Jupyter Notebook/Lab  =  网页操作台（前端 UI）
IPython Kernel        =  会话级执行后端（接 cell、管变量、魔法命令）
CPython               =  语言解释器（真正跑字节码）
```

- **IPython** 在 Jupyter 里扮演 **Kernel（内核进程）**——不是替换 CPython，而是 CPython 之上的 **交互执行层**。
- 命令行里 **`ipython`** 则是同一套能力的 **CLI 形态**（见 [2.2.1](./02_02_01_运行_IPython_命令行.md)）。

> 层级总览：[2.1 Python 解释器](./02_01_Python_解释器.md)

---

## 三、书本原文：运行 Jupyter

### 2.2.2 运行 Jupyter Notebook

| 项 | 说明 |
|----|------|
| 启动 | `jupyter notebook` 或 **`jupyter lab`**（推荐，功能更全） |
| 文件 | **`.ipynb`**（JSON），含代码 cell、输出、Markdown |
| 内核 | 浏览器通过 WebSocket 与本地 **IPython 内核**通信 |
| 关闭 | 关浏览器标签 **不会** 结束内核 → 需 **Kernel → Shutdown** 或 **Close and Halt** |

```bash
jupyter lab
# 或
jupyter notebook
```

### 常用操作速查

| 操作 | 快捷键 / 菜单 |
|------|----------------|
| 运行当前 cell | **Shift+Enter** |
| 运行并留在本 cell | **Ctrl+Enter** |
| 插入 cell | **B**（下方）/ **A**（上方）（命令模式） |
| 切换 Markdown | **M**（命令模式） |
| 重启内核 | Kernel → Restart |
| 清输出 | Cell → All Output → Clear |

---

## 四、【量化专属改造】

1. **因子探索默认工作台**：Notebook 里 `%matplotlib inline`、分 cell 跑「读数据 → 清洗 → groupby → 画图 → OLS」。
2. **内核状态**：同一内核里 `df` 一直驻留内存；改代码后 **Restart & Run All** 避免旧变量污染回测结果。
3. **`.ipynb` vs `.py`**：实验留 notebook；可 **`jupyter nbconvert --to script`** 或 `%run` 导出逻辑到 `strategy.py` 上线。
4. **多环境**：Notebook 右上角选对 **内核**（对应 conda 环境里的 ipykernel），否则 import 错包。

---

## 五、补充小结（背诵）

1. **IPython**：命令行交互终端 **或** Jupyter 的 Python 内核；可直接写/跑代码，**不是 IDE**。
2. **Jupyter**：基于 IPython 演进的 **通用交互平台**；Notebook/Lab 是 **Web 前端**，跑 Python 时依赖 **IPython 内核**。
3. **CPython**：无论 CLI 还是 Jupyter，最终执行 Python 的都是它。
4. **内存脚本**：交互代码驻留内核内存，关会话/Restart 即丢 → 定稿用 `%save` 或 `nbconvert`。

---

## 六、自检

- [ ] 能说明 Jupyter 前端与 IPython 内核的分工  
- [ ] 知道关浏览器不等于关内核  
- [ ] 能解释 IPython 在 CLI 与 Jupyter 中的两种形态  
- [ ] 知道 notebook 代码在内核内存里，与自动生成的 `.py` 不是一回事  

---

## 七、留白

（记录：常用 `jupyter lab` 端口、默认内核名、notebook 模板路径）

---

**相关**：[2.2.1 IPython 命令行](./02_02_01_运行_IPython_命令行.md) · [2.1 解释器与层级](./02_01_Python_解释器.md)

[← 返回第 2 章](../chapter02_python_syntax_ipython_jupyter.md)
