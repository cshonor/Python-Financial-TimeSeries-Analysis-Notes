"""
NumPy 02.1 - numpy 数据类型

常用 dtype：bool_ / int / uint / float / complex 等
"""
import numpy as np

# 布尔型
arr_bool = np.array([True, False, True], dtype=np.bool_)
print("bool_:", arr_bool, arr_bool.dtype)

# 整数型 - 用 np.iinfo() 查看取值范围
print("\n有符号整数 np.iinfo():")
for t in [np.int8, np.int16, np.int32, np.int64]:
    info = np.iinfo(t)
    print(f"  {t.__name__:6} min={info.min:>22}, max={info.max:>22}")

print("\n无符号整数 np.iinfo():")
for t in [np.uint8, np.uint16, np.uint32, np.uint64]:
    info = np.iinfo(t)
    print(f"  {t.__name__:7} min={info.min:>22}, max={info.max:>22}")

# int_ / intc / intp（平台相关）
print("\n平台相关:")
print("int_ 默认整数:", np.array([1]).dtype)
print("intp 索引用整数")

# 浮点型 - 用 np.finfo() 查看精度
print("\n浮点型 np.finfo():")
for t in [np.float16, np.float32, np.float64]:
    info = np.finfo(t)
    print(f"  {t.__name__:8} 精度{info.precision:2}位  min={info.min:.2e}  max={info.max:.2e}")

# 复数型
print("\n复数型:")
print("complex_  complex128 简写，128位复数")
print("complex64 双32位浮点(实部+虚部):", np.array([1+2j], dtype=np.complex64).dtype)
print("complex128 双64位浮点(实部+虚部):", np.array([1+2j]).dtype)


# np.iinfo 与 np.finfo

#np.iinfo(dtype)

#返回整数类型的机器限制信息。

#| 属性 | 含义 |
#|------|------|
#| `min` | 该类型能表示的最小值 |
#| `max` | 该类型能表示的最大值 |
#| `bits` | 位数（如 int8 为 8） |
#| `dtype` | 对应的 NumPy dtype |

#--------------------------------

#np.finfo(dtype)

#返回浮点类型的机器限制信息。

#| 属性 | 含义 |
#|------|------|
#| `min` | 最小正数 |
#| `max` | 最大值 |
#| `precision` | 十进制有效位数 |
#| `eps` | 最小可表示正数（机器精度） |
#--------------------------------