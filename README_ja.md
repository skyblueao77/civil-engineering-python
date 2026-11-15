
# Python for Civil Engineering (土木のためのPython 入門)

[English README](README.md)

土木工学、環境工学、都市工学などを学ぶ学生のための、Python入門学習用リソースです。

本プロジェクトは、これからPythonの学習を始める学生向けに設計されています。以下のステップを通して、土木分野におけるPython活用の基礎を網羅的に学ぶことができます。

**環境構築 → Pythonの基礎 → データ処理 → 視覚化 → 数値計算 → 土木工学への応用**

本リポジトリは、Qiitaの記事、Jupyter Notebook、Pythonスクリプトとあわせて活用することを想定しています。

---

## 目次

* [対象読者](#対象読者)
* [学べること](#学べること)
* [記事と学習教材](#記事と学習教材)
* [リポジトリ構成](#リポジトリ構成)
* [環境構築](#環境構築)
  * [方法1: Google Colabを使う](#方法1-google-colabを使う)
  * [方法2: uv + PyCharmを使う](#方法2-uv--pycharmを使う)
* [依存パッケージ](#依存パッケージ)
* [再現性と依存関係の管理](#再現性と依存関係の管理)
* [セキュリティとコード品質](#セキュリティとコード品質)
* [Pythonの実行方法](#pythonの実行方法)
* [Jupyter Notebookについて](#jupyter-notebookについて)
* [土木工学におけるPython](#土木工学におけるpython)
* [AI時代のPython学習](#ai時代のpython学習)
* [推奨する学習ロードマップ](#推奨する学習ロードマップ)
* [推奨環境](#推奨環境)
* [トラブルシューティング](#トラブルシューティング)
* [開発者の方へ](#開発者の方へ)
* [免責事項](#免責事項)
* [ライセンス](#ライセンス)
* [著者](#著者)
* [関連リンク](#関連リンク)
* [今後の予定](#今後の予定)

---

## 対象読者

本プロジェクトは以下のような方を対象としています。

* 土木工学を専攻する学生
* 環境工学を専攻する学生
* 都市工学を専攻する学生
* Pythonの学習を始めたい学生
* プログラミング初心者
* 土木分野でデータ分析を行いたい学生
* NumPy、pandas、Matplotlib、SciPyを学びたい学生
* AIが生成したPythonコードの仕組みを理解し、検証したい学生
* Pythonが土木分野でどのように活用できるか知りたい学生

高度なプログラミング経験は不要です。

---

## 学べること

本プロジェクトを通して、工学やデータ分析にPythonを活用するための基礎知識を習得できます。

主なテーマは以下の通りです。

* Python開発環境の構築方法
* Pythonの基本構文とプログラミングの概念
* pandasによるデータ処理
* Matplotlibによるデータの可視化
* NumPyによる数値計算
* SciPyによる科学技術計算
* GeoPandasによるGIS・地理空間データの扱い
* 構造力学・土木工学の課題に対するPythonの応用（単純梁の解析など）
* Jupyter Notebookの使い方
* uvを用いたPython環境および依存関係の管理
* AIが生成したPythonコードの理解と検証

今後の教材では、実際の公共データセットを用いた土木データ分析、より高度な構造解析や数値計算などにも展開していく予定です。

---

## 記事と学習教材

連載全体の案内ページはこちら: [【連載一覧】土木のためのPython入門](https://qiita.com/skyblueao77/items/ea31e9890f6368b25e19)

現在利用可能な教材は以下の通りです。

| 巻 | テーマ | GitHub教材 | Qiita記事 |
| --- | --- | --- | --- |
| Vol.1 | 環境構築編（Google Colab・uv） | リポジトリルート | [土木のためのPython入門① 環境構築編（Google Colab・uv）](https://qiita.com/skyblueao77/items/c4a0e7ddc9913c55994f) |
| Vol.2 | 基本文法編 | `./qiita_02_basic/` | [土木のためのPython入門② 基本文法編](https://qiita.com/skyblueao77/items/65abd5ad5befa474ee5f) |
| Vol.3 | pandas入門編 | `./qiita_03_pandas/` | [土木のためのPython入門③ pandas入門編](https://qiita.com/skyblueao77/items/c8c4902706f97415d1ec) |
| Vol.4 | Matplotlib入門編 | `./qiita_04_matplotlib/` | [土木のためのPython入門④ matplotlib入門編](https://qiita.com/skyblueao77/items/45da8225a78e99d28cc5) |
| Vol.5 | NumPy入門 | `./qiita_05_numpy/` | [土木のためのPython入門⑤ NumPy入門｜配列・行列・数値計算を基礎から解説](https://qiita.com/skyblueao77/items/dfc9a12c147230814424) |
| Vol.6 | SciPyで科学技術計算 | `./qiita_06_scipy/` | [土木のためのPython入門⑥ SciPyで科学技術計算｜補間・数値積分・数値微分・最適化](https://qiita.com/skyblueao77/items/a1306b9cd6c06671191b) |
| Vol.7 | GeoPandas入門編 | `./qiita_07_geopandas/` | [土木のためのPython入門⑦ GeoPandas入門編](https://qiita.com/skyblueao77/items/3b64dff2020415332445) |
| Vol.8 | 構造解析編（単純梁） | `./qiita_08_beam/` | [土木のためのPython入門⑧ 単純梁をPythonで解析してみよう](https://qiita.com/skyblueao77/items/cd31c475fdbf9d5a80f6) |
| Vol.9 | 構造解析編（2次元トラス） | `./qiita_09_truss/` | 準備中（第9回記事は未作成） |

各巻には基本的に以下が含まれます。

* 解説用のQiita記事
* インタラクティブに学べるJupyter Notebook
* サンプルコードが含まれたPythonスクリプト
* その巻固有の情報をまとめたREADME


---

## リポジトリ構成

本リポジトリでは、各巻で統一された構成を採用しています。

```text
civil-engineering-python/
│
├── .github/
├── .gitignore
├── .python-version
├── .pre-commit-config.yaml
│
├── pyproject.toml
├── uv.lock
│
├── README.md
├── README_ja.md
├── LICENSE
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
│
├── qiita_XX_topic/
│   ├── README.md
│   ├── *.ipynb
│   └── *.py
│
└── ...

```

各 `qiita_XX_topic/` ディレクトリは、基本的に「土木のためのPython入門」シリーズの各巻に対応しています。

Python環境は、以下のファイルを用いてプロジェクトルートで一括管理されています。

```text
pyproject.toml
uv.lock
.python-version

```

巻ごとに個別環境を作成するのではなく、シリーズ全体で1つの統一されたPython環境を共有しています。

---

## 環境構築

本リポジトリでは、Python環境およびプロジェクトの依存関係管理に [uv](https://docs.astral.sh/uv/) を採用しています。

基本構成は以下の通りです。

* Python 3.13
* uv
* Jupyter
* ipykernel
* NumPy
* pandas
* Matplotlib
* SciPy
* GeoPandas

学習教材の利用方法は、大きく分けて2通りあります。

---

### 方法1: Google Colabを使う

**「まずは手軽にPythonを試してみたい」という方におすすめの方法です。**

Google Colab（Google Colaboratory）を使用すると、ローカル環境にPythonをインストールすることなく、ウェブブラウザ上で直接Pythonコードを実行できます。

対応するJupyter Notebookをアップロードまたは開くだけで、対話的にコードを実行することが可能です。

以下のような方に適しています。

* とりあえずPythonを動かしてみたい方
* ローカルの環境構築なしで手軽に学びたい方
* パソコンにPythonをインストールしたくない方
* ブラウザ上でJupyter Notebookを実行したい方

利用はこちらから:

[Google Colab](https://colab.research.google.com/)

---

### 方法2: uv + PyCharmを使う

**「今後も継続してPythonを勉強したい」「ローカルでリポジトリを使って作業したい」という方におすすめの方法です。**

本プロジェクトでは、リポジトリ全体のPython環境を `uv` で管理しています。

`uv` を使うことで、Pythonのバージョン管理、仮想環境の作成、依存パッケージの管理をまとめて行うことができます。

### 1. PyCharmのインストール

PyCharmを使用する場合は、公式サイトからダウンロードしてインストールしてください。

[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

### 2. uvのインストール

公式ドキュメントに従って `uv` をインストールします。

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

インストール後、以下のコマンドで動作確認を行います。

```powershell
uv --version

```

バージョン番号が表示されれば、正常にインストールされています。

### 3. リポジトリのクローン

Gitがインストールされている場合は、リポジトリをクローンします。

```powershell
git clone https://github.com/skyblueao77/civil-engineering-python.git

```

ディレクトリに移動します。

```powershell
cd civil-engineering-python

```

### 4. Python環境の構築

プロジェクトのルートディレクトリで以下のコマンドを実行します。

```powershell
uv sync

```

`uv sync` を実行すると、`pyproject.toml` と `uv.lock` に基づいてプロジェクト環境が自動的に構築・更新されます。

なお、本リポジトリでは巻ごとに個別の環境を作成しません。

**シリーズ全体で共通の1つのPython環境を使用します。**

### 5. Pythonバージョンの確認

以下のコマンドで指定のバージョンになっているか確認します。

```powershell
uv run python --version

```

現在、本リポジトリでは Python 3.13 をターゲットにしています。

### 6. JupyterLabの起動

プロジェクトルートから以下を実行します。

```powershell
uv run jupyter lab

```

または、Jupyter NotebookをサポートしているIDE（PyCharm等）で直接 `.ipynb` ファイルを開くことも可能です。

### 7. 学習教材を開く

勉強したい巻に対応するディレクトリを選択します。

（例）

```text
qiita_03_pandas/
├── README.md
├── qiita_doboku_3.ipynb
└── qiita_doboku_3.py

```

READMEを読みながら、Notebookを実行したりサンプルコードを書き換えたりして学習を進めてください。

---

## 依存パッケージ

現在利用している主なパッケージは以下の通りです。

| パッケージ | 用途 |
| --- | --- |
| NumPy | 数値計算・配列処理 |
| pandas | 表形式データの処理 |
| Matplotlib | データの可視化（グラフ描画） |
| SciPy | 科学技術計算 |
| GeoPandas | GIS・地理空間データの処理 |
| Jupyter | ノートブック環境 |
| ipykernel | Pythonカーネル |

使用されている具体的な依存関係やバージョンは、リポジトリルートの管理ファイルによって固定・解決されています。

---

## 再現性と依存関係の管理

教育用コードや数値計算環境を共有する際、環境の「再現性」は非常に重要です。

本リポジトリでは、以下のファイルを用いてPython環境を管理しています。

| ファイル | 用途 |
| --- | --- |
| `pyproject.toml` | プロジェクト設定および依存関係の定義 |
| `uv.lock` | 解決された依存パッケージの正確なバージョン記録 |
| `.python-version` | プロジェクトで使用するPythonバージョンの指定 |

各巻ごとに環境を分けるのではなく、ルートにある単一の環境を使用します。

リポジトリをクローンした後は、以下を実行するだけで環境が再現されます。

```powershell
uv sync

```

ロックファイル（`uv.lock`）を使用することで、開発環境ごとの予期せぬパッケージバージョンのズレを防ぐことができます。

ただし、再現性の確保がすべてのセキュリティ脆弱性の排除を保証するわけではありません。開発ツールやパッケージは定期的に更新し、必要に応じてセキュリティアドバイザリを確認することをお勧めします。

---

## セキュリティとコード品質

本リポジトリでは、学習者や利用者が安心してコードを実行できるよう、セキュリティ管理・依存関係の脆弱性監視・環境の再現性・コード品質の自動検証を継続的に実施しています。

### 安心してご利用いただくための取り組み

* **不要な外部通信や機密情報の非扱い**: 教材スクリプト・Notebook はローカル環境（または Google Colab）での数値計算・データ可視化を中心としており、認証情報の取得や外部へのデータ送信は行いません。
* **ロックファイルによる再現性と整合性検証**: `uv.lock` にパッケージバージョンとハッシュを記録しています。より厳密に環境を構築・検証したい場合は `uv sync --locked` を使用できます。
* **GitHub セキュリティ機能**:
  * **Security Policy / Private Vulnerability Reporting**: 脆弱性発見時の非公開報告窓口
  * **Dependabot Alerts & Updates**: `uv` および GitHub Actions の依存関係を週次で自動監視・更新
  * **Secret Scanning & Push Protection**: APIキー・秘密鍵・`.env` 等の機密情報の誤コミットを検知・ブロック（`.gitignore` でも除外設定済み）
  * **CodeQL**: 静的解析によるコードスキャンを運用
* **CI による自動検証（GitHub Actions）**:
  * ワークフロー（[`.github/workflows/ci.yml`](.github/workflows/ci.yml)）は最小権限（`contents: read`）かつ Action のコミット SHA 固定で運用しています。
  * すべての push / Pull Request で `uv lock --check`、Ruff のセキュリティルール（`S`: flake8-bandit）、および `pytest --nbmake` による全 Notebook の実行テストを実施しています。
  * 定期実行（毎週）および変更時に **`pip-audit --strict`** を実行し、依存パッケージに既知の脆弱性（CVE）がないか検査しています。

関連リンク:

* [Security Policy](https://github.com/skyblueao77/civil-engineering-python/security/policy)
* [Security Advisories](https://github.com/skyblueao77/civil-engineering-python/security/advisories)
* [Dependabot Alerts](https://github.com/skyblueao77/civil-engineering-python/security/dependabot)
* [Secret Scanning](https://github.com/skyblueao77/civil-engineering-python/security/secret-scanning)

### 利用者向けの安全な使い方のポイント

1. **公式リポジトリから取得する**: `https://github.com/skyblueao77/civil-engineering-python` からクローンするか、各巻 README の公式 **Open in Colab** リンクをご利用ください。
2. **`uv sync --locked` を活用する**: ローカル環境で依存関係を構築する際、`uv sync --locked` を使うと `uv.lock` と一致しない改変や意図しないバージョン変更を防げます。
3. **独自データの扱いに注意する**: ご自身の業務データや位置情報、APIキーなどを扱う場合は、リポジトリへコミットしないようご注意ください（`.env` 等は `.gitignore` で除外しています）。

### Pre-commit チェック

本リポジトリでは `pre-commit` を使用して開発チェックを自動化しています。

設定ファイル:

```text
.pre-commit-config.yaml
```

開発ワークフローには以下のツールが含まれています。

* **Ruff**: 静的解析、コード品質チェック、および Bandit セキュリティルール（`S`）検査
* **uv lock --check**: `pyproject.toml` と `uv.lock` の整合性確認
* **Pytest / nbmake**: 自動テストおよび全 Jupyter Notebook の実行テスト
* **pip-audit**: 依存パッケージの既知脆弱性チェック（`uv run pip-audit --strict`）

手動で事前にチェックを実行したい場合は、以下を実行します。

```bash
uv run pre-commit run --all-files
```

これらのチェックにより、フォーマット崩れ、文法エラー、セキュリティ上の懸念、ロックファイルの不整合、スクリプトや Notebook の実行エラーなどを事前に検知できます。

### セキュリティの範囲について

本リポジトリは学習・教育を目的としたものであり、高度なセキュリティを要する本番稼働システムではありません。

記載されているセキュリティ機能や開発チェックは、リポジトリの衛生状態、依存関係の監視、再現性、およびコード品質を向上させるためのものです。

これらは、本リポジトリや依存する全パッケージに完全に脆弱性がないことを永久に保証するものではありません。

---

## Pythonの実行方法

Pythonスクリプトは、プロジェクトルートから `uv run` を使用して実行できます。

（例）

```powershell
uv run python qiita_03_pandas/qiita_doboku_3.py

```

`uv run` を使用することで、プロジェクトで正しく管理された環境のPythonが確実に使用されます。

---

## Jupyter Notebookについて

本教材では、主にJupyter Notebook（`.ipynb`）形式の教材を提供しています。

Notebookを使用すると、以下のようなサイクルで学習を進めることができます。

```text
コードを書く
    ↓
実行する
    ↓
結果を確認する
    ↓
コードを修正してみる
    ↓
再度実行する

```

コードと出力結果を1ステップずつ確認できるため、プログラミング初心者にとって非常に扱いやすい形式です。

最初からすべてを完璧に理解しようとする必要はありません。

サンプルコードを少しずついじって動作の変化を試すことが、Python習得の近道です。

---

## 土木工学におけるPython

土木工学では、以下のように多種多様なデータを扱います。

* 降水量データ
* 水位データ
* 河川流量データ
* 交通量データ
* 地形データ
* 測量データ
* 土質・地盤データ
* 構造物モニタリングデータ
* 各種実験データ
* 地理空間情報（GISデータ）

Pythonを活用することで、以下のような一連の業務・解析フローを効率化できます。

```text
データを読み込む
    ↓
データを整理・整形（クレンジング）する
    ↓
計算処理を行う
    ↓
データを分析する
    ↓
結果をグラフ等で可視化する
    ↓
分析結果を考察・評価する

```

本プロジェクトでは、単にPythonの文法を覚えるだけでなく、以下を意識した学びを提供します。

> **「土木分野でPythonをどのように活かすか？」**

プログラミングの基礎と、実践的な工学解析を結びつけることを目指しています。

---

## AI時代のPython学習

近年、生成AIを使えば簡単にPythonコードを出力できるようになりました。

そのため、次のような疑問を持つ方も多いでしょう。

> **「AIがコードを書いてくれるなら、人間がPythonを学ぶ必要はあるのか？」**

本プロジェクトは、AIを活用したプログラミングを否定するものではありません。

むしろ、以下の能力を養うことが重要だと考えています。

> **「AIが生成したコードの内容を理解し、正しいか検証し、必要に応じて修正できる力」**

仮にAIがコードを作成してくれたとしても、エンジニアや学生自身が次のような点を判断する必要があります。

* どのような計算が行われているか？
* 入力データは妥当か？
* 物理量や単位の扱いは正しいか？
* なぜエラーが発生したのか？
* 選択された数値計算手法は適切か？
* 算出された数値は工学的に妥当か？
* 土木工学の観点から見て意味の通る結果か？

工学の現場において、「プログラムがエラーなく動いたこと」と「解析結果が正しく安全であること」は同義ではありません。

```text
コードがエラーなく動いた
        ≠
工学的解析として正しい

```

したがって、Pythonの知識は「コードをゼロから書くため」だけでなく、「AIが提示したコードを理解し、適切に評価するため」にも欠かせないスキルであり続けます。

プログラミング技術と同時に、計算結果を論理的に検証する力を身につけることを目指しましょう。

---

## 推奨する学習ロードマップ

学習を進める際は、以下の順序を推奨しています。

```text
環境構築
    ↓
Pythonの基礎
    ↓
データ処理
  (pandas)
    ↓
データの可視化
 (Matplotlib)
    ↓
数値計算の基礎
 (NumPy / SciPy)
    ↓
土木データの分析
    ↓
GIS・空間データ
    ↓
高度な工学応用解析

```

このロードマップは各巻の番号と独立して設計されています。

新しいコンテンツが追加された場合も、このロードマップの適切なステップに組み込んで学習を進めることができます。

一度にすべてをマスターする必要はありません。

> **コードを書く → 実行する → 結果を見る → 少し変えてみる → 再実行する**

というサイクルを繰り返しながら学んでいきましょう。

---

## 推奨環境

本プロジェクトでは、主に以下の環境を想定しています。

| 項目 | 推奨仕様 |
| --- | --- |
| OS | Windows / macOS / Linux |
| Python | 3.13 |
| IDE | PyCharm またはその他のPython対応IDE |
| 環境管理ツール | uv |
| ノートブック | Jupyter Notebook / JupyterLab |
| ブラウザ実行環境 | Google Colab |
| バージョン管理 | Git / GitHub |

Pythonやパッケージのバージョンは、リポジトリルートの設定ファイルに従って管理されています。

---

## トラブルシューティング

### `uv` コマンドが見つからない（Command Not Found）

`uv` がインストールされているか確認してください。

```powershell
uv --version

```

認識されない場合は、公式ドキュメントに従って再インストールを行ってください。

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

### Pythonのバージョンが異なる

プロジェクトで使用されているPythonバージョンを確認します。

```powershell
uv run python --version

```

リポジトリルートにある `.python-version` および設定ファイルによって指定されたバージョンが適用されます。

---

### パッケージが見つからない（ModuleNotFoundError）

まず、リポジトリのルートディレクトリで以下を実行してください。

```powershell
uv sync

```

その後、使用しているIDEやJupyter環境が、本プロジェクトで構築されたPython環境を参照しているか確認してください。

---

### NotebookでPython環境を選択できない

プロジェクトの環境がJupyterカーネルとして表示されない場合は、手動で登録することができます。

プロジェクトルートで以下を実行します。

```powershell
uv run python -m ipykernel install --user --name civil-engineering-python --display-name "Python (civil-engineering-python)"

```

実行後、JupyterまたはIDEを再起動し、カーネル一覧から以下を選択してください。

```text
Python (civil-engineering-python)

```

---

## 開発者の方へ

本リポジトリでは、Python環境および依存関係の管理に `uv` を、開発チェックの自動化に `pre-commit` を使用しています。

### 1. 開発環境の構築

リポジトリをクローンします。

```bash
git clone https://github.com/skyblueao77/civil-engineering-python.git
cd civil-engineering-python

```

環境を同期します。

```bash
uv sync

```

Gitフックを有効化します。

```bash
uv run pre-commit install

```

---

### 2. コード品質の自動化とテスト

コミット時に、設定されたpre-commitフックが開発チェックを自動的に行います。

ワークフローには以下が含まれます。

* **Ruff**: 静的解析・コード品質チェック
* **Pytest**: 自動テストの実行
* **nbmake**: Jupyter Notebookの実行テスト

すべてのpre-commitチェックを手動で実行する場合:

```bash
uv run pre-commit run --all-files

```

テストの実行:

```bash
uv run pytest --nbmake

```

Ruffによるチェックの実行:

```bash
uv run ruff check .

```

Ruffで修正可能な問題を自動修正する場合:

```bash
uv run ruff check --fix .

```

コントリビュートを検討されている方は、事前に `./CONTRIBUTING.md` もご確認ください。

---

## 免責事項

本リポジトリは、Pythonおよびその土木工学への応用を学ぶための**教育用リソース**です。

提供されているコードや解説の正確性、完全性、信頼性を永久に保証するものではありません。

本リポジトリのコードや計算例を、十分な検証なしに実務上の重要な工学的判断に直接使用しないでください。

特に、実際の業務、設計、施工、インフラ管理、防災・安全に関わる計算に利用する場合は、必ず有資格者・専門家に相談し、適用される法令、示方書、基準、公式文書、および各種ガイドラインに基づいて結果を検証してください。

---

## ライセンス

本リポジトリは **MIT License** のもとで公開されています。

詳細は `./LICENSE` ファイルを参照してください。

---

## 著者

**skyblueao77**

Python、データ分析、AIなどの技術を学んでいる土木工学専攻の学生。

「土木のためのPython」シリーズはQiitaでも連載・公開しています。

* [Qiita](https://qiita.com/skyblueao77)
* [【連載一覧】土木のためのPython入門](https://qiita.com/skyblueao77/items/ea31e9890f6368b25e19)
* [GitHub](https://github.com/skyblueao77/civil-engineering-python)

---

## 関連リンク

### プロジェクト関連

* [Qiita - skyblueao77](https://qiita.com/skyblueao77)
* [【連載一覧】土木のためのPython入門](https://qiita.com/skyblueao77/items/ea31e9890f6368b25e19)
* [GitHub - civil-engineering-python](https://github.com/skyblueao77/civil-engineering-python)

### Python環境・開発ツール

* [Python 公式](https://www.python.org/)
* [uv ドキュメント](https://docs.astral.sh/uv/)
* [PyCharm 公式](https://www.jetbrains.com/pycharm/)
* [Jupyter 公式](https://jupyter.org/)
* [Google Colab](https://colab.research.google.com/)

### 主要Pythonライブラリ

* [NumPy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [SciPy](https://scipy.org/)
* [GeoPandas](https://geopandas.org/)

---

## 今後の予定

今後は以下のようなテーマを扱っていく予定です。

* 土木実務に役立つデータ分析手法
* 実際のデータセットを用いた実践的解析
* 公共データ（国土交通省などのオープンデータ）の活用
* 応用的なGIS・地理空間データ処理
* 統計解析の基礎と応用
* 構造・水理などの工学課題に対する数値計算手法
* 機械学習・AIの土木工学への応用
* AI生成コードのデバッグ・検証テクニック
* より高度な数値解析プログラミング

基礎的なPythonの習得から始まり、最終的には実際の土木データや解析手法を自在に扱えるようになる実践的な学習リソースを目指していきます。

---

## コントリビューション（貢献）について

ご意見、改善のご提案、修正の指摘などは大歓迎です！

誤字や内容の誤りを見つけた場合や、教材の改善案がある場合は、Issueを立てていただくか、`./CONTRIBUTING.md` のガイドラインに沿ってPull Requestをお送りください。

---

**Python for Civil Engineering（土木のためのPython 入門）**

Pythonの基礎から、実際の土木データの理解・分析まで。