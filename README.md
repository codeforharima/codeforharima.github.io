# Code for Harima Webサイト

Pythonで作られた静的サイトジェネレーター「[Pelican](https://getpelican.com/)」を使って作られた、Code for Harimaのウェブサイトです。

## ビルド方法

Visual Studio Codeの[開発コンテナ](https://code.visualstudio.com/docs/devcontainers/create-dev-container)を使っているのでビルドをするには、[Docker](https://www.docker.com/)または[Podman](https://podman.io/)と[Visual Studio Code](https://code.visualstudio.com/download)をインストールしてください。
そして、このリポジトリをクローンします。

```terminal
git clone https://github.com/codeforharima/codeforharima.github.io.git
```

クローンしたら、Visual Studio Codeを起動してリポジトリの中にあるワークスペースファイル(`c4h-website.code-workspace`)を開きます。

あとは、必要な拡張機能がインストールされてビルド用の開発コンテナーがビルドされるので開発環境が一式揃います。

開発環境が揃ったなら、リポジトリの中で`pelican content`を実行すればビルドできます。

### もう1つのビルド方法

Pythonと[uv](https://docs.astral.sh/uv/)が用意できるなら、VS Codeと開発コンテナを使わなくてもビルドできます。

このリポジトリをクローンしたら、ディレクトリの中で`uv sync`を実行してください。それだけでビルド環境は整います。

```console
git clone https://github.com/codeforharima/codeforharima.github.io.git
cd codeforharima.github.io/
uv sync
```

こちらの方法も開発環境が準備できれば、リポジトリの中で`pelican content`を実行すればビルドできます。

## LICENSE
