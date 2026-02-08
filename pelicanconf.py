SITENAME = "Code for Harima"
SITEURL = "http://127.0.0.1:8000"
AUTHOR = ""
SITESUBTITLE = "兵庫県播磨地域で地域課題をシビックテックで解決を図るボランティア団体"

# --- 基本 ---
PATH = "content"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y/%m/%d"
THEME = "themes/codeforharima"

# --- コンテンツの役割分離（CMS化の肝） ---
PAGE_PATHS = ["pages"]  # 固定ページ群（サイト本体）
ARTICLE_PATHS = ["blog"]  # 記事は/blog専用

# --- URL設計：ページはそのまま階層、記事は/blog配下 ---
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

# --- 記事一覧を/blog/に出す（サイト直下のindexを奪わない） ---
INDEX_SAVE_AS = "blog/index.html"

# 記事関連のアーカイブ類も/blog配下へ（好みでON/OFF）
ARCHIVES_SAVE_AS = "blog/archives/index.html"
TAGS_SAVE_AS = "blog/tags/index.html"
TAG_SAVE_AS = "blog/tag/{slug}/index.html"
CATEGORIES_SAVE_AS = "blog/categories/index.html"
CATEGORY_SAVE_AS = "blog/category/{slug}/index.html"

# 著者ページを生成しない
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# 直下の index は pages/index.md に任せるので、ここは生成だけ/blogへ逃がす
DIRECT_TEMPLATES = ["index", "archives", "tags", "categories"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Code for Japan", "https://www.code4japan.org/"),)

# Social widget
SOCIAL = (
    ("Facebookページ", "https://facebook.com/codeforharima"),
    ("Facebookグループ", "https://www.facebook.com/groups/codeforharima"),
    ("Instagram", "https://instagram.com/codeforharima"),
    ("LINE", "https://liff.line.me/1645278921-kWRPP32q/?accountId=946ardlp"),
    ("GitHub", "https://github.com/codeforharima"),
    ("HackMD", "https://hackmd.io/@codeforharima"),
)

# カルーセルキャッチコピーと画像
CAROUSEL = (
    ("地域課題に挑む", "シビックテックで未来を変える", "shapelined.webp"),
    ("つながる地域", "テクノロジーで地域を元気に", "shapelined.webp"),
    ("未来を創る", "あなたの参加で地域が変わる", "shapelined.webp"),
)

# 活動内容
MAIN_ACTIVITY = (
    ("定例会", "毎月開催する定例会で地域課題について話し合います", "bi-people-fill"),
    ("イベント開催", "地域のイベントに参加してシビックテックの魅力を伝えます", "bi-calendar-check"),
    ("地域コミュニティ支援", "地域のコミュニティを支援し、より良い地域社会の実現を目指します", "bi-geo-alt-fill"),
)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelicanconf.py or publishconf.py
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer
