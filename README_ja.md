
# 土木工学のための Python 入門 (Python for Civil Engineering)

[ English Version](README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Managed by uv](https://img.shields.io/badge/python--package--manager-uv-de5b88.svg)](https://docs.astral.sh/uv/)
[![Security Policy](https://img.shields.io/badge/Security-Policy-green.svg)](https://github.com/skyblueao77/civil-engineering-python/security/policy)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-green.svg)](https://github.com/skyblueao77/civil-engineering-python/security/dependabot)
[![Secret Scanning](https://img.shields.io/badge/Secret%20Scanning-enabled-green.svg)](https://github.com/skyblueao77/civil-engineering-python/security/secret-scanning)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

土木工学を学ぶ学生のための Python 入門用学習教材リポジトリです。

本プロジェクトは、これから Python の学習を始める土木専攻の学生を対象としています。以下のステップに沿って、土木分野における Python 活用の基礎を網羅的に学べるよう構成されています。

**環境構築 → Python の基礎 → データ処理 → 可視化 → 数値計算**

本リポジトリは、Qiita に連載中の解説記事、Jupyter Notebook、および Python スクリプトと連動して学習を進められるよう設計されています。

---

## 目次

- [対象読者](#対象読者)
- [学べること](#学べること)
- [解説記事一覧 (Qiita)](#解説記事一覧-qiita)
  - [Vol.1 環境構築編](#vol1-環境構築編)
  - [Vol.2 Python 基礎編](#vol2-python-基礎編)
  - [Vol.3 pandas 入門編](#vol3-pandas-入門編)
  - [Vol.4 Matplotlib 入門編](#vol4-matplotlib-入門編)
  - [Vol.5 NumPy 入門編](#vol5-numpy-入門編)
  - [Vol.6 SciPy 入門編](#vol6-scipy-入門編)
- [リポジトリの構成](#リポジトリの構成)
- [環境構築](#環境構築)
  - [方法 1: Google Colab を使う場合](#方法-1-google-colab-を使う場合)
  - [方法 2: uv + PyCharm を使う場合（ローカル環境）](#方法-2-uv--pycharm-を使う場合ローカル環境)
- [`uv sync` について](#uv-sync-について)
- [依存パッケージ](#依存パッケージ)
- [環境の再現性と依存関係管理](#環境の再現性と依存関係管理)
- [セキュリティとコード品質](#セキュリティとコード品質)
- [Python スクリプトの実行](#python-スクリプトの実行)
- [Jupyter Notebook について](#jupyter-notebook-について)
- [土木工学における Python の活用](#土木工学における-python-の活用)
- [AI 時代における Python 学習の意義](#ai-時代における-python-学習の意義)
- [推奨される学習ロードマップ](#推奨される学習ロードマップ)
- [推奨環境](#推奨環境)
- [トラブルシューティング](#トラブルシューティング)
- [開発者向け情報](#開発者向け情報)
- [免責事項](#免責事項)
- [ライセンス](#ライセンス)
- [著者](#著者)
- [関連リンク](#関連リンク)
- [今後の更新予定](#今後の更新予定)

---

## 対象読者

本プロジェクトは、以下のような方を対象としています。

* 土木工学（社会基盤工学・都市工学等）を学ぶ学生
* これから Python の学習を始めたいプログラミング初心者
* 土木分野でのデータ分析や数値シミュレーションに興味がある方
* NumPy、pandas、Matplotlib、SciPy などの標準的なライブラリを学びたい方
* AI（生成AI）が出力した Python コードの意味を理解し、検証できるようになりたい方
* 「土木分野で Python がどう役立つのか」を知りたい方

---

## 学べること

現在、以下のコンテンツを提供しています。

| 巻数 | コンテンツ名 | 主なテーマ |
| ------ | ------- | ----------- |
| Vol.1 | 環境構築編 | Google Colab / uv / PyCharm / Python 開発環境 |
| Vol.2 | Python 基礎編 | 変数 / データ型 / 条件分岐 / 繰り返し処理 / リスト |
| Vol.3 | pandas 入門編 | DataFrame / Series / データ抽出 / CSV操作 / 基本統計量 |
| Vol.4 | Matplotlib 入門編 | 折れ線グラフ / 散布図 / 軸設定 / 凡例 / グラフの保存 |
| Vol.5 | NumPy 入門編 | ndarray / 配列演算 / ベクトル化 / 数値計算の基礎 |
| Vol.6 | SciPy 入門編 | 補間処理 / 数値積分 / 数値微分 / 科学技術計算 |

今後は、実際の土木データを用いた分析、GIS（空間情報）、実データ解析、高度な数値シミュレーションなどのコンテンツを追加予定です。

---

## 解説記事一覧 (Qiita)

### Vol.1 環境構築編

**【土木のためのPython入門】Vol.1 環境構築編（Google Colab / uv 入門）**

学習を始めるための Python 開発環境のセットアップ方法について解説しています。

主なトピック：
* Google Colab の使い方
* PyCharm の導入
* uv による環境構築
* Python 仮想環境の仕組み

[👉 Qiita 記事: Vol.1 環境構築編](https://qiita.com/skyblueao77/items/c4a0e7ddc9913c55994f)

---

### Vol.2 Python 基礎編

**【土木のためのPython入門】Vol.2 Pythonの基本文法**

Python を扱う上で必要となる最重要の基本文法を解説しています。

主なトピック：
* 変数とデータ型
* 四則演算と数値処理
* 条件分岐（if 文）
* 繰り返し処理（for / while 文）
* リスト操作

※土木工学での応用を意識した実践的な例題を扱っています。

[👉 Qiita 記事: Vol.2 Pythonの基本文法](https://qiita.com/skyblueao77/items/65abd5ad5befa474ee5f)

---

### Vol.3 pandas 入門編

**【土木のためのPython入門】Vol.3 pandasによるデータ処理入門**

土木分野でよく扱う表形式データ（観測データ等）を pandas で効率的に処理する方法を解説しています。

主なトピック：
* DataFrame と Series の扱い方
* データの作成と参照
* 行・列の抽出と条件フィルタリング
* 基本統計量の算出
* CSV ファイルの読み込み・書き出し

[👉 Qiita 記事: Vol.3 pandasによるデータ処理入門](https://qiita.com/skyblueao77/items/c8c4902706f97415d1ec)

---

### Vol.4 Matplotlib 入門編

**【土木のためのPython入門】Vol.4 Matplotlibによるデータ可視化入門**

pandas 等で整理した土木データを Matplotlib を用いてグラフとして可視化する方法を解説しています。

主なトピック：
* 折れ線グラフ・散布図の作成
* 軸ラベル、タイトル、凡例の設定
* グラフの日本語描画対応
* 画像ファイルとしての保存方法

[👉 Qiita 記事: Vol.4 Matplotlibによるデータ可視化入門](https://qiita.com/skyblueao77/items/45da8225a78e99d28cc5)

---

### Vol.5 NumPy 入門編

**【土木のためのPython入門】Vol.5 NumPy入門 — 配列・行列演算と数値計算の基礎**

土木数値計算の基礎となる NumPy の扱い方について解説しています。

主なトピック：
* ndarray（多次元配列）の基礎
* 配列の作成と形状変更
* インデックス参照とスライス
* 要素ごとの演算とベクトル化処理
* 基本的な数値計算手法

[👉 Qiita 記事: Vol.5 NumPy入門 — 配列・行列演算と数値計算の基礎](https://qiita.com/skyblueao77/items/dfc9a12c147230814424)

---

### Vol.6 SciPy 入門編

**【土木のためのPython入門】Vol.6 科学技術計算ライブラリ SciPy 入門 — 補間・数値積分・数値微分・最適化**

NumPy をベースにした、より発展的な科学技術計算用ライブラリ SciPy について解説しています。

主なトピック：
* データ点の補間処理（線形補間・スプライン補間など）
* 数値積分と数値微分
* 高度な科学技術計算
* NumPy と SciPy の使い分け

[👉 Qiita 記事: Vol.6 科学技術計算ライブラリ SciPy 入門](https://qiita.com/skyblueao77/items/a1306b9cd6c06671191b)

---

## リポジトリの構成

本リポジトリは、**プロジェクト全体で単一の Python 共通環境**を使用しています。

```text
civil-engineering-python/
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── README_ja.md
├── LICENSE
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── .pre-commit-config.yaml
│
├── qiita_02_basic/
│   ├── README.md
│   ├── civil_engineering_python_intro_02.ipynb
│   └── qiita_doboku_2.py
│
├── qiita_03_pandas/
│   ├── README.md
│   ├── qiita_doboku_3.ipynb
│   └── qiita_doboku_3.py
│
├── qiita_04_matplotlib/
│   ├── README.md
│   ├── qiita_doboku_4.ipynb
│   └── qiita_doboku_4.py
│
├── qiita_05_numpy/
│   ├── README.md
│   └── qiita_doboku_5.ipynb
│
└── qiita_06_scipy/
    ├── README.md
    ├── qiita_doboku_6.ipynb
    └── qiita_doboku_6.py

```

Python 環境の設定ファイルはプロジェクトルートで一元管理されています。

```text
pyproject.toml
uv.lock
.python-version

```

各話のディレクトリには、それぞれのテーマに対応する Jupyter Notebook（`.ipynb`）、Python スクリプト（`.py`）、および README が配置されています。

---

## 環境構築

本リポジトリでは、パッケージおよび環境管理ツールとして [`uv`](https://docs.astral.sh/uv/) を採用しています。

本プロジェクトの主要な開発構成：

* Python 3.13
* uv
* Jupyter / ipykernel
* PyCharm
* NumPy / pandas / Matplotlib / SciPy

なお、ローカルに環境を作らず手軽に試したい場合は、Google Colab を利用することも可能です。

---

### 方法 1: Google Colab を使う場合

**「まずは手軽に Python を動かしてみたい」という方にオススメの方法です。**

Google Colab を使うと、Web ブラウザ上だけで Python コードを実行できます。

各記事に設置されている「Open in Colab」ボタンから Notebook を開くことで、自分のパソコンに Python や Jupyter をインストールすることなく学習をスタートできます。

#### こんな方にオススメ：

* まずは気軽に Python を触ってみたい方
* ローカル環境の構築でつまずきたくない方
* PC のストレージを圧迫したくない方
* ブラウザ上でサクサク Notebook を動かしたい方

---

### 方法 2: uv + PyCharm を使う場合（ローカル環境）

**「本格的に Python を学び、継続的に開発や解析を行いたい」という方にオススメの方法です。**

本プロジェクトでは `uv` を使用してリポジトリ全体の Python 環境を管理しています。

`uv` は、Python のバージョン切り替え、仮想環境の作成、パッケージ導入を高速かつ一元的に行えるモダンなツールです。

#### 1. PyCharm のインストール

PyCharm を利用する場合は、公式サイトよりインストールしてください。

[PyCharm 公式サイト](https://www.jetbrains.com/pycharm/)

#### 2. uv のインストール

公式ドキュメントの手順に従って `uv` をインストールします。

[uv 公式ドキュメント](https://docs.astral.sh/uv/)

Windows（PowerShell）の場合は、公式に案内されているコマンドでインストール可能です。

インストール後、以下のコマンドで動作を確認します。

```powershell
uv --version

```

バージョン番号が表示されればインストール完了です。

#### 3. リポジトリのクローン

Git がインストールされている環境で、リポジトリをクローンします。

```powershell
git clone [https://github.com/skyblueao77/civil-engineering-python.git](https://github.com/skyblueao77/civil-engineering-python.git)

```

クローン後、ディレクトリに移動します。

```powershell
cd civil-engineering-python

```

#### 4. Python 環境の構築

**プロジェクトのルートディレクトリで** 以下のコマンドを実行します。

```powershell
uv sync

```

`uv sync` を実行すると、`pyproject.toml` および `uv.lock` に基づいて必要な依存パッケージと仮想環境が自動的にセットアップされます。

※各話ごとに個別環境を作る必要はありません。**シリーズ全体で 1 つの共通環境を使用します。**

#### 5. Python バージョンの確認

```powershell
uv run python --version

```

`Python 3.13` と表示されれば基礎環境の構築は完了です。

#### 6. Jupyter の起動

ルートディレクトリから以下を実行します。

```powershell
uv run jupyter lab

```

または、PyCharm 内で直接 `.ipynb` ファイルを開いて実行することも可能です。

#### 7. Notebook を開く

例として、各話の Notebook は以下のように配置されています。

* Vol.2 の場合: `qiita_02_basic/civil_engineering_python_intro_02.ipynb`
* Vol.3 の場合: `qiita_03_pandas/qiita_doboku_3.ipynb`

目的に応じた Notebook を開いて学習を進めてください。

---

## `uv sync` について

本リポジトリでは、プロジェクトルートにて Python 環境および依存関係を一元管理しています。

```text
civil-engineering-python/
├── pyproject.toml
├── uv.lock
└── .python-version

```

そのため、パッケージの同期や初回セットアップ時には常にリポジトリ直下で以下を実行してください。

```powershell
uv sync

```

`uv.lock` ファイルには解決済みの具体的なパッケージバージョンが記録されており、どの端末からでも全く同じ環境を正確に再現することができます。

---

## 依存パッケージ

現在プロジェクトで使用している主なパッケージは以下の通りです。

| パッケージ名 | 用途・機能 |
| --- | --- |
| NumPy | 高速な数値計算・多次元配列処理 |
| pandas | 表形式データの処理・解析・操作 |
| Matplotlib | データのグラフ化・可視化 |
| SciPy | 科学技術計算（補間・積分・微分・最適化など） |
| Jupyter | 対話型 Notebook 実行環境 |
| ipykernel | Jupyter 用の Python カーネル |

依存関係の定義はすべてルートの `pyproject.toml` で管理されています。

---

## 環境の再現性と依存関係管理

教材コードの共有や数値計算において、実行環境の再現性を確保することは非常に重要です。

本リポジトリでは、以下のファイルを用いて正確な Python 環境を保持しています。

| ファイル名 | 役割 |
| --- | --- |
| `pyproject.toml` | プロジェクト設定および依存パッケージの定義 |
| `uv.lock` | バージョン競合を解決した固定依存関係の記録 |
| `.python-version` | プロジェクトで使用する Python バージョンの指定 |

リポジトリ全体で単一の共通環境を採用することで、開発環境による動作の違いを最小限に抑えています。

環境構築時は以下を実行するだけで完了します。

```powershell
uv sync

```

ロックファイルを適用することで環境依存のエラーを防ぐことができますが、これだけでセキュリティが万全になるわけではありません。定期的にライブラリのアップデートを行い、セキュリティ情報のチェックを行うことを推奨します。

---

## セキュリティとコード品質

本リポジトリでは、開発プロセスの一環としてセキュリティ、依存関係管理、環境再現性、およびコード品質の維持に取り組んでいます。

### GitHub セキュリティ機能

安全で健全な開発環境を保つため、以下の GitHub セキュリティ機能を有効化しています。

* **Security Policy** — 脆弱性を安全に報告するためのガイドラインの提供
* **Security Advisories** — セキュリティ勧告の管理および開示メカニズム
* **Private Vulnerability Reporting** — 脆弱性の非公開報告ルートの確立
* **Dependabot Alerts** — 依存パッケージにおける既知の脆弱性の監視
* **Secret Scanning** — 誤ってコミットされた機密情報（APIキー等）の検知

[セキュリティポリシーを見る](https://github.com/skyblueao77/civil-engineering-python/security/policy)

[セキュリティアドバイザリを見る](https://github.com/skyblueao77/civil-engineering-python/security/advisories)

[Dependabot アラートを見る](https://github.com/skyblueao77/civil-engineering-python/security/dependabot)

[シークレットスキャン状況を見る](https://github.com/skyblueao77/civil-engineering-python/security/secret-scanning)

### コードスキャン (Code Scanning)

GitHub Code Scanning による自動静的解析は導入を計画中であり、今後準備が整い次第設定予定です。

### 依存関係の管理

プロジェクトの依存関係は以下で一元管理されています。

```text
pyproject.toml
uv.lock
.python-version

```

`uv.lock` ファイルにより意図しないパッケージ更新による破損を防ぎ、Dependabot によって常に最新の脆弱性情報をチェックしています。

### Pre-commit による自動チェック

コードのコミット前に自動で品質チェックを行うため、`pre-commit` を導入しています。

設定ファイル：

```text
.pre-commit-config.yaml

```

主な開発ワークフロー：

* **Ruff** — 静的解析、コード整形、品質チェック
* **Pytest** — 自動単体テスト
* **nbmake** — Jupyter Notebook の実行動作テスト

以下のコマンドで手動実行も可能です。

```bash
uv run pre-commit run --all-files

```

これにより、構文エラーや未定義変数、フォーマットの乱れ、Notebook の実行失敗などを事前に防止します。

### セキュリティに関する免責

本リポジトリは教育目的の教材であり、高セキュリティが求められるプロダクションシステムではありません。上記のセキュリティ対策やコードチェックは品質と安全性を高めるための取り組みであり、すべての脆弱性が存在しないことを保証するものではありません。

---

## Python スクリプトの実行

Python スクリプト（`.py`）を実行する場合は、プロジェクトルートから以下のようにコマンドを実行します。

```powershell
uv run python qiita_03_pandas/qiita_doboku_3.py

```

`uv run` を経由することで、プロジェクトに紐づく正確な仮想環境下でスクリプトが実行されます。

---

## Jupyter Notebook について

本教材のコードは、主に Jupyter Notebook（`.ipynb`）形式で提供されています。

Notebook を使うと、以下のサイクルで学習をインタラクティブに進めることができます。

```text
コードを書く
    ↓
実行する
    ↓
結果を確認する
    ↓
コードを少し修正してみる
    ↓
再度実行する
    ↓
（理解が深まる！）

```

プログラムを動かしながら試行錯誤したい初心者に最適な学習フォーマットです。

---

## 土木工学における Python の活用

土木工学では、日常的に多様かつ膨大なデータを扱います。

例：

* 降水・気象データ
* 河川の水位・流量データ
* 交通量・人流データ
* 点群・地形・標高データ
* 測量データ
* 地盤・土質試験データ
* 構造物のモニタリング・センサーデータ
* 各種水理・構造実験データ

Python を活用することで、以下の一連の流れを効率化・自動化することができます。

```text
データの読み込み
    ↓
データの整理・前処理
    ↓
統計計算・各種物理シミュレーション
    ↓
グラフや地図への可視化
    ↓
解析結果の考察・評価

```

本プロジェクトでは単に Python の文法を覚えるだけでなく、**「土木の実務や研究でどう活かせるか」** を常に考慮した構成にしています。

---

## AI 時代における Python 学習の意義

現在、生成 AI を使えば誰でも簡単に Python コードを生成できるようになりました。

そうした中で、

> 「自分自身で Python コードの書き方を学ぶ必要はあるのか？」

という疑問が湧くかもしれません。

本プロジェクトは AI によるコード生成を否定しません。むしろ、**「AI が生成したコードを正しく理解し、検証し、修正できる能力」** こそが今最も重要であると考えています。

たとえば、AI にコードを書かせた場合でも、人間側で以下の確認・判断が不可欠です。

* 何をどのように計算しているコードなのか？
* インプットデータや条件指定は正しいか？
* 単位系や次元は合っているか？
* エラーが発生した際、何が原因か？
* 計算結果は数値的に妥当か？
* **土木工学的・物理的に意味の通る結果になっているか？**

特に土木工学においては、

**「プログラムがエラーなく動いた」ことと「解析結果が工学的に正しい」ことはまったく別物です。**

Python の基礎知識を身につけることは、AI を安全かつ高度に使いこなすための最強の基盤となります。

---

## 推奨される学習ロードマップ

以下の順番で学習を進めることを推奨します。

```text
Vol.1 環境構築編
    ↓
Vol.2 Python 基礎編
    ↓
Vol.3 pandas 入門編
    ↓
Vol.4 Matplotlib 入門編
    ↓
Vol.5 NumPy 入門編
    ↓
Vol.6 SciPy 入門編
    ↓
【応用】土木実データ解析
    ↓
【応用】GIS・空間情報データ処理
    ↓
【応用】高度な数値シミュレーション・構造・水理計算

```

一回で完璧に理解する必要はありません。Notebook を実際に動かしながら、

**「書く → 試す → 結果を見る → 条件を変えてみる」**

という小さな実験を繰り返しながら進めていきましょう。

---

## 推奨環境

本プロジェクトが想定している動作環境は以下の通りです。

| 項目 | 推奨環境 |
| --- | --- |
| OS | Windows / macOS / Linux |
| Python | 3.13 |
| IDE（統合開発環境） | PyCharm |
| パッケージ・環境管理 | uv |
| Notebook 環境 | Jupyter Notebook / JupyterLab |
| ブラウザ実行環境 | Google Colab |
| バージョン管理 | Git / GitHub |

※Python およびライブラリのバージョンは、リポジトリ内の `pyproject.toml` および `uv.lock` に従って管理されます。

---

## トラブルシューティング

### `uv` コマンドが認識されない場合

以下を実行して動作を確認してください。

```powershell
uv --version

```

エラーが出る場合は、`uv` のインストールが正しく完了しているか確認してください。

[uv 公式ドキュメント](https://docs.astral.sh/uv/)

---

### Python のバージョンが想定と異なる場合

バージョンを確認します。

```powershell
uv run python --version

```

本リポジトリでは、ルート直下の `.python-version` ファイルにて Python バージョンを指定しています。

---

### パッケージが見つからない（ImportError 等）場合

まず、プロジェクトのルートディレクトリで以下を実行して環境を同期してください。

```powershell
uv sync

```

その後、PyCharm や Jupyter がプロジェクト内の仮想環境（`.venv`）を参照しているか確認してください。

---

### Notebook でプロジェクト環境の Python が選択できない場合

PyCharm や Jupyter 内でカーネルの設定を確認してください。

必要に応じて、ルートディレクトリで以下を実行して Jupyter にカーネルを登録します。

```powershell
uv run python -m ipykernel install --user --name civil-engineering-python --display-name "Python (civil-engineering-python)"

```

---

## 開発者向け情報

本リポジトリでは環境管理に `uv` を、コミット前の自動品質チェックに `pre-commit` を採用しています。

### 1. 開発環境のセットアップ

リポジトリをクローンした後、以下を実行して依存関係を同期し、Git Hooks を有効化します。

```bash
# 依存関係の同期
uv sync

# Git Hooks の有効化
uv run pre-commit install

```

---

### 2. コード品質の検証とテスト

`git commit` 実行時、ローカル環境で設定済みのチェックが自動実行されます。

組み込まれているワークフロー：

* **Ruff**: 静的コード解析、コードフォーマット、構文エラー・未定義変数の検出
* **Pytest (+ nbmake)**: Python スクリプトおよび Jupyter Notebook（`.ipynb`）の実行・動作テスト

#### コミット前の手動テスト実行

コミット前に手動で全体の品質チェックを行う場合は以下を実行します。

```bash
# 全ファイルに対して pre-commit チェックを実行
uv run pre-commit run --all-files

# Notebook の実行テストを含めて Pytest を実行
uv run pytest --nbmake

# Ruff による自動修正付きコードチェック
uv run ruff check --fix

```

---

## 免責事項

本リポジトリは、Python および土木工学分野におけるプログラミング手法を学ぶための**教育・学習用コンテンツ**です。

掲載されているコードおよび解説の正確性、完全性、信頼性について保証するものではありません。

特に、実際の土木構造物の設計、施工、防災、安全評価などの実務判断にコードを利用する場合は、必ず有資格者・専門家の指示のもと、公式の基準書・計算書・関連法規等に照らし合わせて検証を行ってください。本リポジトリのプログラムを利用したことによって生じた一切の損害について、著者は責任を負いかねます。

---

## ライセンス

本リポジトリは **[MIT License](https://www.google.com/search?q=/LICENSE)** のもとで公開されています。商用・非商用を問わず自由にご利用いただけます。

---

## 著者

**skyblueao77**

土木工学を専攻する学生。Python、データ分析、AI 技術などを勉強中。

Qiita にて「土木のための Python 入門」シリーズを連載中。

* [Qiita プロフィール](https://qiita.com/skyblueao77)
* [GitHub プロフィール](https://www.google.com/search?q=https://github.com/skyblueao77)

---

## 関連リンク

* [Qiita - 土木のための Python 入門](https://qiita.com/skyblueao77)
* [GitHub - civil-engineering-python](https://github.com/skyblueao77/civil-engineering-python)
* [uv 公式ドキュメント](https://docs.astral.sh/uv/)
* [PyCharm 公式サイト](https://www.jetbrains.com/pycharm/)
* [Google Colab](https://colab.research.google.com/)

---

## 今後の更新予定

今後、以下のテーマについて順次コンテンツを追加・更新していく予定です。

* 実用的な土木データの解析・可視化実践
* NumPy / SciPy を用いた数値解析応用（水理計算・構造計算等）
* 国土交通省などのオープンデータ（i-Construction、プレート、観測データ等）の活用
* GeoPandas や GIS データを活用した空間情報処理
* AI（生成AI）を活用した Python 開発手法とコード検証技術
* 土木工学における高度な数値シミュレーション

最終的には、**「Python の文法基礎から、実際の土木データ・数値計算を自在に扱えるレベルまで到達できる実践的な学習リポジトリ」** を目指して開発を続けていきます。

```

```