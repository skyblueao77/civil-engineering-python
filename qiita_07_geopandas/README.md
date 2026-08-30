# 土木のためのPython入門 Vol.7

Qiita記事:
[土木のためのPython入門⑦ GeoPandas・GISデータ入門編]([https://qiita.com/skyblueao77](https://qiita.com/skyblueao77/items/3b64dff2020415332445))

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/skyblueao77/civil-engineering-python/blob/main/qiita_07_geopandas/qiita_doboku_7.ipynb)

## 内容

* GeoPandasとは（GIS・空間データの概要）
* GeoDataFrame / GeoSeries の基本操作
* 空間データ（Shapefile / GeoJSON / GeoPackage）の読み込みと可視化
* 座標参照系（CRS: Coordinate Reference System）と投影変換
* 地理空間データに対する空間結合（Spatial Join）と統計処理

## 環境

* Python 3.13
* uv
* Jupyter Notebook

このリポジトリでは、プロジェクト全体で1つのPython環境を使用しています。

## セットアップ

リポジトリのルートディレクトリ（`civil-engineering-python`）で以下を実行してください。

```bash
uv sync