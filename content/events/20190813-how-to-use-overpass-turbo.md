---
Title: Overpass Turboの使い方
Date: 2019-08-13 19:00:00
Category: events
Tags: memo, openstreetmap
Summary:
lang: ja
Slug: how-to-use-overpass-turbo
Save_as: history/how-to-use-overpass-turbo.html
Template: page
---

## OpenStreetMapは地理データベース

OpenStreetMapは地図として表示されますが、実は巨大な地理データベースです。Overpass Turbo(<https://overpass-turbo.eu/>)というサイトからデータベースとしてOpenStreetMapを検索できます。

コンビニエンスストアを検索してみましょう。

1. <https://overpass-turbo.eu/> にアクセスする。
1. 表示されている地図を実行したい場所まで移動する。（地図は検索範囲になるので、なるべく拡大しましょう。）
1. \[ウィザード\]ボタンを押す。
1. `shop=convenience` と半角で入力する。 (`shop=convenience` は、OpenStreetMapで決められているコンビニを表すタグです。)
1. \[クエリを作成して実行\]ボタンを押す。

地図上にコンビニエンスストアが登録されている場所があれば検索結果が表示されます。地図上の検索結果をクリックすると詳細データが表示されます。また、ブラウザ画面右上の\[データ\]ボタンを押すと検索結果のデータが表示されます。

### 補足解説

OpenStreetMapの検索は、SQLで検索ではなくjsonで書かれたOverpassQLという独自問い合わせ言語で検索しています。ブラウザ画面左側の表示は、そのOverpassQLが表示されています。

`shop=convenience`は、OpenStreetMapの入力に使うタグで、key/valueの形になっています。なので想像できると思いますが、`convenience`の部分を`supermarket`に変えるとスーパーマーケットが検索できます。ほかのタグ一覧については下のリンクを参照してください。

- タグ一覧: <https://wiki.openstreetmap.org/wiki/JA:Map_Features>

Overpass Turbo自体の解説は、こちらにあります。

- OverPassTurboの解説: <https://wiki.openstreetmap.org/wiki/JA:Overpass_turbo>
