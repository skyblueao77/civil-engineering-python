# %% モジュールのインポート
from typing import cast

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib_fontja  # noqa: F401
from shapely.geometry import LineString, Point, Polygon

# %% GeoPandasのバージョン確認
print(f"GeoPandas: {gpd.__version__}")

# %% GeoDataFrameの作成
# 大阪周辺の地点を、経度・緯度（EPSG:4326）で作成する
points = gpd.GeoDataFrame(
    {
        "name": ["A観測地点", "B観測地点", "C観測地点"],
        "population": [12000, 8500, 15600],
    },
    geometry=[
        Point(135.000, 34.700),
        Point(135.010, 34.700),
        Point(135.000, 34.710),
    ],
    crs="EPSG:4326",
)

print(points)
print(points.geometry)

# %% GeoSeriesから座標を取り出す
print("経度:")
print(points.geometry.x)
print("緯度:")
print(points.geometry.y)

# %% GeoJSONなどのファイルを読み込む場合
# 実際のファイルを使うときは、次のように読み込む
# areas = gpd.read_file("data/sample.geojson")
# print(areas.head())
# print(areas.info())

# %% CRSの確認と投影座標系への変換
print(f"変換前のCRS: {points.crs}")

# 大阪を含む近畿地方ではJGD2011平面直角座標系第6系を使用する
# このCRSの座標単位はメートルなので、距離や面積を計算できる
points_projected = points.to_crs("EPSG:6674")
print(f"変換後のCRS: {points_projected.crs}")

# %% 距離の計算
# 1つ目の観測地点から他の観測地点までの距離（m）
point_a = cast(Point, points_projected.geometry.iloc[0])
distances = points_projected.geometry.distance(point_a)
print("A観測地点からの距離（m）:")
print(distances.round(2))

# %% 属性情報による色分け
ax = points.plot(
    column="population",
    legend=True,
    figsize=(7, 5),
    markersize=100,
)
ax.set_title("観測地点（人口による色分け）")
ax.set_xlabel("経度")
ax.set_ylabel("緯度")
plt.show()

# %% バッファの作成
# EPSG:4326のままではなく、メートル単位のCRSで100 mのバッファを作る
buffers = points_projected.geometry.buffer(100)

buffer_gdf = gpd.GeoDataFrame(
    {"name": points_projected["name"]},
    geometry=buffers,
    crs=points_projected.crs,
)

print(buffer_gdf)

ax = buffer_gdf.plot(alpha=0.4, edgecolor="black", figsize=(7, 5))
points_projected.plot(ax=ax, color="red", markersize=20)
ax.set_title("観測地点から100 mのバッファ")
ax.set_aspect("equal")
plt.show()

# %% クリップ
# 道路と対象区域をサンプルデータとして作成する
roads = gpd.GeoDataFrame(
    {"road_name": ["道路1", "道路2"]},
    geometry=[
        LineString([(134.995, 34.695), (135.015, 34.715)]),
        LineString([(134.995, 34.710), (135.015, 34.710)]),
    ],
    crs="EPSG:4326",
).to_crs("EPSG:6674")

study_area = gpd.GeoDataFrame(
    {"area_name": ["解析対象区域"]},
    geometry=[
        Polygon(
            [
                (134.998, 34.698),
                (135.008, 34.698),
                (135.008, 34.708),
                (134.998, 34.708),
            ]
        )
    ],
    crs="EPSG:4326",
).to_crs("EPSG:6674")

clipped_roads = gpd.clip(roads, study_area)
print("解析対象区域内の道路:")
print(clipped_roads)

ax = study_area.plot(facecolor="none", edgecolor="black", figsize=(7, 5))
clipped_roads.plot(ax=ax, color="blue", linewidth=2)
ax.set_title("解析対象区域でクリップした道路")
ax.set_aspect("equal")
plt.show()

# %% 空間結合
# 観測地点がどの区域に含まれるかを、位置関係で結合する
areas = gpd.GeoDataFrame(
    {"area_name": ["西側区域", "東側区域"]},
    geometry=[
        Polygon(
            [
                (134.995, 34.695),
                (135.005, 34.695),
                (135.005, 34.715),
                (134.995, 34.715),
            ]
        ),
        Polygon(
            [
                (135.005, 34.695),
                (135.015, 34.695),
                (135.015, 34.715),
                (135.005, 34.715),
            ]
        ),
    ],
    crs="EPSG:4326",
)

joined = gpd.sjoin(points, areas, how="left", predicate="within")
print("空間結合の結果:")
print(joined[["name", "population", "area_name"]])

# 区域ごとの人口集計（pandasのgroupbyと組み合わせる）
summary = joined.groupby("area_name", dropna=False)["population"].sum()
print("区域ごとの人口:")
print(summary)
