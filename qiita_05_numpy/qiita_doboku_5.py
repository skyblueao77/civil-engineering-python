import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. NumPyとは & 3. PythonのリストとNumPy配列
# ==========================================
# Python標準リストの挙動（連結される）
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("リストの加算:", list_a + list_b)  # Output: [1, 2, 3, 4, 5, 6]

# NumPy配列（ndarray）の挙動（要素ごとに計算される）
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
print("NumPy配列の加算:", arr_a + arr_b)  # Output: [5 7 9]

# 配列要素の累乗計算
print("要素ご体の自乗:", arr_a**2)  # Output: [1 4 9]


# ==========================================
# 4. 土木データを計算する
# ==========================================
water_level = np.array([1.2, 1.5, 2.1, 1.8, 2.5])

# 全要素への一括加算
water_level_adjusted = water_level + 0.3
print("補正後水位:", water_level_adjusted)

# 統計値の算出
print("最大水位:", np.max(water_level))
print("最小水位:", np.min(water_level))
print("平均水位:", np.mean(water_level))


# ==========================================
# 5. ブロードキャスト
# ==========================================
arr = np.array([1, 2, 3])
# スカラー値が自動的に拡張されて計算される
result = arr + 10
print("ブロードキャスト結果:", result)  # Output: [11 12 13]


# ==========================================
# 6. 配列の形を確認する
# ==========================================
sample_arr = np.array([[1, 2, 3], [4, 5, 6]])

print("shape (各次元の大きさ):", sample_arr.shape)  # (2, 3)
print("ndim (次元数):", sample_arr.ndim)  # 2
print("size (全要素数):", sample_arr.size)  # 6
print("dtype (データ型):", sample_arr.dtype)  # int64 または int32


# ==========================================
# 7. 2次元配列と行列 & 8. * と @ の違い
# ==========================================
A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# 要素ごとの積 (*)
print("要素ごとの積 (*):\n", A * B)

# 行列積 (@)
print("行列積 (@):\n", A @ B)


# ==========================================
# 9. 連立方程式を解く
# ==========================================
# 2x + y = 5
# x + 3y = 10
A_eq = np.array([[2, 1], [1, 3]])

B_eq = np.array([5, 10])

# 解 [x, y] を求める
sol = np.linalg.solve(A_eq, B_eq)
print("連立方程式の解 (x, y):", sol)


# ==========================================
# 10. NumPyのビューとコピー
# ==========================================
original = np.array([1, 2, 3, 4, 5])

# スライスによるビューの作成（参照を共有）
view_part = original[0:3]
view_part[0] = 999
print("ビュー変更後の元配列:", original)  # 元のデータも変更される

# コピーの作成（独立したデータ）
original_2 = np.array([1, 2, 3, 4, 5])
copy_part = original_2[0:3].copy()
copy_part[0] = 999
print("コピー変更後の元配列:", original_2)  # 元のデータは影響を受けない


# ==========================================
# 12. NumPyとMatplotlibを組み合わせる
# ==========================================
# 0から10までの範囲を100等分
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="y = sin(x)")
plt.title("NumPy and Matplotlib Visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()