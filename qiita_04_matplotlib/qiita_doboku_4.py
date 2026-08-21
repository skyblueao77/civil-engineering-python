# %% [markdown]
# # 土木のためのPython入門④ matplotlib入門編
#
# 元記事のサンプルコードを実行できる形にまとめた教材用スクリプトです。

# %%
import matplotlib.pyplot as plt
import pandas as pd

# %% [markdown]
# ## 1. 折れ線グラフ

# %%
days = ["月", "火", "水", "木", "金", "土", "日"]
water_level = [1.2, 1.5, 1.4, 2.1, 2.8, 2.2, 1.7]
plt.plot(days, water_level)
plt.show()

# %% [markdown]
# ## 2. タイトルと軸ラベル

# %%
plt.plot(days, water_level)
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.show()

# %% [markdown]
# ## 3. グリッド

# %%
plt.plot(days, water_level)
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 4. 凡例

# %%
standard_level = [2.0] * 7
plt.plot(days, water_level, label="観測水位")
plt.plot(days, standard_level, label="基準水位")
plt.title("河川水位と基準水位")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.legend()
plt.grid()
plt.show()

# %% [markdown]
# ## 5. 棒グラフ

# %%
locations = ["A地点", "B地点", "C地点", "D地点"]
traffic = [1200, 1800, 1500, 900]
plt.bar(locations, traffic)
plt.title("地点別交通量")
plt.xlabel("地点")
plt.ylabel("交通量 (台/日)")
plt.show()

# %% [markdown]
# ## 6. 散布図

# %%
rainfall = [5, 10, 15, 20, 25, 30, 40]
water_level_rain = [1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.5]
plt.scatter(rainfall, water_level_rain)
plt.title("雨量と河川水位の関係")
plt.xlabel("雨量 (mm)")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 7. pandasとmatplotlib

# %%
river_data = pd.DataFrame(
    {
        "曜日": ["月", "火", "水", "木", "金", "土", "日"],
        "水位(m)": [1.2, 1.5, 1.4, 2.1, 2.8, 2.2, 1.7],
    }
)
print(river_data)
plt.plot(river_data["曜日"], river_data["水位(m)"])
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.show()

# %% [markdown]
# ## 8. CSVから読み込んでグラフ化

# %%
csv_data = """日,雨量(mm)
1,5
2,12
3,8
4,25
5,40
6,18
7,10
"""
with open("rainfall.csv", "w", encoding="utf-8") as f:
    f.write(csv_data)
rain_data = pd.read_csv("rainfall.csv")
print(rain_data.head())
plt.plot(rain_data["日"], rain_data["雨量(mm)"])
plt.title("日別雨量")
plt.xlabel("日")
plt.ylabel("雨量 (mm)")
plt.grid()
plt.show()

# %% [markdown]
# ## 9. グラフを画像として保存

# %%
plt.plot(river_data["曜日"], river_data["水位(m)"])
plt.title("河川水位の変化")
plt.xlabel("曜日")
plt.ylabel("水位 (m)")
plt.grid()
plt.savefig("river_water_level.png")
plt.show()