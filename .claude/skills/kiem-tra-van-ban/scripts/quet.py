#!/usr/bin/env python3
"""Quét máy các lỗi bắt được bằng mẫu theo quy-tac-viet-van-ban.md.

Cách dùng:
    python3 quet.py <file.md|file.html|file.txt>
    cat bai.txt | python3 quet.py -

Chỉ bắt lỗi có mẫu cố định (dấu câu, từ cấm, chỗ trống, độ dài câu...).
Các quy tắc cần đọc hiểu (Q12, Q14, Q15, Q16, Q18-Q21, Q24, Q28, Q29) vẫn phải rà tay.
Danh sách từ cấm ở đây phải khớp với bảng Q9, Q10 trong quy-tac-viet-van-ban.md.
"""
import html
import re
import sys

Q9 = [
    # Thổi phồng vai trò
    "đóng vai trò quan trọng", "đóng vai trò then chốt", "đóng vai trò chủ chốt",
    "giữ vai trò", "là minh chứng cho", "minh chứng cho", "khẳng định vị thế",
    "dấu ấn", "di sản", "bước ngoặt", "cột mốc quan trọng", "góp phần không nhỏ",
    "để lại ấn tượng sâu sắc",
    # Quảng cáo rỗng
    "hàng đầu", "đẳng cấp", "vượt trội", "tuyệt vời", "hoàn hảo", "số 1", "đỉnh cao",
    "nâng tầm", "giải pháp toàn diện", "an tâm tuyệt đối", "vượt mong đợi", "không thể bỏ lỡ",
    # Hình ảnh sáo
    "hành trình", "bức tranh", "chìa khóa", "chìa khoá", "mảnh ghép", "bệ phóng",
    "ngọn hải đăng", "khám phá thế giới",
    # Mở bài khuôn
    "trong thời đại 4.0", "thời đại công nghệ số", "trong bối cảnh hiện nay", "ngày nay",
    "hãy cùng tìm hiểu", "bạn có biết",
    # Chen ý kiến
    "đáng chú ý là", "cần lưu ý rằng", "điều quan trọng là", "có thể nói",
    "không thể phủ nhận", "không quá khi nói",
    # Kết bài khuôn
    "tóm lại", "nhìn chung", "tổng kết lại", "có thể thấy", "hy vọng bài viết",
    # Tiếng Anh
    "delve", "tapestry", "testament", "pivotal", "crucial", "vibrant", "showcase",
    "underscore", "foster", "intricate", "landscape", "seamless", "elevate", "robust",
    "realm", "additionally", "moreover", "furthermore",
]
Q9_NOI = ["bên cạnh đó", "ngoài ra", "hơn nữa", "thêm vào đó", "đồng thời"]
Q10 = ["vô cùng", "cực kỳ", "cực kì", "thực sự", "hoàn toàn", "tuyệt đối", "đặc biệt là"]
Q11 = ["được xem là", "được coi là", "đóng vai trò là", "sở hữu"]
Q22 = ["bạn nên lưu ý", "chỉ mang tính tham khảo", "tùy trường hợp", "tuỳ trường hợp"]
Q25 = ["chắc chắn rồi", "dưới đây là", "hy vọng điều này", "hy vọng thông tin",
       "bạn có muốn tôi", "hãy cho tôi biết", "câu hỏi rất hay", "mô hình ai",
       "mô hình ngôn ngữ", "dữ liệu tôi được cập nhật", "as an ai", "i hope this helps",
       "certainly!", "great question"]
Q27 = ["oaicite", "contentreference", "turn0search", "oai_citation", "utm_source=chatgpt",
       "utm_source=openai", "grok_card", "attached_file"]

REGEX = [
    ("Q13", re.compile(r"không chỉ\b.{0,80}?\bmà còn", re.I), "song hành phủ định"),
    ("Q13", re.compile(r"không (?:đơn thuần|phải)\b.{0,80}?\bmà là", re.I), "song hành phủ định"),
    ("Q15", re.compile(r",\s*(?:giúp khẳng định|thể hiện|góp phần|mang lại|khẳng định)\b", re.I),
     "đuôi câu bình luận (xem lại)"),
    ("Q16", re.compile(r"\btừ\s+\S+(?:\s+\S+){0,3}\s+đến\s+\S+", re.I), "khoảng 'từ... đến...' (xem lại thang đo)"),
    ("Q26", re.compile(r"\[[^\]\n]{1,300}\]"), "chỗ trống trong ngoặc vuông"),
    ("Q26", re.compile(r"\bX{3,}\b|\b\d{4}-xx-xx\b|điền vào đây|PASTE_\w+", re.I), "chỗ trống mẫu"),
    ("Q27", re.compile(r"^\s*subject\s*:", re.I | re.M), "dòng Subject:"),
]

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF\U0001F900-\U0001F9FF"
    "\u2705\u2714\u2716\u274C\u2B50\u27A1\uFE0F]"
)


def html_sang_text(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", s)
    s = re.sub(r"(?is)<details.*?</details>", "", s)  # bỏ khối schema/ghi chú kỹ thuật
    s = re.sub(r"(?i)<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", s)
    s = re.sub(r"(?i)<li[^>]*>", "\n- ", s)
    s = re.sub(r"(?i)</?(strong|b)>", "**", s)
    s = re.sub(r"(?i)<(br|/p|/h[1-6]|/li|/tr|/figcaption|/dd|/div|p|tr|figcaption|dt|dd|div)[^>]*>", "\n", s)
    s = re.sub(r"(?i)<t[dh][^>]*>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s)


def dem_chu(cau):
    return len(re.findall(r"[^\s|#*\-]+", cau))


def tach_cau(doan):
    return [c.strip() for c in re.split(r"(?<=[.!?…])\s+", doan) if c.strip()]


def quet(text):
    loi = []
    lines = text.split("\n")
    lower_lines = [l.lower() for l in lines]

    def them(q, dong, mo_ta, trich):
        loi.append((q, dong, mo_ta, trich.strip()[:110]))

    so_cham_than = 0
    noi_dem = []
    for i, (l, ll) in enumerate(zip(lines, lower_lines), 1):
        if not l.strip():
            continue
        for ch in ("—", "–"):
            if ch in l:
                them("Q1", i, f"gạch ngang dài '{ch}'", l)
        if EMOJI.search(l):
            them("Q2", i, "emoji / ký hiệu trang trí", l)
        if re.search("[“”‘’]", l):
            them("Q3", i, "nháy cong", l)
        dam = len(re.findall(r"\*\*[^*]+\*\*", l))
        if dam > 1:
            them("Q4", i, f"{dam} cụm in đậm trong một đoạn", l)
        if re.match(r"\s*[-*+]\s+\*\*[^*]{1,60}:\*\*|\s*[-*+]\s+\*\*[^*]{1,60}\*\*\s*:", l):
            them("Q5", i, "gạch đầu dòng kiểu '**Tiêu đề:** nội dung'", l)
        m = re.match(r"\s*#{1,6}\s+(.*)", l)
        if m:
            tu = [t for t in re.findall(r"[^\s:|,.?!]+", m.group(1)) if t[0].isalpha()]
            hoa = [t for t in tu[1:] if t[0].isupper()]
            if len(tu) >= 4 and len(hoa) >= 0.6 * (len(tu) - 1):
                them("Q6", i, "tiêu đề viết hoa mọi chữ (kiểm tra tên riêng)", l)
        if "!!" in l:
            them("Q8", i, "dấu chấm than liên tiếp", l)
        so_cham_than += l.count("!")
        for ds, q, mo_ta in ((Q9, "Q9", "từ cấm"), (Q10, "Q10", "từ nhấn vô nghĩa"),
                             (Q11, "Q11", "né chữ 'là'"), (Q22, "Q22", "rào đón"),
                             (Q25, "Q25", "câu thoại AI"), (Q27, "Q27", "mã rác AI")):
            for w in ds:
                if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", ll):
                    them(q, i, f"{mo_ta}: '{w}'", l)
        for w in Q9_NOI:
            if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", ll):
                noi_dem.append((i, w, l))
        for q, rx, mo_ta in REGEX:
            for mm in rx.finditer(l):
                them(q, i, mo_ta, mm.group(0) if q == "Q26" else l)
        if not l.lstrip().startswith(("#", "|")):
            noi_dung = re.sub(r"^\s*[-*+]\s+", "", l)
            cau_list = tach_cau(noi_dung)
            for c in cau_list:
                n = dem_chu(c)
                if n > 30:
                    them("Q17", i, f"câu {n} chữ (tối đa 30)", c)
            if len(cau_list) > 4:
                them("Q17", i, f"đoạn {len(cau_list)} câu (tối đa 4)", l)

    if so_cham_than > 1:
        them("Q8", 0, f"cả bài có {so_cham_than} dấu chấm than (tối đa 1)", "")
    if len(noi_dem) > 1:
        for i, w, l in noi_dem:
            them("Q9", i, f"từ nối thừa '{w}' (cả bài {len(noi_dem)} lần, tối đa 1)", l)
    md = re.search(r"^\s*#{1,6}\s|\*\*[^*]+\*\*|^\s*\|.*\|\s*$", text, re.M)
    return loi, bool(md)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    src = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    if re.search(r"(?i)<(p|div|article|li|h[1-6])\b", src):
        src = html_sang_text(src)
    loi, co_md = quet(src)
    if not loi:
        print("KHÔNG thấy lỗi máy bắt được. Vẫn phải rà tay các quy tắc còn lại.")
    else:
        print(f"Tìm thấy {len(loi)} lỗi máy bắt được:\n")
        for q, dong, mo_ta, trich in sorted(loi, key=lambda x: (int(x[0][1:]), x[1])):
            vi_tri = f"dòng {dong}" if dong else "cả bài"
            print(f"[{q}] {vi_tri}: {mo_ta}\n      > {trich}")
    if co_md:
        print("\nLưu ý Q7: văn bản có ký hiệu Markdown. Nếu đăng Zalo, Facebook, TikTok, Shopee thì phải bỏ.")
    sys.exit(1 if loi else 0)


if __name__ == "__main__":
    main()
