Title: Code for Harima 2025.02（第80回定例会）
Date: 2025-02-04 19:00:00
Category: minutes
Tags: 2025
Summary:
lang: ja
Slug: 202502
Save_as: history/202502.html
Template: page

# Code for Harima 2025.02（第80回定例会）

- 日時: 2025/02/04（火）19:00-21:00
- 場所: [加古川びぃぷらす](https://bb-beplus.net/) / [オンライン](https://meet.jit.si/moderated/2e1dddcb737659dfaf7e569c158bbd3aa7acf95eedec00441b0e87ac4db731e1)
- 議事録(HackMD): <https://hackmd.io/@codeforharima/BJw2OHNOyx/edit>
- 司会： 野方
- 参加者: 水野、石本、福田
- リモート: 野方、まなみ、ろみひ〜
- 次回開催: 2025年03月11日（火）19:00 - 21:00
- 開催場所: びぃぷらす
- Webサイト
  - Instagram: <https://instagram.com/codeforharima>
  - Facebookページ: <https://facebook.com/codeforharima>
  - Facebookグループ: <https://www.facebook.com/groups/codeforharima>
  - LINEアカウント: <https://liff.line.me/1645278921-kWRPP32q/?accountId=946ardlp>
  - Webサイト(過去の議事録含む): <https://codeforharima.notion.site/Code-for-Harima-893bae4719f0496d998298ed91ce694a>

## 運営連絡

- 8月から定例会は第2火曜日になってます
- 播磨の情報なら参加者グループにどんどん投稿してくださいね！
  - <https://www.facebook.com/groups/codeforharima/>

## オープンソースカンファレンス2025 Osaka（福田）

- 日時：1月25日(土) 10:00-18:00（展示は16:00まで）
- 場所：大阪産業創造館 \[受付は3F\]
  - <https://www.sansokan.jp/map/> (堺筋本町駅から徒歩5分)
- ＨＰ：OSC2025 Osaka公式サイト
  - <https://event.ospn.jp/osc2025-osaka/>
- セミナータイムテーブル
  - <https://register.ospn.jp/osc2025-osaka/modules/eventrsv/1.html>
- 展示ブース（出展者と展示内容リスト）
  - <https://event.ospn.jp/osc2025-osaka/exhibit>
  - OpenStreetMap Japanブースに１日います。
    - 坂ノ下さんは、WikidateとOpenStreetMapを絡めてお話していた。
    <https://event.ospn.jp/osc2025-osaka/session/1963430>
- **Wikidate**ってなに？
  - ウィキメディアプロジェクトが決めた同じものを指し示すための一意のID番号
    - びぃぷらすの韓国語のページと日本語のページができた場合、言語の違いはあるけれど、両方とも説明される対象が同じなので、同一であることを示す番号がふられる
- たとえば加古川市（日本語ページ）があります
  - <https://ja.wikipedia.org/wiki/%E5%8A%A0%E5%8F%A4%E5%B7%9D%E5%B8%82>
  - 加古川市には`Q750569`というWikidataの番号が振ってあります
    - <https://www.wikidata.org/wiki/Q750569>
  - 加古川市は`Q750569`という番号が振ってあるので、OpenStreetMapにもこの番号で紐づけてあげれば、同じデータを引っ張ってくることができます。そのための番号を振るプロジェクトがWikidataです。
- OpenStreetMapにWikidataのタグがあるので、ここにWikidataの番号を入力しておけば紐づけできます。
  - JA:Wikidata - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Wikidata>

## オープンデータデイで権現総合公園をマッピングする？

- 権現総合公園がオープン！
  - <https://www.city.kakogawa.lg.jp/material/files/group/1/kiji20250121gongensogokoengaopun.pdf>
- オープンは3月30日（日）
- オープンデータ化はなんとなく理解してもらえるものの、公園への立ち入りには「いいよ」と言ってもらえない状況。
  - 遊具の設置は完了
  - 外構施工中
  - マル秘写真は入手済み。
  - ドローンで上空から、複合遊具は正面から。
  - パース
    <https://www.instagram.com/hanshinengei_official/p/CsLLHC8POt6/?img_index=1>
  - 市長の定例会見後に、公開できるかも。
- オープンデータデーのイベントについて
  - 下見をするので、近づけそうなところで取材し、カフェなどに移動してマッピングする？
    - それでいいと思います（の）
      - 見える部分だけ書いて、すぐに追加できるようにするだけでもアリだと思います
        - 全然、音が聞こえないので書くだけ書きました↑
    - 近くまで行くということにしても日程どうするかですね
  - 日岡山公園もニュースポーツゾーン
- 2025年3月30日（日）現地マッピング
  - 当日、10時　加古川駅集合
  - 高校生も参加の方向！
- 日岡山もGWにやる？

## 野口観光マップ作成の件（福田）

- 木谷議員が野口町の観光マップ作成企画中
  - Wikipediaに野口町があった
    - <https://ja.wikipedia.org/wiki/%E9%87%8E%E5%8F%A3%E7%94%BA_(%E5%8A%A0%E5%8F%A4%E5%B7%9D%E5%B8%82)>
  - 水野から木谷さんに、Openstreetmapとコラボしましょう、声かけてよ〜と連絡しました（なう）
  - 返事:来週打ち合わせするので、観光マップを作るかどうか、聞いてみる。観光協会といっても、新住民が多いので、良さを知ってもらおうというところから始めます。１回目は、桜の名所を巡るスタンプラリーをして、オークラさんで軽食を食べてもらう。４月５日の予定だけど、開花状態により１週間前倒しにするかも。都合が付けば遊びに来てほしいです。

## ロミヒーさん

2/16に不登校支援団体の交流会学校の空き教室に事業所さんがコミュニティースクールのいっかんで入ってた事例があったので加古川のどこかの空き教室入らせてって最近お願いしにいきました

- 公立中学校の空き教室に地元企業がオフィスを構える。山形県朝日町の「スキマクラス2.5組」
  - <https://drive.media/posts/65701>

## 探求のテーマ（まなみ）

- テーマは「観光」
- アドバイザーからは、対象をできるだけ小さくするいいと言われていて、おじいちゃんおばあちゃんにしぼるとか、稲美町全体は大きすぎるのではと言われた。
  - 遊具のある公園マップ
    - <https://armd-02.github.io/Playgrounds/?node/11390856787&category=-#19/34.7651439/134.8622103>
