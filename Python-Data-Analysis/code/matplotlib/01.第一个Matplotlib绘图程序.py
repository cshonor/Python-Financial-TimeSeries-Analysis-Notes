"""
第一个 Matplotlib 绘图程序

1. 导入 pyplot 模块，用 as 简化别名
2. 用 NumPy 的 arange() 创建数据
3. 使用 plt.plot 绘图并显示
"""
from matplotlib import pyplot as plt
import numpy as np

# 创建 -50 到 50 的 ndarray 作为 x 轴数据
x = np.arange(-50, 50)

# 简单示例：y = x^2
y = x ** 2
plt.plot(x, y)
plt.title("y = x^2")
plt.show()
