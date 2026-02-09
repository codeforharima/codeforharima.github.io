---
Title: オープンストリートマップ(OpenStreetMap)講座
Date: 2018-09-21 18:00:00
Category: events
Tags: openstreetmap
Summary:
lang: ja
Slug: openstreetmap-workshop
---

- 日時: 2018/09/21 18:00-21:00
- 場所: 加古川 00. Workspace

## OpenStreetMapについての話 / 野方

- <https://gist.github.com/nogajun/76cc316d635cb35433bed584abd462a7>
- 資料などを貼り付ける予定
- 以下、それを受けてのディスカッションとかメモを記録

---

以下、野方のメモから抜き出し。

## OpenStreetMap初心者向けガイド

- OpenStreetMapのアカウント登録とエディター(JOSM)のセットアップ方法
    - 坂ノ下さんが書かれた、[[OSM]マッピングパーティの準備](https://medium.com/openstreetmap-tips-japan/osm-%E3%83%9E%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%81%AE%E6%BA%96%E5%82%99-b417654cf469)より
    - [OSM]アカウント登録方法 – OpenStreetMap Tips(Japan) – Medium: <https://medium.com/openstreetmap-tips-japan/osm-%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E7%99%BB%E9%8C%B2%E6%96%B9%E6%B3%95-fd0dd1383380>
    - [JOSM]Java 10のインストール方法 – OpenStreetMap Tips(Japan) – Medium: <https://medium.com/openstreetmap-tips-japan/josm-java-10%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95-80e95394694>
    - [JOSM]インストール＆設定方法 – OpenStreetMap Tips(Japan) – Medium: <https://medium.com/openstreetmap-tips-japan/josm-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB-%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95-b7d39775bc79>

- Mapbox社作成のOSM参加ガイドブック
    - OpenStreetMapマッピング | Mapbox: <https://www.mapbox.com/mapping/jp/>
    - あれ?これは、どう書くの?といったことなども説明されている

- ごうだまりぽさんの初心者メモ
    - OpenStreetMapに参加して5ヶ月経ったのでメモ – コーヒーサーバは香炉である:
    <https://blog.maripo.org/2017/10/openstreetmap-5m/>

---

## 定礎はどうやってタグ付けする？

OpenStreetMapで定礎をどうやってタグ付けするか考えてみる。

### 定礎とは

- 礎石 - Wikipedia: <https://ja.wikipedia.org/wiki/%E7%A4%8E%E7%9F%B3>
- Cornerstone - Wikipedia: <https://en.wikipedia.org/wiki/Cornerstone>

竣工日を記したプレート。英語では、cornerstoneやfoundation stoneという。「openstreetmap cornerstone」などで検索してもない感じ。

### building= + と?

建物は`building`タグなので、関連するものから考える。

- JA:Key:building - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Key:building>
- 工事終了日に使うタグ
    - JA:Key:opening_date - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Key:opening_date>
- 使用開始日に使うタグ
    - JA:Key:start_date - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Key:start_date>

`opening_date`が竣工日っぽい。

### historic=memorial + ?

- `historic=memorial` 記念碑に使うタグ
    - JA:Tag:historic=memorial - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Tag:historic%3Dmemorial>
        - `name=*` 記念碑の名称
        - `memorial=*` 記念碑の種類（memorial:type=* もときどき使われています。議論ページを参照）
        - `inscription=*` 記念碑にある碑文の文字列
        - `inscription:url=*` Wikisource などといった碑文がわかる外部のウェブサイト
        - `wikidata=*` この記念碑の特有の Wikidata 項目の ID （もしあれば）
        - `commemorates:wikidata=*` 記念碑で記念される人物、団体、出来事についての Wikidata 項目の ID

- `memorial=plaque` 記念碑の種類にプレートがある
    - Tag:memorial=plaque - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/Tag:memorial%3Dplaque>
- `inscription`は対象物の銘文を記述
    - JA:Key:inscription - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Key:inscription>
- `description`は対象物の説明を書く
    - JA:Key:description - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Key:description>

### 考察まとめ

とりあえず、物として書くならノードに以下のタグでいいのだろうか?

- `name=(定礎は固有名詞ではないので無いほうがいいと思う)`
- `historic=memorial`
- `memorial=plaque`
- `inscription="定礎"`
- `description="(定礎の説明を書く)"`

建物の方にはこんな感じ

- `building=(建物の種類)`
- `opening_date=YYYY-MM-DD`
