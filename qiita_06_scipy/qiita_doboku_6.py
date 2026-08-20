"""
土木のためのPython入門⑥ SciPyで科学技術計算
補間・数値積分・数値微分・最適化

著者: skyblueao77
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.differentiate import derivative
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize, root_scalar
from scipy.stats import norm


def main():
    # ============================================================
    # 1. SciPyのバージョン
    # ============================================================

    print(f"SciPy version: {scipy.__version__!s}")

    # ============================================================
    # 2. NumPyとSciPy
    # ============================================================

    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr!s}")
    print(f"Array * 2: {arr * 2!s}")

    # ============================================================
    # 3. 補間
    # ============================================================

    time = np.array([0, 10, 20, 30])
    water_level = np.array([1.2, 1.8, 2.5, 2.0])

    # 単純な1次元線形補間
    water_level_15 = np.interp(15, time, water_level)

    print("\n--- 線形補間 ---")
    print(f"15分後の水位: {water_level_15:.2f} m")

    # ============================================================
    # 4. 数値積分
    # ============================================================

    def f_integral(val):
        return val**2

    result_int, error_int = quad(f_integral, 0, 1)

    print("\n--- 数値積分 ---")
    print(f"∫₀¹ x² dx = {result_int!s}")
    print(f"推定誤差 = {error_int!s}")

    # ============================================================
    # 5. 土木工学の例：変化する幅から面積を求める
    # ============================================================

    def width(val):
        return 2 + 0.1 * val

    area, error_area = quad(width, 0, 10)

    print("\n--- 断面積の計算 ---")
    print(f"面積: {area:.2f}")
    print(f"推定誤差: {error_area!s}")

    # ============================================================
    # 6. 数値微分
    # ============================================================

    def f_derivative(val):
        return val**2

    result_diff = derivative(f_derivative, 3)

    print("\n--- 数値微分 ---")
    print(f"微分値: {result_diff.df!s}")
    print(f"推定誤差: {result_diff.error!s}")
    print(f"収束判定: {result_diff.success!s}")

    if result_diff.success:
        print("数値微分は正常に収束しました。")
    else:
        print("数値微分が収束しませんでした。")

    # ============================================================
    # 7. 方程式を数値的に解く
    # ============================================================

    def f_equation(val):
        return val**2 - 2

    result_root = root_scalar(f_equation, bracket=(0, 2))

    print("\n--- 方程式の求解 ---")
    print(f"解: {result_root.root!s}")
    print(f"収束判定: {result_root.converged!s}")

    # ============================================================
    # 8. 最適化
    # ============================================================

    def f_optimization(vec):
        return (vec[0] - 3) ** 2 + 1

    result_opt = minimize(f_optimization, x0=[0])

    print("\n--- 最適化 ---")
    print(f"最小値を与える x: {result_opt.x[0]!s}")
    print(f"最小値: {result_opt.fun!s}")
    print(f"収束判定: {result_opt.success!s}")

    # ============================================================
    # 9. 統計計算
    # ============================================================

    target_x = 0
    pdf_value = norm.pdf(target_x)

    print("\n--- 正規分布 ---")
    print(f"標準正規分布の x={target_x!s} における確率密度: {pdf_value!s}")

    # ============================================================
    # 10. 実例：水位データを補間して可視化
    # ============================================================

    time_obs = np.array([0, 10, 20, 30, 40, 50, 60])
    water_level_obs = np.array([1.2, 1.4, 1.9, 2.8, 3.1, 2.5, 1.8])

    interpolation = PchipInterpolator(time_obs, water_level_obs)

    time_interpolated = np.linspace(0, 60, 300)
    water_level_interpolated = interpolation(time_interpolated)

    plt.scatter(time_obs, water_level_obs, label="Observed")
    plt.plot(
        time_interpolated,
        water_level_interpolated,
        label="PCHIP interpolation",
    )

    plt.xlabel("Time (min)")
    plt.ylabel("Water level (m)")
    plt.title("Water Level")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()