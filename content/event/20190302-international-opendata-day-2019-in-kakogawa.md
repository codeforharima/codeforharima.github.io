---
Title: インターナショナル・オープンデータ・デイ 2019 in 加古川
Date: 2019-03-02 11:00:00
Category: event
Tags: openstreetmap
Summary:
lang: ja
Slug: international-opendata-day-2019
---

- 日時: 2019/03/02 11:00-17:00 (予定)
- 場所: 加古川 00. Workspace
- 参加者:

## OpenStreetMapマッピングパーティの事前準備

- OpenStreetMapのアカウント(必須!!)
- 編集用のパソコンとマウス(JOSMをインストールしておいてください)
- 筆記用具とクリップボード(メモを取ります)
- デジカメかスマホ(メモを取りづらいものを写真で記録)
    - Androidの人は[OSM Tracker](https://play.google.com/store/apps/details?id=net.osmtracker&hl=ja_JP)というアプリを入れておくとGPSログと写真などが一度に記録取れて便利
- 歩きやすい格好の服装(寺家町商店街を1時間ほど歩きます)
- <https://medium.com/openstreetmap-tips-japan/osm-%E3%83%9E%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%81%AE%E6%BA%96%E5%82%99-b417654cf469>
- Field papers(メモ用の地図): <http://fieldpapers.org/atlases/4cqj9x1b>
- OpenStreetMapで入力された物を見る地図: <https://www.openstreetbrowser.org/>

## 予定

- 11:00: 00に集合。今日の説明
- 11:30: 一時間ぐらい寺家町商店街を歩いて、地図を書くポイントなどを説明
    - 加古川本町商店街のほぼ中央に位置する「神田家住宅洋館」を取材してまいりました♪♪ | 地元民が語る加古川ネタ知っとう？ | まいぷれ加古川市: <https://kakogawa.mypl.net/mp/jimoneta_kakogawa/?sid=64098>
    - <http://umap.openstreetmap.fr/ja/map/20190302_odd_kakogawa_298155>
- 13:00ぐらい: 00に戻ってきてOSMの地図を書く
- 16:30ぐらい: 成果発表

## 地図を書く時のワンポイント

- 下絵の航空写真は、bingはズレているので「国土地理院 電子国土基本図(オルソ画像)」か「国土地理院 全国最新写真」を使う
    - bingのほうが新しいので「位置は地理院、建物はbing」と切り替えながら確認するといいかも
- 高い建物は、屋上で形を書いて足元に移動
    - 斜めに写っている建物の実態は足元なので、形を書いたら足元に移動させましょう
- 道路は幅ではなく「役割」で選ぶ
    - めっちゃ広いスーパー農道でも種類は「農道」だし、酷道と呼ばれる細い国道でも種類は「国道」
        - 日本の道路区分は管理主体で分けられているので、OSMの区分とは合ってないのです
        - 幅や通行制限は、widthやaccessタグを追加して表現
    - 道路の種類に迷ったら「一般道(2車線未満)」(unclassified)を選ぶ
        - 「住宅地区の道路」(residential)という区分は日本には無いです
            - 地域住人しか通らなくて車が入れるところなら、つけてもいいかも
    - 裏路地(住んでいる人しか通らず、人が歩くだけの道)は、highway=service,
    service=alley
- タグ付けでわからない時はOpenStreetMap Wikiで検索
    - <https://wiki.openstreetmap.org/wiki/JA:Main_Page>
- Map Features(日本の全タグが載ってるけど、めちゃ重い): <https://wiki.openstreetmap.org/wiki/JA:Map_Features>
- 五十音順POI(地物)タグ一覧: <https://wiki.openstreetmap.org/wiki/JA:How_to_map_a>
- チェーン店の名前サンプル: <https://wiki.openstreetmap.org/wiki/JA:Naming_sample>

## マッピングパーティ成果予定地

3/2の11時以降に編集した部分が表示されるはず。

- <http://u.osmfr.org/m/297641/>
