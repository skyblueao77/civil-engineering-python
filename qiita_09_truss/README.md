# 土木のためのPython入門 Vol.9

## 2次元三角形トラスをPythonで解析してみよう

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/skyblueao77/civil-engineering-python/blob/main/qiita_09_truss/qiita_doboku_9.ipynb)

## 内容

* 2次元三角形トラスの節点・部材・荷重・支持条件の定義
* 部材長、方向余弦、要素剛性行列の計算
* 要素剛性行列から全体剛性行列を組み立てる有限要素法の基本
* 支持条件を適用した連立方程式 `Ku=f` の求解
* 節点変位、支点反力、部材軸力の計算
* 変形を拡大したトラスモデルの可視化
* 理論値と解析結果の比較
* ヤング係数や荷重を変えた場合の変位の確認
* 複数の解析結果を pandas のデータフレームにまとめる方法

## 解析モデル

Aをピン支持、Bをローラー支持とし、節点Cに下向きの荷重を作用させる三角形トラスを扱います。

| 項目 | 値 |
| --- | ---: |
| A座標 | (0, 0) m |
| B座標 | (4, 0) m |
| C座標 | (2, 3) m |
| 部材 | AB、AC、BC |
| ヤング係数 `E` | 200 GPa |
| 断面積 `A` | 1.0×10⁻³ m² |
| 節点Cの荷重 | 10 kN 下向き |

計算では長さを m、力を N、応力を Pa の基本単位とし、表示時に mm や kN へ換算しています。

## 仮定

* 2次元構造として扱う
* 部材は直線部材とする
* 節点はピン接合とする
* 部材は軸方向力のみを負担する
* 部材の曲げ剛性は考慮しない
* 材料は線形弾性体とする
* 変形は小さいものとする
* 各部材のヤング係数と断面積は一定とする

## 環境

* Python 3.13
* uv
* Jupyter Notebook

このリポジトリでは、プロジェクト全体で1つのPython環境を使用しています。

## セットアップ

リポジトリのルートディレクトリ（`civil-engineering-python`）で以下を実行してください。

```bash
uv sync
```

## 実行方法

Pythonスクリプトを実行する場合は、リポジトリのルートディレクトリで以下を実行してください。

```bash
uv run python qiita_09_truss/qiita_doboku_9.py
```

Notebookを使用する場合は、上の **Open in Colab** バッジから開くか、Jupyterで `qiita_doboku_9.ipynb` を開いて上から順番に実行してください。

> この教材は学習用の簡略化されたモデルです。実構造物の設計や安全性の判断には使用しないでください。
