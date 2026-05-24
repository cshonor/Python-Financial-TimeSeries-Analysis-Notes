"""
NumPy 03 - Routines 函数

常用签名：
  np.ones(shape, dtype=None, order='C')
  np.zeros(shape, dtype=float, order='C')
  np.full(shape, fill_value, dtype=None, order='C')
  np.eye(N, M=None, k=0, dtype=float)           # k: 对角线偏移，0为主对角线
  np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
  np.arange([start,] stop [,step,] dtype=None)
  np.random.randint(low, high=None, size=None, dtype='l')
  np.random.normal(loc=0, scale=1, size=None)   # 正态分布
--------------------------------
参数详解：
  shape	数组的形状，可以是整数（一维）、元组（多维）
  dtype	数组元素的数据类型（如 np.int8、np.float64 等）
  order='C' 是 NumPy 创建 / 操作数组时，指定数组在内存中的存储顺序的参数，
'C' 是默认值，代表「C 语言风格的行优先存储」。
  fill_value	用于 np.full 填充的常数值
    N	方阵的行数（M 为列数，默认 N）
k	对角线偏移，0 为主对角线，正数向上偏移，负数向下偏移
start	起始值（默认 0）
stop	终止值（不包含）
num	等分区间的数量（默认 50）
endpoint=True 时包含右端点
retstep=False 不返回步长
dtype=None 自动推断数据类型
low	随机整数范围的下限（包含）
high	随机整数范围的上限（不包含）
size	生成数组的大小（如 (2, 3) 表示 2x3 矩阵）
loc	正态分布的均值
scale	正态分布的标准差
--------------------------------
用途详解：

  np.zeros 全 0 数组
    - 占位数组：预先分配内存再逐步填充
    - 累加器：result = np.zeros(n) 后循环 +=
    - 掩码/二值图：初始化后按条件赋值

  np.ones 全 1 数组
    - 神经网络权重初始化（常配合 scale）
    - 掩码：与目标数组相乘做筛选
    - 概率：均匀先验
    - shape=(3,) 一维 vs shape=(1,3) 二维：维度不同，矩阵运算行为不同（ML 中重要）

  np.full 指定值填充
    - 批量设置常数：如填充 -1、NaN
    - 构建特殊矩阵（非 0/1 的对角线等）

  np.eye 单位矩阵
    - 线性代数：矩阵求逆、特征值分解
    - k 参数：上/下对角线，用于构造带状矩阵

  np.arange 等差整数序列
    - 循环索引：for i in np.arange(n)
    - 坐标轴刻度、网格生成
    - 注意：不包含 stop，步长可指定

  np.linspace 等分区间
    - 绘图横轴：x = np.linspace(0, 2*np.pi, 100) 画 sin
    - 插值采样：在 [a,b] 内均匀取 n 个点
    - endpoint=True 时包含右端点

  np.random.rand  [0,1) 均匀分布 均匀分布，在 [0, 1) 内等概率采样 
    - 蒙特卡洛模拟、随机采样
    - 生成随机权重、dropout 掩码

  np.random.random  [0,1) 均匀分布  均匀，在 [0, 1) 内等概率采样（与 rand 类似，参数为 size=）
    - size=(10,1) 可指定多维形状
    - 左闭右开，不含 1

  np.random.randn  标准正态 N(0,1)
    - 无需参数，直接 randn(d0,d1,...) 指定形状
    - 深度学习权重初始化常用

  np.random.randint  随机整数
    - 随机抽样、打乱索引
    - 模拟掷骰子、抽奖

  np.random.normal  正态分布
    - 模拟测量误差、噪声
    - 股价/收益模拟、深度学习权重初始化

  np.sum/mean/std/min/max
    - 描述性统计：数据探索
    - 特征工程：构造均值、方差特征
    - 归一化：(x - mean) / std
"""
import numpy as np

print("=== 1. 数组创建类 routines ===")
print("np.zeros(3):", np.zeros(3))

# np.ones 不同 shape：(3,)一维 (1,3)行向量 (3,1)列向量
print("np.ones((2, 3)):\n", np.ones((2, 3)))
print("np.ones((3,)) 一维:", np.ones((3,)))           # → [1., 1., 1.]
print("np.ones((1, 3)) 行向量:\n", np.ones((1, 3)))   # → [[1., 1., 1.]]
print("np.ones((3, 1)) 列向量:\n", np.ones((3, 1)))   # → [[1.],[1.],[1.]]
print("np.full(shape=(3,3), fill_value=6):\n", np.full(shape=(3, 3), fill_value=6))  # → [[6,6,6],...]
print("np.eye(N=3) 单位矩阵:\n", np.eye(N=3))  # → [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]
print("np.eye(N=3, M=2) 非方阵:\n", np.eye(N=3, M=2))  # → [[1.,0.],[0.,1.],[0.,0.]]
print("np.eye(N=3, k=-1) 下对角线:\n", np.eye(N=3, k=-1))  # k=-1 主对角线下移 → [[0,0,0],[1,0,0],[0,1,0]]
print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))  # 默认 endpoint=True 含右端
print("np.linspace(0,100,10,endpoint=False):", np.linspace(0, 100, 10, endpoint=False))  # 不含100
print("np.linspace(0,360,4,endpoint=False):", np.linspace(0, 360, 4, endpoint=False))    # 0,90,180,270 角度分4段

print("\n=== 2. 随机数 routines ===")
np.random.seed(42)
#NumPy 库中用于设置随机数生成器种子的函数，核心作用是让随机数生成结果可复现（固定化）。
print("np.random.rand(2, 3):\n", np.random.rand(2, 3))
#作用：生成取值范围在 [0.0, 1.0) 之间的随机浮点数（包含 0.0，不包含 1.0）；
#参数：(2, 3) 表示输出数组的形状，即2 行 3 列的二维数组；
#区别于 randint：rand 生成浮点数，randint 生成整数；且 rand 无需指定上下限（固定 0 到 1）
print("np.random.randint(1, 10, size=5):", np.random.randint(1, 10, size=5))
#若只传两个参数（如 np.random.randint(1, 10)），则只生成1 个随机整数（而非数组）；
#若想生成二维数组，可将 size 设为元组，比如 size=(2,3) 会生成 2 行 3 列的数组；
#该函数生成的是伪随机数，若需固定结果（如复现实验），可先用 np.random.seed(固定数字) 设定随机种子
print("np.random.randint(low=0, high=100, size=(3,5)):\n", np.random.randint(low=0, high=100, size=(3, 5)))
# randn(d0,d1,...)=标准正态 N(0,1)，如 randn(10,5) 生成 10x5 矩阵
print("np.random.randn(2,3):\n", np.random.randn(2, 3))
print("np.random.normal(loc=175, scale=10, size=5) 身高模拟:", np.random.normal(loc=175, scale=10, size=5))
#np.random.normal(loc, scale, size) 生成正态分布随机数，loc 是均值（中心），scale 是标准差（离散程度），size 是输出形状；
#正态分布的数值集中在均值附近，标准差越大，数值范围越广；
#设定 np.random.seed(固定值) 可固定随机结果，size 传元组可生成多维数组。
print("np.random.random(5) [0,1)左闭右开:", np.random.random(5))
#作用：生成取值范围在 [0.0, 1.0) 之间的随机浮点数（包含 0.0，不包含 1.0）；
#参数 5：表示输出数组的总元素个数 / 形状，这里传入单个整数 5，会生成长度为 5 的一维数组；
#关键区别：random() 的参数需是整数或元组（如 size=(2,3)），而 rand() 是直接传多个整数（如 rand(2,3)），本质功能完全一致。
print("np.random.random(size=(10,1)) 10x1列向量:\n", np.random.random(size=(10, 1)))

print("\n=== 3. 数学 / 统计 routines ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"arr = {arr}")
print("np.sum(arr):", np.sum(arr))
print("np.mean(arr):", np.mean(arr))
print("np.std(arr):", np.std(arr))
print("np.min(arr), np.max(arr):", np.min(arr), np.max(arr))

# (3,) 一维 vs (1,3) 二维 在矩阵运算中的区别
print("\n=== 4. shape (3,) vs (1,3) 矩阵运算区别 ===")
a_1d = np.ones((3,))      # 一维 → array([1., 1., 1.])
a_2d = np.ones((1, 3))    # 二维行向量 → array([[1., 1., 1.]])
B = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
print("a_1d shape:", a_1d.shape, "a_2d shape:", a_2d.shape)
print("a_1d + B (广播):\n", a_1d + B)   # (3,) 与 (2,3) 广播
print("a_2d + B (广播):\n", a_2d + B)   # (1,3) 与 (2,3) 广播
# 与矩阵乘法时：a_1d 不能直接 @ 矩阵，a_2d 可以
