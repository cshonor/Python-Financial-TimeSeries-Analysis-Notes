"""
NumPy 02 - ndarray 元素统一

1. numpy 默认 ndarray 的所有元素的类型是相同的
2. 如果传进来的列表中包含不同的类型，则统一为同一类型
   优先级：str > float > int
"""
import numpy as np

print("=== 优先级 str > float > int 示例 ===")
print("int  alone →", np.array([1, 2, 3]).dtype)
print("int+float →", np.array([1, 2, 3.0]).dtype)      # float 优先
print("int+str   →", np.array([1, 2, "x"]).dtype)      # str 优先
print("float+str →", np.array([1.0, 2.0, "x"]).dtype)  # str 优先
print("int+float+str →", np.array([1, 2.5, "a"]).dtype)

print("\n=== 元素类型自动统一 ===")

# 1. 纯整数 → int
arr1 = np.array([1, 2, 3])
print(f"[1,2,3] dtype: {arr1.dtype}")  # int64 或 int32

# 2. 整数 + 浮点数 → 自动提升为 float
arr2 = np.array([1, 2, 3.0])
print(f"[1,2,3.0] dtype: {arr2.dtype}")  # float64

# 3. 整数 + 字符串 → 统一为字符串
arr3 = np.array([1, 2, "a"])
print(f"[1,2,'a'] dtype: {arr3.dtype}")  # <U11 或 str

#<U11是Unicode字符串类型，最大长度为11个字符。例子：创建包含字符串的数组

str_arr = np.array(["Python", "NumPy", "数据分析", "12345678901"])
print("数组内容：", str_arr)
print("数组dtype：", str_arr.dtype)  # 输出 <U11
print("每个元素的最大字符数：", str_arr.dtype.itemsize // 4)  # Unicode字符占4字节，11*4=44字节

# 验证字符串长度限制：超过11个字符会被截断
long_str_arr = np.array(["123456789012"], dtype="<U11")
print("\n超长字符串截断后：", long_str_arr)  # 输出 ['12345678901']

#NumPy 会根据数组中最长字符串的长度自动设置 U 后的数字。比如上面例子中最长的元素是 "12345678901"（11 个字符），所以 dtype 自动变成 <U11；如果最长是 5 个字符，就是 <U5

# 4. 手动指定 dtype
arr4 = np.array([1, 2, 3], dtype=float)
print(f"指定 dtype=float: {arr4} dtype: {arr4.dtype}")

arr5 = np.array([1.1, 2.2, 3.3], dtype=int)  # 浮点会被截断
print(f"指定 dtype=int: {arr5} dtype: {arr5.dtype}")  # [1 2 3]
