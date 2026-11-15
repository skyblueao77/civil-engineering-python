# Security Policy

## Supported Versions / サポート対象バージョン

本リポジトリで提供しているコード・チュートリアルについて、最新のコード（`main` ブランチ）のみセキュリティアップデートや補正対応を行います。
For the code and tutorials provided in this repository, security updates and fixes are applied only to the latest code (`main` branch).

| Version / バージョン | Supported / サポート状況 |
| -------------------- | ------------------------ |
| `main` (Latest)      | :white_check_mark:       |

## Security Measures / 実施しているセキュリティ対策

学習者・利用者が安心してコードを実行できるよう、以下の対策を継続的に運用しています。
To help learners and users run this repository safely, the following security controls are maintained:

1. **Dependency Locking & Integrity (`uv.lock`)**: 依存パッケージのバージョンとハッシュを `uv.lock` で固定し、意図しないパッケージの混入や環境差異を防ぎます（`uv sync --locked` で検証可能）。
   Dependencies and hashes are locked in `uv.lock` (`uv sync --locked` enforces strict lockfile verification).
2. **Automated Vulnerability Auditing (`Dependabot` + `pip-audit`)**: GitHub Dependabot による週次の依存関係更新（`uv` および `github-actions`）とセキュリティアラートに加え、CI で `pip-audit --strict` を定期実行して既知の脆弱性（CVE）を監視しています。
   Dependabot monitors dependencies (`uv` and `github-actions`) weekly, and CI runs `pip-audit --strict` to check for known vulnerabilities.
3. **Static Security Analysis (`CodeQL` + `Ruff S`)**: GitHub CodeQL および Ruff の Bandit セキュリティルール（`S`）により、安全でない関数呼び出しや問題のある実装パターンを自動検査しています。
   GitHub CodeQL and Ruff Bandit security rules (`S`) scan scripts and notebooks for unsafe coding patterns.
4. **Secret Scanning & Push Protection**: GitHub Secret Scanning / Push Protection および `.gitignore` により、APIキー・秘密鍵・`.env` 等の誤コミットを防止しています。
   GitHub Secret Scanning, Push Protection, and `.gitignore` rules help prevent accidental commits of credentials or `.env` files.
5. **Least-Privilege CI & Notebook Execution Tests**: GitHub Actions ワークフロー（`.github/workflows/ci.yml`）は最小権限（`contents: read`）・Action のコミット SHA 固定で運用し、全 Jupyter Notebook を `pytest --nbmake` で自動検証しています。
   GitHub Actions workflows run with read-only permissions (`contents: read`), SHA-pinned actions, and automated `pytest --nbmake` execution tests across all notebooks.
6. **Minimal Surface Area**: 本リポジトリの教材コードはローカルの数値計算・データ可視化・構造解析を中心に設計されており、認証情報の取得や外部サーバーへの送信処理を含みません。
   Educational scripts and notebooks focus on local numerical computation and visualization without collecting credentials or transmitting user data.

## Reporting a Vulnerability / 脆弱性の報告方法

本リポジトリのコードや依存ライブラリにおいてセキュリティ上の問題（脆弱性や機密情報の誤記述など）を発見された場合は、公開の Issue を作成せず、以下の手順でご連絡をお願いいたします。
If you discover a security issue (such as a vulnerability or accidental exposure of sensitive information) in the code or dependent libraries of this repository, please do not create a public issue and contact us through the following procedure.

1. **GitHub Private Vulnerability Reporting:** リポジトリの [Security] タブからプライベートに報告を作成してください。
   Please create a private report via the [Security] tab of the repository.
2. **Notes / 注意事項:** 連絡の際は、再現手順や影響範囲などの記載にご協力をお願いいたします。原則として数日以内に確認・対応いたします。
   When contacting us, please help by providing steps to reproduce and the scope of impact. As a rule, we will review and respond within a few days.
