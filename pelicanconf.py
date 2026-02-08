SITENAME = "Code for Harima"
SITEURL = "http://127.0.0.1:8000"
AUTHOR = ""
SITESUBTITLE = "兵庫県播磨地域で地域課題をシビックテックで解決を図るボランティア団体"

PATH = "content"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y/%m/%d"
THEME = "themes/codeforharima"

# フィード設定
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ページネーション
DEFAULT_PAGINATION = 6

# --- URL設計 ---
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

# カテゴリごとのURL設定
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"

# 固定ページのURL
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# タグ・著者ページ（必要に応じて無効化）
TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_SAVE_AS = "tags/index.html"

# 著者ページを生成しない
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# --- 記事一覧を/blog/に出す（サイト直下のindexを奪わない） ---
INDEX_SAVE_AS = "blog/index.html"

# 直下の index は pages/index.md に任せるので、ここは生成だけ/blogへ逃がす
DIRECT_TEMPLATES = ["index", "archives", "tags", "categories"]

# カスタムページ設定
TEMPLATE_PAGES = {
    "home.html": "index.html",  # トップページ用カスタムテンプレート
}

# 静的ファイル
STATIC_PATHS = ["images", "extra"]

# メニュー設定
MENUITEMS = [
    ("ホーム", "/"),
    ("私たちについて", "/about/"),
    ("活動記録", "/history/"),
    ("イベント記録", "/events/"),
    ("ブログ", "/blog/"),
]

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


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelicanconf.py or publishconf.py
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer
