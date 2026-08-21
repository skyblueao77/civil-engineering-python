#%% モジュールのインポート
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.differentiate import derivative
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize, root_scalar
from scipy.stats import norm

#%% インストール後のバージョン確認
print(scipy.__version__)


#%% NumPyの基本配列計算
arr = np.array([1, 2, 3, 4, 5])

print(arr * 2)


#%% numpy.interp による1次元線形補間
time = np.array([0, 10, 20, 30])
water_level = np.array([1.2, 1.8, 2.5, 2.0])

water_level_15 = np.interp(
    15,
    time,
    water_level
)

print(water_level_15)


#%% scipy.integrate.quad による定積分 (f(x) = x^2)
def func_square(val):
    return val**2

result, _ = quad(func_square, 0, 1)

print(result)


#%% scipy.integrate.quad による断面面積の数値積分
def width(val):
    return 2 + 0.1 * val

area, _ = quad(width, 0, 10)

print(area)


#%% scipy.differentiate.derivative による数値微分
def func_diff(val):
    return val**2

res_diff = derivative(func_diff, 3)

print(f"微分値: {res_diff.df}")
print(f"推定誤差: {res_diff.error}")
print(f"収束判定: {res_diff.success}")


#%% scipy.differentiate.derivative の収束判定付き処理
def func_diff_check(val):
    return val**2

res_diff_check = derivative(func_diff_check, 3)

if res_diff_check.success:
    print(f"微分値: {res_diff_check.df}")
else:
    print("数値微分が収束しませんでした")


#%% scipy.optimize.root_scalar による方程式の数値解法
def func_root(val):
    return val**2 - 2

res_root = root_scalar(
    func_root,
    bracket=(0, 2)
)

print(res_root.root)


#%% scipy.optimize.minimize による関数の最小化
def func_min(vec):
    return (vec[0] - 3)**2 + 1

res_min = minimize(
    func_min,
    x0=[0]
)

print(res_min.x)
print(res_min.fun)


#%% scipy.stats.norm による正規分布の確率密度計算
x_val = 0

print(norm.pdf(x_val))


#%% 実例：PchipInterpolatorを用いた水位データの補間とMatplotlibによる可視化
# 観測データ
time = np.array([
    0, 10, 20, 30, 40, 50, 60
])

water_level = np.array([
    1.2,
    1.4,
    1.9,
    2.8,
    3.1,
    2.5,
    1.8
])

# PCHIP補間モデル作成とデータ生成
interpolation = PchipInterpolator(
    time,
    water_level
)

time_interpolated = np.linspace(
    0,
    60,
    300
)

water_level_interpolated = interpolation(
    time_interpolated
)

# 描画処理
plt.scatter(
    time,
    water_level,
    label="Observed"
)

plt.plot(
    time_interpolated,
    water_level_interpolated,
    label="PCHIP interpolation"
)

plt.xlabel("Time (min)")
plt.ylabel("Water level (m)")
plt.title("Water Level")

plt.legend()
plt.grid()

plt.show()