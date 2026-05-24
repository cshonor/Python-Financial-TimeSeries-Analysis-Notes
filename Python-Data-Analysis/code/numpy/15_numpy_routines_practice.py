"""
NumPy 03.2 - Routines 练习

完成下方练习，运行检查输出。
"""
import numpy as np

# 练习 1：用 np.zeros 创建 2x4 全 0 数组
# 你的代码：
# arr1 = 
# print("1:", arr1)

# 练习 2：用 np.full 创建 3x3、填充值为 5 的数组
# 你的代码：
# arr2 = 
# print("2:", arr2)

# 练习 3：用 np.eye 创建 4x4 单位矩阵，再试试 k=1（上对角线）
# 你的代码：
# arr3 = 
# print("3:", arr3)

# 练习 4：用 np.arange 生成 [0, 5, 10, 15, 20]
# 你的代码：
# arr4 = 
# print("4:", arr4)

# 练习 5：用 np.linspace 在 [0, 1] 间生成 6 个等分点（含端点）
# 你的代码：
# arr5 = 
# print("5:", arr5)

# 练习 6：用 np.random.randint 生成 1~100 之间的 10 个随机整数
# 你的代码：
# arr6 = 
# print("6:", arr6)

# 练习 7：用 np.random.normal 生成均值 10、标准差 2 的 5 个样本
# 你的代码：
# arr7 = 
# print("7:", arr7)

# ========== 1.3.5 习题 ==========
# 习题 1：形状(3,4)的二维数组，取值范围(-5,5)
# arr = np.random.randint(-5, 6, (3, 4))

# 习题 2：等差数列，步长3，长度5
# arr = np.arange(0, 15, 3)  # [0,3,6,9,12]

# 习题 3：3维(100,100,3)，0-1随机，dtype=float64
# arr = np.random.random((100, 100, 3)).astype(np.float64)

# 习题 4：圆等分8份的弧度（np.pi）
# angles = np.linspace(0, 2*np.pi, 9)[:-1]  # 或 np.linspace(0, 2*np.pi, 8, endpoint=False)

# ========== 参考答案（取消注释可对比） ==========
# arr1 = np.zeros((2, 4))
# arr2 = np.full((3, 3), 5)
# arr3 = np.eye(4)  # k=1: np.eye(4, k=1)
# arr4 = np.arange(0, 25, 5)
# arr5 = np.linspace(0, 1, 6)
# arr6 = np.random.randint(1, 101, size=10)
# arr7 = np.random.normal(10, 2, 5)
