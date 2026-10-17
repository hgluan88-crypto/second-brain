#!/usr/bin/env python3
"""Công cụ dòng lệnh gọi Sapo Admin API của vuabaoho.com.

Xác thực: proxy của môi trường Claude tự gắn mã API Sapo (Network secret
"Sapo VBH", kiểu Basic, cho host vuabaoho.mysapo.net), nên script không cần
và không được chứa mã. Nếu chạy ở nơi khác, đặt SAPO_API_KEY và SAPO_API_SECRET.

Ví dụ:
  python3 seo/scripts/sapo.py articles --out /tmp/articles.json
  python3 seo/scripts/sapo.py search-articles "giày bảo hộ" "jogger"
  python3 seo/scripts/sapo.py products --q "áo sưởi"
  python3 seo/scripts/sapo.py kho-images --q "xanh cobalt"
  python3 seo/scripts/sapo.py prep-image in.png out.jpg
  python3 seo/scripts/sapo.py kho-upload out.jpg --alt "Mô tả ảnh"
  python3 seo/scripts/sapo.py create-article bai.json
  python3 seo/scripts/sapo.py publish 4115540
  python3 seo/scripts/sapo.py check-live dat-may-quan-ao-bao-ho-lao-dong-cho-doanh-nghiep
"""
import argparse
import base64
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

STORE = os.environ.get("SAPO_STORE", "vuabaoho.mysapo.net")
SITE = os.environ.get("SAPO_SITE", "https://vuabaoho.com")
BLOG_ID = int(os.environ.get("SAPO_BLOG_ID", "562093"))  # blog "Thông tin tiêu dùng" (/tin-tuc)
KHO_ANH_ID = int(os.environ.get("SAPO_KHO_ANH_ID", "94248792"))  # sản phẩm ẩn "KHO ẢNH BÀI VIẾT"
AUTO_TAG = "seo-tu-dong"  # gắn cho mọi bài do lịch tự động đăng
PHASE1_LIMIT = 14  # 14 bài tự động đầu tiên phải để ẩn chờ anh Luận duyệt
AUTHOR = "Vua Bảo Hộ"
UA = "VBH-SEO-bot/1.0"  # Sapo chặn User-Agent mặc định của Python (trả 403)


def _headers(json_body=False):
    h = {"User-Agent": UA, "Accept": "application/json"}
    if json_body:
        h["Content-Type"] = "application/json"
    key, secret = os.environ.get("SAPO_API_KEY"), os.environ.get("SAPO_API_SECRET")
    if key and secret:
        h["Authorization"] = "Basic " + base64.b64encode(f"{key}:{secret}".encode()).decode()
    return h


def api(method, path, body=None, retries=3):
    url = f"https://{STORE}/admin/{path}"
    data = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, method=method, headers=_headers(data is not None))
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                text = r.read().decode()
                return json.loads(text) if text.strip() else {}
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:600]
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            sys.exit(f"Lỗi API {method} /admin/{path}: HTTP {e.code} {detail}")
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            sys.exit(f"Lỗi kết nối {url}: {e}")


def fetch(url, method="GET"):
    """Tải một trang web công khai. Trả (status, text)."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, (r.read().decode(errors="replace") if method == "GET" else "")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except urllib.error.URLError as e:
        return 0, str(e)


def out(obj, path=None):
    text = json.dumps(obj, ensure_ascii=False, indent=1)
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Đã ghi {path}")
    else:
        print(text)


def all_articles(blog_id=BLOG_ID):
    rows, page = [], 1
    while True:
        res = api("GET", f"blogs/{blog_id}/articles.json?limit=250&page={page}"
                         "&fields=id,title,alias,published_on,tags,created_on,summary")
        batch = res.get("articles", [])
        rows += batch
        if len(batch) < 250:
            return rows
        page += 1


def all_products():
    rows, page = [], 1
    while True:
        res = api("GET", f"products.json?limit=250&page={page}"
                         "&fields=id,name,alias,product_type,published_on,images,variants,tags")
        batch = res.get("products", [])
        rows += batch
        if len(batch) < 250:
            return rows
        page += 1


def norm(s):
    return (s or "").lower().replace("hoà", "hòa").replace("oà", "òa")


# ---------- lệnh ----------

def cmd_articles(a):
    rows = all_articles()
    if a.published:
        rows = [r for r in rows if r.get("published_on")]
    out(rows, a.out)


def cmd_search_articles(a):
    kws = [norm(k) for k in a.keywords]
    for r in all_articles():
        t = norm(r["title"]) + " " + norm(r["alias"])
        if any(k in t for k in kws):
            state = "hiện" if r.get("published_on") else "ẨN"
            print(f"[{state}] /{r['alias']} | {r['title']}")


def cmd_alias_exists(a):
    for r in all_articles():
        if r["alias"] == a.alias:
            print(f"CÓ: id={r['id']} {'hiện' if r.get('published_on') else 'ẩn'} | {r['title']}")
            sys.exit(0)
    print("CHƯA CÓ")
    sys.exit(1)


def count_auto():
    return sum(1 for r in all_articles() if AUTO_TAG in (r.get("tags") or ""))


def cmd_count_auto(a):
    print(count_auto())


def cmd_products(a):
    rows = []
    for p in all_products():
        if not a.all and not p.get("published_on"):
            continue
        if p.get("tags") and "kho-anh-bai-viet" in p["tags"]:
            continue
        if a.q and not any(norm(q) in norm(p["name"]) for q in a.q):
            continue
        v = (p.get("variants") or [{}])[0]
        rows.append({
            "id": p["id"], "name": p["name"], "url": f"{SITE}/{p['alias']}",
            "type": p.get("product_type"), "price": v.get("price"),
            "published": bool(p.get("published_on")),
            "images": [{"src": "https:" + i["src"] if i["src"].startswith("//") else i["src"],
                        "alt": i.get("alt")} for i in (p.get("images") or [])][: a.max_images],
        })
    out(rows, a.out)


def cmd_collections(a):
    rows = []
    for kind in ("custom", "smart"):
        for c in api("GET", f"{kind}_collections.json?limit=250").get(f"{kind}_collections", []):
            rows.append({"name": c["name"], "url": f"{SITE}/{c['alias']}",
                         "products_count": c.get("products_count"),
                         "published": bool(c.get("published_on"))})
    out(rows, a.out)


def kho_images():
    imgs = api("GET", f"products/{KHO_ANH_ID}/images.json").get("images", [])
    return [{"id": i["id"], "src": "https:" + i["src"] if i["src"].startswith("//") else i["src"],
             "alt": i.get("alt"), "width": i.get("width"), "height": i.get("height")} for i in imgs]


def cmd_kho_images(a):
    rows = kho_images()
    if a.q:
        rows = [r for r in rows if any(norm(q) in norm(r["alt"]) + " " + norm(r["src"]) for q in a.q)]
    out(rows, a.out)


def cmd_prep_image(a):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Thiếu Pillow: chạy `pip install pillow` rồi thử lại.")
    im = Image.open(a.src).convert("RGB")
    if a.crop_dark:  # bỏ viền đen hai bên ảnh dọc
        bbox = im.convert("L").point(lambda v: 255 if v > 20 else 0).getbbox()
        if bbox:
            im = im.crop(bbox)
    im.thumbnail((a.max, a.max))
    im.save(a.dst, "JPEG", quality=a.quality, optimize=True, progressive=True)
    print(f"{a.dst} {im.width}x{im.height} {os.path.getsize(a.dst) // 1024}KB")


def cmd_kho_upload(a):
    with open(a.file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    filename = a.filename or os.path.basename(a.file)
    res = api("POST", f"products/{KHO_ANH_ID}/images.json",
              {"image": {"base64": b64, "filename": filename, "alt": a.alt}})
    img = res.get("image") or {}
    src = img.get("src", "")
    print(json.dumps({"id": img.get("id"), "src": "https:" + src if src.startswith("//") else src,
                      "alt": img.get("alt"), "width": img.get("width"), "height": img.get("height")},
                     ensure_ascii=False))


def _article_payload(spec, creating):
    art = {}
    for k in ("title", "alias", "meta_title", "meta_description", "summary"):
        if spec.get(k):
            art[k] = spec[k]
    if spec.get("content_file"):
        with open(spec["content_file"], encoding="utf-8") as f:
            art["content"] = f.read()
    elif spec.get("content"):
        art["content"] = spec["content"]
    tags = [t.strip() for t in (spec.get("tags") or "").split(",") if t.strip()]
    if creating and AUTO_TAG not in tags:
        tags.append(AUTO_TAG)
    if tags:
        art["tags"] = ", ".join(tags)
    if creating:
        art["author"] = AUTHOR
        art["published"] = False
    if spec.get("image_file"):
        with open(spec["image_file"], "rb") as f:
            art["image"] = {"base64": base64.b64encode(f.read()).decode(),
                            "filename": spec.get("image_filename") or os.path.basename(spec["image_file"])}
    if spec.get("image_alt"):
        art["alt_image"] = spec["image_alt"]
    return art


def cmd_create_article(a):
    with open(a.spec, encoding="utf-8") as f:
        spec = json.load(f)
    for k in ("title", "alias", "meta_title", "meta_description"):
        if not spec.get(k):
            sys.exit(f"Thiếu trường bắt buộc: {k}")
    for r in all_articles():
        if r["alias"] == spec["alias"]:
            sys.exit(f"Đường dẫn /{spec['alias']} đã có bài (id={r['id']}). Chọn đường dẫn khác.")
    res = api("POST", f"blogs/{BLOG_ID}/articles.json", {"article": _article_payload(spec, True)})
    art = res["article"]
    if spec.get("image_alt"):  # alt ảnh đại diện chỉ nhận khi cập nhật
        api("PUT", f"blogs/{BLOG_ID}/articles/{art['id']}.json",
            {"article": {"id": art["id"], "alt_image": spec["image_alt"]}})
    print(json.dumps({"id": art["id"], "alias": art["alias"], "published_on": art["published_on"],
                      "image": (art.get("image") or {}).get("src")}, ensure_ascii=False))


def cmd_update_article(a):
    with open(a.spec, encoding="utf-8") as f:
        spec = json.load(f)
    payload = _article_payload(spec, False)
    payload["id"] = a.id
    if "tags" in payload:  # giữ tag bài tự động, nếu không quy tắc 14 bài đầu sẽ đếm sai
        old = api("GET", f"blogs/{BLOG_ID}/articles/{a.id}.json")["article"].get("tags") or ""
        if AUTO_TAG in old and AUTO_TAG not in payload["tags"]:
            payload["tags"] += f", {AUTO_TAG}"
    res = api("PUT", f"blogs/{BLOG_ID}/articles/{a.id}.json", {"article": payload})
    art = res["article"]
    print(json.dumps({"id": art["id"], "alias": art["alias"], "published_on": art["published_on"]},
                     ensure_ascii=False))


def cmd_publish(a):
    if not a.anh_da_duyet:
        n = count_auto()
        if n <= PHASE1_LIMIT:
            sys.exit(f"KHÔNG ĐĂNG: mới có {n} bài tự động (giai đoạn {PHASE1_LIMIT} bài đầu). "
                     "Bài phải để ẩn chờ anh Luận duyệt. Không tìm cách khác để hiện bài.")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    res = api("PUT", f"blogs/{BLOG_ID}/articles/{a.id}.json",
              {"article": {"id": a.id, "published_on": now}})  # trường "published" không có tác dụng
    art = res["article"]
    print(f"Đã hiện bài id={art['id']} lúc {art['published_on']}: {SITE}/{art['alias']}")


def cmd_get_article(a):
    art = api("GET", f"blogs/{BLOG_ID}/articles/{a.id}.json")["article"]
    if a.content_out:
        with open(a.content_out, "w", encoding="utf-8") as f:
            f.write(art.get("content") or "")
        art["content"] = f"(đã ghi vào {a.content_out})"
    else:
        art["content"] = f"({len(art.get('content') or '')} ký tự)"
    out(art)


def _check_html(html, published):
    rep = {}
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    rep["title"] = t.group(1).strip() if t else None
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    rep["meta_description"] = d.group(1) if d else None
    rep["h1"] = [re.sub("<[^>]+>", "", x).strip() for x in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)][:2]
    ld = []
    for m in re.finditer(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', html, re.S):
        try:
            ld.append(json.loads(m.group(1)).get("@type", "?"))
        except Exception:
            ld.append("LỖI JSON")
    rep["schema"] = ld
    visible = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    rep["json_lo_ra_ngoai"] = "acceptedAnswer" in visible
    return rep


def _img_srcs(html):
    return [s for s in re.findall(r'<img[^>]+src="([^"]+)"', html) if not s.startswith("data:")]


def _check_images(html):
    bad, srcs = [], _img_srcs(html)
    for src in srcs:
        url = "https:" + src if src.startswith("//") else src
        status, _ = fetch(url, "HEAD")
        if status != 200:
            status, _ = fetch(url)
        if status != 200:
            bad.append(f"{status} {url}")
    return len(srcs), bad


def cmd_check_live(a):
    status, html = fetch(f"{SITE}/{a.alias}")
    if status != 200:
        sys.exit(f"Trang {SITE}/{a.alias} trả HTTP {status}")
    rep = _check_html(html, True)
    art = next((r for r in all_articles() if r["alias"] == a.alias), None)
    if art:
        content = api("GET", f"blogs/{BLOG_ID}/articles/{art['id']}.json")["article"].get("content") or ""
        srcs = _img_srcs(content)
        rep["so_anh_trong_bai"], rep["anh_loi"] = _check_images(content)
        rep["anh_khong_thay_tren_trang"] = [s for s in srcs if s.split("?")[0].split("/")[-1] not in html]
    out(rep)


def cmd_check_draft(a):
    art = api("GET", f"blogs/{BLOG_ID}/articles/{a.id}.json")["article"]
    html = art.get("content") or ""
    n, bad = _check_images(html)
    if art.get("image") and art["image"].get("src"):
        src = art["image"]["src"]
        status, _ = fetch("https:" + src if src.startswith("//") else src, "HEAD")
        if status != 200:
            bad.append(f"{status} ảnh đại diện {src}")
    rep = {"id": art["id"], "alias": art["alias"], "published_on": art["published_on"],
           "title": art["title"], "meta_title": art.get("meta_title"),
           "meta_description": art.get("meta_description"),
           "anh_dai_dien": (art.get("image") or {}).get("src"), "alt_anh_dai_dien": art.get("alt_image"),
           "so_anh_trong_bai": n, "anh_loi": bad, "so_h2": html.count("<h2"),
           "co_faq_schema": "FAQPage" in html, "so_chu": len(re.sub("<[^>]+>", " ", re.sub(r"<script.*?</script>", "", html, flags=re.S)).split())}
    out(rep)


def cmd_download(a):
    url = "https:" + a.url if a.url.startswith("//") else a.url
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r, open(a.dst, "wb") as f:
        f.write(r.read())
    print(f"{a.dst} {os.path.getsize(a.dst) // 1024}KB")


def cmd_faq_schema(a):
    """Đọc phần "Câu hỏi thường gặp" (mỗi câu là <h3>, trả lời là <p> ngay sau) và gắn schema FAQPage."""
    with open(a.html, encoding="utf-8") as f:
        html = f.read()
    html = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", html, flags=re.S)
    m = re.search(r"<h2[^>]*>[^<]*(?:Câu hỏi thường gặp|Hỏi đáp|FAQ)[^<]*</h2>(.*?)(?=<h2|$)", html, re.S | re.I)
    if not m:
        sys.exit("Không thấy mục H2 'Câu hỏi thường gặp'.")
    qa = re.findall(r"<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>", m.group(1), re.S)
    if len(qa) < 3:
        sys.exit(f"Mục câu hỏi thường gặp chỉ có {len(qa)} câu, cần ít nhất 3 (h3 + p).")
    clean = lambda s: re.sub(r"\s+", " ", re.sub("<[^>]+>", "", s)).strip()
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(ans)}}
        for q, ans in qa]}
    html = html.rstrip() + '\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n"
    with open(a.html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Đã gắn schema FAQPage ({len(qa)} câu hỏi) vào {a.html}")


def cmd_hide(a):
    res = api("PUT", f"blogs/{BLOG_ID}/articles/{a.id}.json", {"article": {"id": a.id, "published_on": None}})
    print(f"Đã ẩn bài id={a.id}: published_on={res['article']['published_on']}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("articles", help="liệt kê mọi bài trong blog tin tức")
    s.add_argument("--published", action="store_true", help="chỉ bài đang hiện")
    s.add_argument("--out")
    s.set_defaults(f=cmd_articles)

    s = sp.add_parser("search-articles", help="tìm bài cũ theo từ khóa trong tiêu đề/đường dẫn")
    s.add_argument("keywords", nargs="+")
    s.set_defaults(f=cmd_search_articles)

    s = sp.add_parser("alias-exists", help="kiểm tra đường dẫn đã có bài chưa (exit 0 = có)")
    s.add_argument("alias")
    s.set_defaults(f=cmd_alias_exists)

    s = sp.add_parser("count-auto", help=f"đếm bài có tag {AUTO_TAG}")
    s.set_defaults(f=cmd_count_auto)

    s = sp.add_parser("products", help="liệt kê sản phẩm (mặc định chỉ sản phẩm đang hiện)")
    s.add_argument("--q", nargs="*", help="lọc theo tên")
    s.add_argument("--all", action="store_true", help="gồm cả sản phẩm ẩn")
    s.add_argument("--max-images", type=int, default=4)
    s.add_argument("--out")
    s.set_defaults(f=cmd_products)

    s = sp.add_parser("collections", help="liệt kê danh mục sản phẩm")
    s.add_argument("--out")
    s.set_defaults(f=cmd_collections)

    s = sp.add_parser("kho-images", help="liệt kê ảnh trong kho ảnh bài viết")
    s.add_argument("--q", nargs="*", help="lọc theo mô tả ảnh")
    s.add_argument("--out")
    s.set_defaults(f=cmd_kho_images)

    s = sp.add_parser("prep-image", help="thu nhỏ và nén ảnh thành JPG cho web")
    s.add_argument("src")
    s.add_argument("dst")
    s.add_argument("--max", type=int, default=1200)
    s.add_argument("--quality", type=int, default=80)
    s.add_argument("--crop-dark", action="store_true", help="cắt viền đen hai bên")
    s.set_defaults(f=cmd_prep_image)

    s = sp.add_parser("kho-upload", help="tải một ảnh JPG vào kho ảnh, in ra link ảnh")
    s.add_argument("file")
    s.add_argument("--alt", required=True, help="mô tả ảnh tiếng Việt, đúng nội dung ảnh")
    s.add_argument("--filename", help="tên file không dấu, gạch nối")
    s.set_defaults(f=cmd_kho_upload)

    s = sp.add_parser("create-article", help="tạo bài mới ở chế độ ẨN từ file JSON")
    s.add_argument("spec")
    s.set_defaults(f=cmd_create_article)

    s = sp.add_parser("update-article", help="cập nhật bài từ file JSON")
    s.add_argument("id", type=int)
    s.add_argument("spec")
    s.set_defaults(f=cmd_update_article)

    s = sp.add_parser("publish", help=f"hiện bài lên web; tự từ chối khi chưa quá {PHASE1_LIMIT} bài tự động")
    s.add_argument("id", type=int)
    s.add_argument("--anh-da-duyet", action="store_true",
                   help="chỉ dùng khi chính anh Luận vừa bảo đăng bài này; lịch tự động không bao giờ dùng")
    s.set_defaults(f=cmd_publish)

    s = sp.add_parser("hide", help="ẩn lại một bài đang hiện (dùng khi phát hiện lỗi sau khi đăng)")
    s.add_argument("id", type=int)
    s.set_defaults(f=cmd_hide)

    s = sp.add_parser("download", help="tải một file (ví dụ ảnh sản phẩm) về máy")
    s.add_argument("url")
    s.add_argument("dst")
    s.set_defaults(f=cmd_download)

    s = sp.add_parser("faq-schema", help="gắn schema FAQPage vào cuối file HTML bài viết")
    s.add_argument("html")
    s.set_defaults(f=cmd_faq_schema)

    s = sp.add_parser("get-article", help="xem thông tin một bài")
    s.add_argument("id", type=int)
    s.add_argument("--content-out")
    s.set_defaults(f=cmd_get_article)

    s = sp.add_parser("check-draft", help="kiểm tra bài (kể cả bài ẩn) qua API: ảnh, meta, FAQ")
    s.add_argument("id", type=int)
    s.set_defaults(f=cmd_check_draft)

    s = sp.add_parser("check-live", help="kiểm tra trang bài đang hiện trên vuabaoho.com")
    s.add_argument("alias")
    s.set_defaults(f=cmd_check_live)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
