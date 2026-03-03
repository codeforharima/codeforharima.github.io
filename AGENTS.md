# Code for Harima Website 仕様メモ

このドキュメントは、`/workspaces/website` の現状実装を元にした開発用仕様です。  
今後の開発はここを基準にし、仕様変更時は本ファイルも更新します。

## 1. プロジェクト概要

- 種別: Pelican製の静的Webサイト
- サイト名: `Code for Harima`
- 目的: 兵庫県播磨地域でシビックテック活動を行うボランティア団体「Code for Harima」の広報
- 主用途:
  - 団体サイト（トップ、紹介、行動規範）
  - 定例会議事録の公開（`meeting`）
  - イベント記録（`event`）
  - ブログ投稿（`blog`）

## 2. 技術スタック

- 言語/実行環境: Python 3.13+
- 静的サイトジェネレータ: Pelican 4.11系
- テーマ: `themes/c4h`
- CSS/JS:
  - Bootstrap 5.3.8
  - Bootstrap Icons 1.11.0
- 検索UI: Stork（`base.html` で `search-index.st` を参照）
- CMS: Decap CMS（`/admin/`）
- 認証/バックエンド連携: Netlify Identity + `git-gateway`（Decapのbackend設定）

## 2.1 Pelicanプラグイン方針

- Pelican 4.5以降の仕様により、インストール済みプラグインは `pelicanconf.py` に `PLUGINS` を明示しなくても自動認識される前提で運用。
- 自動認識の確認コマンド: `uv run pelican-plugins`
- 2026-03-03 時点の認識結果:
  - `pelican.plugins.featured_image`
  - `pelican.plugins.neighbors`
  - `pelican.plugins.read_more`
  - `pelican.plugins.related_posts`
  - `pelican.plugins.search`
  - `pelican.plugins.series`
  - `pelican.plugins.share_post`
  - `pelican.plugins.sitemap`
  - `pelican.plugins.tag_cloud`
  - `pelican.plugins.thumbnailer`

## 2.2 プラグイン利用状況（2026-03-03時点）

- 使用中（本番で機能確認済み）
  - `pelican-search`
    - 役割: Stork用インデックス（`search-index.st`, `search.toml`）生成
    - 備考: CIで `stork` バイナリ導入後にビルドし、本番検索を提供
  - `pelican-sitemap`
    - 役割: `sitemap.xml` 生成
    - 備考: `output/sitemap.xml` の生成を確認済み
- インストール済みだが現状は棚上げ（テンプレート側の活用は未実装/未確認）
  - `pelican-featured-image`
  - `pelican-neighbors`
  - `pelican-read-more`
  - `pelican-related-posts`
  - `pelican-series`
  - `pelican-share-post`
  - `pelican-tag-cloud`
  - `pelican-thumbnailer`
- 補足:
  - 上記棚上げプラグインは、今後サイト基本機能の整備後に段階的に活用する想定。
  - 現在のテーマ実装（`themes/c4h/templates`）では、これらの機能を明示的に利用する表示ロジックは限定的。

## 3. 主要ディレクトリ

- `content/`: コンテンツ本体
  - `content/pages/`: 固定ページ
  - `content/meeting/`: 定例会議事録（カテゴリ `meeting`）
  - `content/event/`: イベント記事（カテゴリ `event`）
  - `content/blog/`: ブログ記事（カテゴリ `blog`）
  - `content/images/`: 画像
  - `content/admin/`: Decap CMS管理画面関連
- `themes/c4h/`: テーマテンプレート/静的アセット
- `pelicanconf.py`: 開発向け設定
- `publishconf.py`: 公開向け設定
- `.github/workflows/pelican.yml`: GitHub Pagesデプロイ

## 4. コンテンツ仕様

## 4.1 フロントマター（Markdown）

- 主に以下メタデータを使用:
  - `Title` / `title`
  - `Date` / `date`
  - `Category` / `category`
  - `Tags` / `tags`
  - `Slug` / `slug`
  - `Summary` / `summary`
  - `Cover` / `cover`
- 既存データは大文字小文字が混在しているが、Pelican側で解釈される前提。

## 4.2 カテゴリと用途

- `meeting`: 定例会議事録
- `event`: 活動イベント・記録
- `blog`: お知らせ等のブログ

## 4.3 固定ページ

- 例:
  - `/about/`（`content/pages/about.md`）
  - `/event/`（`content/pages/event.md`。`template: meeting` + `save_as: meeting/index.html` で活動履歴ページとして利用）
  - `/about/code-of-conduct/`（`slug: about/code-of-conduct`）

## 5. URL/生成仕様（pelicanconf.py）

- 記事URL: `/{category}/{slug}/`
- 記事出力: `/{category}/{slug}/index.html`
- カテゴリURL: `/{slug}/`（例: `/blog/`, `/meeting/`, `/event/`）
- 固定ページURL: `/{slug}/`
- トップページ:
  - 通常index生成は無効（`INDEX_SAVE_AS = ""`）
  - `TEMPLATE_PAGES = {"home.html": "index.html"}` でカスタム生成
- 無効化済み:
  - タグ一覧ページ
  - アーカイブ（年/月/日）
  - 著者一覧ページ

## 6. テンプレート仕様（themes/c4h/templates）

- `base.html`
  - 共通ヘッダー/フッター
  - メニューは `MENUITEMS` を表示
  - SNSリンクは `SOCIAL` を表示
  - Stork検索入力を表示
  - Netlify Identityウィジェット読み込み
- `home.html`（トップ）
  - `CAROUSEL` 設定を3スライド想定で表示
  - 活動紹介（`MAIN_ACTIVITY`）
  - `meeting`カテゴリ記事を先頭3件表示
  - `blog`カテゴリ記事をカード表示
- `meeting.html`
  - `meeting`カテゴリ記事を年別に逆順表示する活動履歴ページ
- `category.html`
  - カテゴリページ一覧表示（ページネーション対応）
- `article.html`, `page.html`
  - 本文表示テンプレート
  - `cover` があれば先頭画像を表示

## 7. サイト設定（pelicanconf.py）

- `DEFAULT_LANG = "ja"`
- `TIMEZONE = "Asia/Tokyo"`
- `DEFAULT_PAGINATION = 6`
- `STATIC_PATHS = ["images", "admin"]`
- `ARTICLE_EXCLUDES = ["admin"]`
- `PAGE_EXCLUDES = ["admin"]`
- メニュー:
  - ホーム `/`
  - 私たちについて `/about/`
  - 定例会 `/meeting/`
  - イベント `/event/`
  - ブログ `/blog/`

## 8. ビルド/開発運用

- 依存導入（推奨）: `uv sync`
- ローカルビルド: `pelican content` または `make html`
- ローカル確認: `make serve` / `make devserver`
- `tasks.py` でも `invoke build`, `invoke serve`, `invoke livereload` などが利用可能
- 開発コンテナ:
  - 設定ファイル: `.devcontainer/devcontainer.json`
  - ベースイメージ: `mcr.microsoft.com/devcontainers/base:trixie`
  - 主なFeatures: Python, uv, Node.js
  - `postCreateCommand` で `stork` バイナリを導入し、`uv sync` を実行

## 9. デプロイ

- GitHub Actions:
  - `main` ブランチへの push で `.github/workflows/pelican.yml` が実行
  - カスタムワークフローで GitHub Pages 配信（build job + deploy job）
  - 設定ファイルは `publishconf.py`、依存導入は `uv sync --frozen` を使用
  - buildジョブで `stork` バイナリを導入してから `uv run pelican content -o output -s publishconf.py` を実行
- 公開先: `https://codeforharima.github.io/`

## 10. CMS（Decap）

- `content/admin/config.yml` で設定
- 現状のコレクションは `blog` のみ
  - 保存先: `content/blog`
  - 生成時のデフォルトカテゴリ: `blog`
- 管理画面は `content/admin/index.html` で Decap CMS (`decap-cms.js`) を読み込む
- backend設定:
  - `name: git-gateway`
  - `repo: codeforharima/codeforharima.github.io`
  - `branch: main`

## 11. 開発時の実装注意点

- トップの「新着記事」表示は `blog` カテゴリのみを対象。
- `home.html` ではタグ表示に `article.tags[0]` を使うため、ブログ記事には `tags` 設定を入れる前提で運用する。
- ページ/記事で `cover` 未設定時のフォールバック画像はテンプレート側で処理される。
- 既存のURL設計（`/{category}/{slug}/`, `/{slug}/`）は外部リンク影響が大きいため、変更時はリダイレクト方針を同時に決める。

## 12. 現在の課題（2026-03-03時点）

- 検索（pelican-search + Stork）:
  - 実装済み。CIで `stork` 導入 + `uv` ベースのビルドにより `search-index.st` を生成し、本番で検索動作を確認済み。
- Decap CMS認証:
  - Decap CMS導入は済んでいるが、認証フロー（Netlify Identity / Git Gateway）が未解決で、運用開始できていない。
