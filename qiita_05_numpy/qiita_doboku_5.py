# %% [markdown]
# # 土木のためのPython入門⑤ NumPy入門｜配列・行列・数値計算を基礎から解説

# %%
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# ## 1. NumPyとは

# %%
water_level = np.array([1.2, 1.5, 1.4, 2.1, 2.8])
print(type(water_level))

# %% [markdown]
# ## 3. PythonのリストとNumPy配列

# %%
# リストの挙動（連結）
a_list = [1, 2, 3]
b_list = [4, 5, 6]
print("リストの足し算:", a_list + b_list)

# NumPy配列の挙動（要素ごとの計算）
a_arr = np.array([1, 2, 3])
b_arr = np.array([4, 5, 6])
print("NumPy配列の足し算:", a_arr + b_arr)

data = np.array([1, 2, 3, 4, 5])
print("data + 10:", data + 10)
print("data * 2:", data * 2)
print("data / 2:", data / 2)

# %% [markdown]
# ## 4. 土木データを計算する

# %%
water_level = np.array([1.2, 1.5, 1.4, 2.1, 2.8])
corrected_level = water_level + 0.3
print("補正後の水位:", corrected_level)

print("最大水位:", np.max(water_level))
print("最小水位:", np.min(water_level))
print("平均水位:", np.mean(water_level))

# %% [markdown]
# ## 5. ブロードキャスト

# %%
data = np.array([1, 2, 3])
print("ブロードキャスト (data + 10):", data + 10)

# %% [markdown]
# ## 6. 配列の形を確認する

# %%
data = np.array([1, 2, 3, 4, 5])
print("shape:", data.shape)
print("ndim:", data.ndim)
print("size:", data.size)
print("dtype:", data.dtype)

# %% [markdown]
# ## 7. 2次元配列と行列

# %%
data_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(data_2d)
print("shape:", data_2d.shape)

A = np.array([
    [1, 2],
    [3, 4]
])

# %% [markdown]
# ## 8. * と @ の違い

# %%
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("要素ごとの積 (A * B):\n", A * B)
print("行列積 (A @ B):\n", A @ B)

# %% [markdown]
# ## 9. 連立方程式を解く

# %%
# 2x +  y = 5
#  x + 3y = 6

A_eq = np.array([
    [2, 1],
    [1, 3]
])

b_eq = np.array([5, 6])

x_sol = np.linalg.solve(A_eq, b_eq)
print("連立方程式の解 [x, y]:", x_sol)

# %% [markdown]
# ## 10. NumPyのビューとコピー

# %%
data = np.array([10, 20, 30, 40, 50])

# ビューの例
part = data[1:4]
part[0] = 999
print("ビュー変更後の元配列:", data)

# コピーの例
data_orig = np.array([10, 20, 30, 40, 50])
part_copy = data_orig[1:4].copy()
part_copy[0] = 999
print("コピー変更後の元配列:", data_orig)

# %% [markdown]
# ## 12. NumPyとMatplotlibを組み合わせる

# %%
x = np.linspace(0, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x²")
plt.grid()
plt.show()