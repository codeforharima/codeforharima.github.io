SITENAME = "Code for Harima"
SITEURL = "https://codeforharima.github.io/"
AUTHOR = ""
SITESUBTITLE = "兵庫県播磨地域で地域課題をシビックテックで解決を図るボランティア団体"

PATH = "content"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y/%m/%d"
THEME = "themes/c4h"

# フィード設定
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ページネーション
DEFAULT_PAGINATION = 6

# --- URL設計 ---
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"

# カテゴリごとのURL設定
CATEGORY_URL = "{slug}/"
# カテゴリーページは無効
CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = "{slug}/index.html"

# 固定ページのURL
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# タグページ無効
TAG_URL = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

# アーカイブページ無効
ARCHIVES_SAVE_AS = ""
YEAR_ARCHIVE_SAVE_AS = ""
MONTH_ARCHIVE_SAVE_AS = ""
DAY_ARCHIVE_SAVE_AS = ""

# 著者ページ無効
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# デフォルトのインデックスページを無効。別途テンプレート指定で作成
INDEX_SAVE_AS = ""

# カスタムページ設定
TEMPLATE_PAGES = {
    "home.html": "index.html",  # トップページ用カスタムテンプレート
}

# メニュー設定
MENUITEMS = [
    ("ホーム", "/"),
    ("私たちについて", "/about/"),
    ("定例会", "/meeting/"),
    ("イベント", "/event/"),
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
    ("地域課題に挑む", "シビックテックで未来を変える", "temp-brianna-marble-unsplash.webp"),
    ("つながる地域", "テクノロジーで地域を元気に", "temp-ilze-lucero-unsplash.webp"),
    ("未来を創る", "あなたの参加で地域が変わる", "temp-roman-serdyuk-unsplash.webp"),
)

# 活動内容
MAIN_ACTIVITY = (
    ("定例会", "毎月開催する定例会で地域課題について話し合います", "bi-people-fill"),
    ("イベント開催", "地域のイベントに参加してシビックテックの魅力を伝えます", "bi-calendar-check"),
    ("地域コミュニティ支援", "地域のコミュニティを支援し、より良い地域社会の実現を目指します", "bi-geo-alt-fill"),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# pelicanconf.py or publishconf.py
# SEO_REPORT = True  # SEO report is enabled by default
# SEO_ENHANCER = True  # SEO enhancer is disabled by default
# SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
# SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer
