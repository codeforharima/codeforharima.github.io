Title: Code for Harimaの議事録をNotionで見られるようにしたメモ
Date: 2023-05-10 19:00:00
Category: events
Tags: memo
Summary:
lang: ja
Slug: how-to-migrate-notion
Save_as: events/how-to-migrate-notion.html
Template: page

# Code for Harimaの議事録をNotionで見られるようにしたメモ

## NotionでCode for Harimaの議事録をWebで見られるようにしました（野方）

定例会でみんなで[HackMD](https://hackmd.io/)に書いていた5年間の議事録を[Notion](https://www.notion.so/ja-jp/product)というメモを蓄積するWebサービスに取り込んで、Webページとして見られるようにしました

HackMDは、[Markdownという書式](https://ja.wikipedia.org/wiki/Markdown)を使ってテキストを書くサービスなので、作業としてはHackMDから過去のMarkdown形式テキストファイルをダウンロードしてNotionにインポートすればOK!のはずでした…

### 苦労1: Notionの仕組みがわからない

Markdownテキストファイルを取り込めばNotionのメモになる、というのは分かります。でも、それを集約する[Notionのデータベース](https://www.notion.so/ja-jp/help/category/databases)の概念が独特すぎて、とっつきづらかったです。

データベースという言葉に惑わされましたが、簡単に言えばページのリンク集作ってメタデータでタグ付けするだけなので、それがわかればページの整理ができました。

ほかにはページのレイアウト、見た目の配置もですがドキュメントの階層のレイアウトもわからんとか、わからんすぎてめちゃくちゃ時間がかかりました。

### 苦労2: Markdownの書式が正しくないこととHackMDのバグ

インポートした後、ページの見た目が崩れているものが目に付いたので元のMarkdownのファイルを確認するとMarkdownの書式が間違っているものが結構ありました。

書式の間違いは、リアルタイムに書いていることや書いた後にチェックをしなかったので仕方ありませんが基本的には[Markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)というチェックツールで機械的に修正しました。

が、Markdownの半角スペースで書く部分を全角スペースで書いてる部分は機械的に修正できない（文章のスペースと書式のスペースが判別できない）のでその部分は手で修正しました。

ほかにファイルを見ているとHackMDのバグで、同じ内容が繰り返して出力されているファイルも発見したこともあって最終的には、5年分全部を[VS Code](https://code.visualstudio.com/)（テキストエディター）で開いて目視でチェックしました。ぴえん。

### HackMDはNotionに置き換えられるのか（置き換えるものではない）

結論から書くと、置き換えるものではありません。NotionとHackMDは役割が違うので、今までどおりHackMDは使います。NotionとHackMDの良い点と悪い点をまとめるとこうなります。

- HackMDの良い点、悪い点
  - ○: 1つのドキュメントをみんな一斉にリアルタイムで書ける
  - ×: 貯めたドキュメントを整理するのは不得意
- Notionの良い点、悪い点
  - ○: ドキュメントを貯めて整理できる
  - ×: リアルタイムでドキュメントを書くのは不得意。無料プランは人数制限もある

と、見事な補完関係になっているので、議事録はHackMDでみんなで書いて、終わったらNotionに移す（HackMDのテキストをCtrl+Aで全選択してコピー、Notionに貼り付けできる）のが良いと思います。
