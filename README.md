# 土木のためのPython入門

土木工学を学ぶ学生向けのPython入門教材です。

Pythonをこれから学び始める土木系学生を対象に、

**環境構築 → Python基礎 → データ分析**

という流れで、土木分野でPythonを使うための基礎を学びます。

Qiitaで公開している連載記事と、このリポジトリのJupyter Notebookを組み合わせて学習できるようにしています。

---

## 対象読者

以下のような方を想定しています。

- 土木工学を専攻している学生
- Pythonをこれから学び始める学生
- プログラミング初心者
- 土木分野でデータ分析をしてみたい方
- AIにPythonコードを書いてもらうだけでなく、コードの意味を理解したい方
- pandasなどを使って土木データを扱ってみたい方

特に、**「土木学生だけどPythonを何に使えばいいのかわからない」**という方を主な対象としています。

---

## この教材で学ぶこと

現在は以下の3回分を公開しています。

| 回 | 内容 | 主なテーマ |
|---|---|---|
| Vol.1 | 環境構築編 | Google Colab / uv / VS Code |
| Vol.2 | 基本文法編 | 変数 / データ型 / 条件分岐 / 繰り返し |
| Vol.3 | pandas入門編 | DataFrame / Series / データ抽出 / CSV |

今後、土木データ分析、可視化、数値計算、GISなどへの発展を予定しています。

---

# 連載記事

## Vol.1 環境構築編

**土木のためのPython入門① 環境構築編（Google Colab・uv）**

Pythonを学習するための環境を準備します。

- Google Colab
- VS Code
- uv
- Python
- 仮想環境

について扱います。

[Qiita記事：Vol.1 環境構築編](https://qiita.com/skyblueao77/items/c4a0e7ddc9913c55994f)

---

## Vol.2 基本文法編

**土木のためのPython入門② 基本文法編**

Pythonを使うために必要となる基本的な文法を学びます。

- 変数
- データ型
- 四則演算
- 条件分岐
- 繰り返し処理
- リスト

などを、土木分野を意識した例題とともに扱います。

[Qiita記事：Vol.2 基本文法編](https://qiita.com/skyblueao77/items/65abd5ad5befa474ee5f)

---

## Vol.3 pandas入門編

**土木のためのPython入門③ pandas入門編**

土木分野で扱うことの多い表形式データを、pandasを使って処理します。

- DataFrame
- Series
- データの作成
- 行・列の抽出
- 条件によるデータ抽出
- 基本的な統計処理
- CSVファイルの読み込み

などを扱います。

[Qiita記事：Vol.3 pandas入門編](https://qiita.com/skyblueao77/items/c8c4902706f97415d1ec)

---

# リポジトリの構成

```text
civil-engineering-python/
│
├── 01_environment/
│   └── ...
│
├── qiita_02_basic/
│   ├── civil_engineering_python_intro_02.ipynb
│   ├── README.md
│   ├── pyproject.toml
│   └── uv.lock
│
├── qiita_03_pandas/
|   |── qiita_doboku_3.ipynb
│   ├── README.md
│   ├── pyproject.toml
│   └── uv.lock
│
└── README.md
````

各回のフォルダには、対応するNotebookや環境設定ファイルなどを配置しています。

---

# 環境構築

このリポジトリでは、基本的に

* Python 3.13
* uv
* VS Code
* Jupyter Notebook

を使用します。

## 方法1：Google Colabを使う

**Pythonの環境構築をせずに、とりあえずコードを実行してみたい場合はこちらがおすすめです。**

Google Colabを利用すると、ブラウザ上でPythonコードを実行できます。

各記事に掲載している **「Open in Colab」** ボタンからNotebookを開いてください。

Google Colabでは、基本的にPythonやJupyter環境を自分でインストールする必要はありません。

### Google Colabがおすすめな人

* Pythonをまず試してみたい
* 環境構築でつまずきたくない
* PCにPythonをインストールしたくない
* Notebookをブラウザ上で実行したい

---

# 方法2：uv + VS Codeを使う

**継続的にPythonを学習したい場合はこちらをおすすめします。**

この教材では、Python環境の管理に `uv` を使用しています。

`uv` はPythonのバージョン管理、仮想環境、パッケージ管理などをまとめて扱えるツールです。

---

## 1. VS Codeをインストール

まずVisual Studio Codeをインストールしてください。

公式サイト：

[https://code.visualstudio.com/](https://code.visualstudio.com/)

インストール後、VS Codeを起動します。

---

## 2. uvをインストール

uvの公式ドキュメントに従ってインストールしてください。

公式ドキュメント：

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

Windows PowerShellでは、公式のインストール方法を利用できます。

インストール後、PowerShellで以下を実行します。

```powershell
uv --version
```

バージョン番号が表示されれば、uvがインストールされています。

例：

```text
uv 0.x.x
```

---

## 3. リポジトリを取得

Gitがインストールされている場合、以下のコマンドでリポジトリを取得できます。

```powershell
git clone https://github.com/skyblueao77/civil-engineering-python.git
```

その後、リポジトリのディレクトリに移動します。

```powershell
cd civil-engineering-python
```

---

## 4. 学習する回のディレクトリへ移動

例えばVol.2を学習する場合：

```powershell
cd 02_basic_syntax
```

このディレクトリには、その回のPython環境を定義する `pyproject.toml` と `uv.lock` が含まれています。

---

## 5. Python環境を準備

以下を実行します。

```powershell
uv sync
```

`uv sync` により、プロジェクトで指定されているPython環境や依存パッケージが準備されます。

この教材では、Vol.2についてPython 3.13を使用しています。

---

## 6. VS Codeでフォルダを開く

VS Codeで、現在のディレクトリを開きます。

```powershell
code .
```

または、VS Codeの

**ファイル → フォルダーを開く**

から対象フォルダを開いてください。

---

## 7. Jupyter Notebookを開く

`.ipynb` ファイルをVS Codeで開きます。

例えばVol.2では、

```text
civil_engineering_python_intro_02.ipynb
```

を使用します。

VS CodeでNotebookを開くと、セルごとにPythonコードを実行できます。

---

# Jupyter Notebookについて

この教材では、主にJupyter Notebook形式（`.ipynb`）でコードを公開しています。

Notebookでは、

```text
コードを書く
↓
実行する
↓
結果を見る
↓
次のコードを書く
```

という形で、Pythonを少しずつ試すことができます。

Python初心者の学習にも適しています。

---

# 仮想環境について

この教材では、`uv` を使ってプロジェクトごとのPython環境を管理しています。

例えば、

```text
プロジェクトA
    └── Python環境A

プロジェクトB
    └── Python環境B
```

のように、それぞれのプロジェクトで必要なパッケージを分離できます。

これにより、

* 別の教材でインストールしたパッケージとの衝突
* Python環境の違いによるエラー
* パッケージのバージョン違い

などを減らすことができます。

---

# `uv sync` とは？

この教材では、各回の環境設定ファイルに基づいて、

```powershell
uv sync
```

を実行します。

`uv sync` は、プロジェクトの設定に従って必要なPython環境・依存パッケージを整えるためのコマンドです。

そのため、基本的には、

```text
pyproject.toml
uv.lock
```

を勝手に変更せず、

```powershell
uv sync
```

を実行するだけで学習環境を準備できます。

---

# Pythonの実行

Pythonファイルを実行する場合は、例えば以下のようにします。

```powershell
uv run python example.py
```

`uv run` を使うことで、プロジェクトの環境を利用してPythonを実行できます。

---

# この教材で使用する主な技術

* Python
* Jupyter Notebook
* Google Colab
* uv
* VS Code
* pandas
* NumPy
* matplotlib
* CSV

今後、土木分野で利用するデータ処理・可視化・数値計算・GIS関連のライブラリも扱う予定です。

---

# 土木工学とPython

土木工学では、さまざまなデータを扱います。

例えば、

* 雨量
* 水位
* 流量
* 交通量
* 地形
* 測量データ
* 地盤データ
* 構造物の計測データ
* 実験データ

などがあります。

これらをPythonで処理することで、

```text
データの読み込み
        ↓
データの整理
        ↓
計算・統計処理
        ↓
グラフ化
        ↓
結果の分析
```

という作業を効率化できます。

この教材では、単にPythonの文法を覚えることではなく、

**「土木工学でPythonをどう使うか」**

を意識して学習していきます。

---

# AI時代にPythonを学ぶ意味

現在は、生成AIを利用することでPythonコードを比較的簡単に生成できます。

そのため、

> 「コードをすべて自分で暗記する必要があるのか？」

という疑問が生まれます。

この教材では、AIによるコード生成そのものを否定するのではなく、

**AIが生成したコードを理解・検証・修正できること**

を重要視しています。

例えば、AIにコードを書かせたとしても、

* 何を計算しているのか
* 入力データは正しいのか
* 単位は合っているのか
* エラーの原因は何なのか
* 計算結果は妥当なのか
* 土木工学的に意味のある結果なのか

を判断するためには、Pythonとデータ処理の基礎知識が必要です。

特に土木分野では、

**「プログラムが正常に実行された」ことと「解析結果が正しい」ことは同じではありません。**

Pythonの文法だけでなく、土木工学として結果を検証する姿勢も大切にします。

---

# 学習の進め方

おすすめの順番は以下です。

```text
Vol.1
環境構築
   ↓
Vol.2
Python基本文法
   ↓
Vol.3
pandas
   ↓
データ可視化
   ↓
NumPy・数値計算
   ↓
土木データ分析
   ↓
GIS・空間データ
```

最初からすべてを理解する必要はありません。

Notebookを実際に動かしながら、

**「コードを書く → 実行する → 結果を見る → 少し変更する」**

というサイクルを繰り返してください。

---

# トラブルシューティング

## `uv` コマンドが見つからない

以下を実行して確認してください。

```powershell
uv --version
```

エラーになる場合は、uvが正しくインストールされているか確認してください。

公式ドキュメント：

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## Pythonのバージョンが違う

以下で確認できます。

```powershell
python --version
```

または、

```powershell
uv run python --version
```

この教材では、各回の環境設定に記載されているPythonバージョンを使用してください。

---

## パッケージが見つからない

まず対象ディレクトリで、

```powershell
uv sync
```

を実行してください。

その後、VS CodeでNotebookのPythonインタープリターがプロジェクトの環境になっているか確認してください。

---

## NotebookでPython環境を選択できない

VS Codeに以下の拡張機能がインストールされているか確認してください。

* Python
* Jupyter

VS Codeの拡張機能画面からインストールできます。

---

# 推奨環境

この教材は主に以下の環境を想定しています。

| 項目         | 推奨                      |
| ---------- | ----------------------- |
| OS         | Windows / macOS / Linux |
| Python     | 3.13                    |
| エディタ       | Visual Studio Code      |
| Python環境管理 | uv                      |
| Notebook   | Jupyter Notebook        |
| ブラウザ実行     | Google Colab            |
| バージョン管理    | Git / GitHub            |

※ 各回によって必要なパッケージやPythonバージョンが異なる場合があります。各ディレクトリのREADMEおよび `pyproject.toml` を確認してください。

---

# 免責事項

このリポジトリは、Pythonおよび土木工学分野の学習を目的とした教材です。

掲載しているコードや説明について、正確性・完全性・動作を保証するものではありません。

特に土木工学に関する計算結果を実務・設計・施工・安全性の判断に利用する場合は、必ず専門家による確認や公式資料・基準類の確認を行ってください。

---

# ライセンス

このリポジトリは **MIT License** のもとで公開しています。

詳細は [`LICENSE`](./LICENSE) ファイルをご確認ください。


---

# Author

**skyblueao77**

土木工学を学びながら、Python・データ分析・AIなどの技術を学習しています。

Qiitaでも「土木のためのPython入門」を連載しています。

Qiita：

[https://qiita.com/skyblueao77](https://qiita.com/skyblueao77)

GitHub：

[https://github.com/skyblueao77](https://github.com/skyblueao77)

---

## 関連リンク

* [Qiita - 土木のためのPython入門](https://qiita.com/skyblueao77)
* [GitHub - civil-engineering-python](https://github.com/skyblueao77/civil-engineering-python)
* [uv 公式ドキュメント](https://docs.astral.sh/uv/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Google Colab](https://colab.research.google.com/)

---

## 今後の予定

今後、以下の内容を追加していく予定です。

* matplotlibによるデータ可視化
* NumPyによる数値計算
* SciPyによる科学技術計算
* 土木データの実践的な分析
* 国土交通省などの公開データの利用
* GIS・GeoPandas
* 土木工学におけるPythonの活用例
* 生成AIを利用したPython開発
* AIが生成したコードの検証方法

このリポジトリを、**土木学生がPythonを学び始めるための実践的な教材**として少しずつ発展させていきます。
