# %% [markdown]
# # 土木のためのPython入門④ matplotlib入門編

# %% [markdown]
# ## 2. matplotlibのセットアップと日本語化
# Python 3.12以降では `japanize-matplotlib` が非推奨となったため、
# `matplotlib-fontja` の利用が推奨されています。

# %%
# 日本語化ライブラリとmatplotlibの読み込み
import matplotlib.pyplot as plt
import matplotlib_fontja  # noqa: F401
import pandas as pd

# %% [markdown]
# ## 3. 折れ線グラフを作ってみる

# %%
days = ["月", "火", "水", "木", "金", "土", "日"]
water_level = [1.2, 1.5, 1.4, 2.1, 2.8, 2.2, 1.7]

plt.plot(days, water_level)
plt.show()

# %% [markdown]
# ## 4. グラフにタイトルを付ける

# %%
plt.plot(days, water_level)
plt.title("河川水位の変化")
plt.show()

# %% [markdown]
# ## 5. 軸ラベルを付ける

# %%
plt.plot(days, water_level)
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.show()

# %% [markdown]
# ## 6. グリッドを表示する

# %%
plt.plot(days, water_level)
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 7. 凡例を表示する

# %%
days = ["月", "火", "水", "木", "金", "土", "日"]
water_level = [1.2, 1.5, 1.4, 2.1, 2.8, 2.2, 1.7]
standard_level = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

plt.plot(days, water_level, label="観測水位")
plt.plot(days, standard_level, label="基準水位")
plt.title("河川水位と基準水位")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.legend()
plt.grid()
plt.show()

# %% [markdown]
# ## 8. 棒グラフを作ってみる

# %%
locations = ["A地点", "B地点", "C地点", "D地点"]
traffic = [1200, 1800, 1500, 900]

plt.bar(locations, traffic)
plt.title("地点別交通量")
plt.xlabel("地点")
plt.ylabel("交通量 (台/日)")
plt.show()

# %% [markdown]
# ## 9. 散布図を作ってみる

# %%
rainfall = [5, 10, 15, 20, 25, 30, 40]
water_level = [1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.5]

plt.scatter(rainfall, water_level)
plt.title("雨量と河川水位の関係")
plt.xlabel("雨量 (mm)")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 10. pandasとmatplotlibを組み合わせる

# %%
river_data = pd.DataFrame({
    "曜日": ["月", "火", "水", "木", "金", "土", "日"],
    "水位(m)": [1.2, 1.5, 1.4, 2.1, 2.8, 2.2, 1.7]
})

plt.plot(river_data["曜日"], river_data["水位(m)"])
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 11. CSVファイルから読み込んでグラフを作る
# ※ あらかじめ `rainfall.csv` が存在する環境で実行してください。

# %%
# rain_data = pd.read_csv("rainfall.csv")
# plt.plot(rain_data["日"], rain_data["雨量(mm)"])
# plt.title("日別雨量")
# plt.xlabel("日")
# plt.ylabel("雨量 (mm)")
# plt.grid()
# plt.show()

# %% [markdown]
# ## 12. グラフを画像として保存する

# %%
plt.plot(river_data["曜日"], river_data["水位(m)"])
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.savefig("river_water_level.png")
plt.show()