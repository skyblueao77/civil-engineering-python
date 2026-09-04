# 土木のためのPython入門 Vol.8

Qiita記事:
[土木のためのPython入門⑧ 単純梁をPythonで解析してみよう](https://qiita.com/skyblueao77/items/cd31c475fdbf9d5a80f6)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/skyblueao77/civil-engineering-python/blob/main/qiita_08_beam/qiita_doboku_8.ipynb)

## 内容

* 単純支持梁に作用する等分布荷重モデルの構築
* Matplotlibを用いた構造モデル（梁・支点・荷重・寸法線）の描画
* 支点反力、せん断力、曲げモーメント、たわみの理論計算と実装
* NumPy配列を活用した全位置におけるせん断力・曲げモーメント・たわみの計算
* せん断力図（SFD）・曲げモーメント図（BMD）・たわみ曲線の3段可視化

## 環境

* Python 3.13
* uv
* Jupyter Notebook

このリポジトリでは、プロジェクト全体で1つのPython環境を使用しています。

## セットアップ

リポジトリのルートディレクトリ（`civil-engineering-python`）で以下を実行してください。

```bash
uv sync
