---
Title: 3D都市モデル（Project PLATEAU）加古川市（2020年度）取り込み
Date: 2022-04-13 19:00:00
Category: events
Tags: openstreetmap, plateau, memo
Summary:
lang: ja
Slug: import-plateau-kakogawa
Save_as: history/2022-import-plateau-kakogawa.html
Template: page
---

# 3D都市モデル（Project PLATEAU）加古川市（2020年度）取り込み

- OpenStreetMapの全体的なインポート方針
    - JA:MLIT PLATEAU/imports outline - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:MLIT_PLATEAU/imports_outline>

全体の作業スケジュールとしては5月下旬から6月にかけてから始まりますが、建物が少ない地域から始めて様子を見ながら広げていくそうなので、加古川は少し遅くなりそうです。

## データ公開場所

- 3D都市モデル（Project PLATEAU）ポータルサイト - データセット: <https://www.geospatial.jp/ckan/dataset/plateau>
- 3D都市モデル（Project PLATEAU）加古川市（2020年度） - データセット: <https://www.geospatial.jp/ckan/dataset/plateau-28210-kakogawa-shi-2020>

## 変換方法

検討用に4月時点での変換ファイルを下に置いています。

- <https://drive.google.com/file/d/1gLo6FkCmIQ5k86Feq-O2qCbXcbkcwe_S/view?usp=sharing>

変換方法は、作業手順に従います。

- 作業手順（ドラフト）
    - Plateau建物データ: OpenStreetMapへのインポート手順（ドラフト） - Qiita: <https://qiita.com/nyampire/items/1c10afdd36750c87154d>

PlateauのCityGMLからOSMデータへの変換にはマシンパワーが必要です。（野方のRyzen5 2400G/32GB/Linuxで5，6時間ぐらい。南部の比較に時間がかかってる?）

## 取込の方法

## 今後の対応

- 2022年5月20日(金)　加古川市多田さんとの意見交換
    - OMSインポートに関してのご意見
    - 加古川市のPLATEAUの活用事例
    - 加古川市のPLATEAUの今後のデータ提供の確認
    - そのほか

## 参考事例

- [『PLATEAU』の都市3Dデータ形式CityGMLをFBXに変換してUnityで遊ぶ](https://tatsuya1970.com/?p=15666)
- [G空間情報センター3D都市モデル（Project PLATEAU）加古川市（2020年度）](https://www.geospatial.jp/ckan/dataset/plateau-28210-kakogawa-shi-2020)
- [国土交通データプラットフォームと公共交通データの連携実証実験を実施し、「GTFSデータリポジトリ」の試験運用を開始](https://prtimes.jp/main/html/rd/p/000000013.000069280.html?fbclid=IwAR1RdjHaUW-Ox9GhSC72vnMJpiYC2D7n-jICfyGfgRF8zxdKl6y3HwKraZk)
- PLATEAUではありませんが富田林市が市のデータをOpenStreetMapにインポートした事例
    - JA:Tondabayashi/Road Building import - OpenStreetMap Wiki: <https://wiki.openstreetmap.org/wiki/JA:Tondabayashi/Road_Building_import>

> 2015年7月19日（提案）　富田林市として市内の各施設の案内サイトについて、27年度に背景地図をOSMに移行し、行政各事務に利用する地図や、市民や事業者から市への申請に利用される地図についてもOSMを推奨する計画を説明する。市が保有する地形図をクリエイティブ・コモンズ（CC-BY2.1JP）のライセンスに則って公開し、OSMに移植する作業は地域関係者が個人として行う。今後、毎年度の地形図差分（CC-BY）を用いて定期的な更新も予定している。

- 実際に使われている地図 <https://www.city.tondabayashi.lg.jp/map2/files/map.html?135.5972&34.4996&17&1000&n000010000>
- 20170721オープンデータ情報交換会: <https://www.slideshare.net/asanokazuhito/20170721-78085553>
