#!/usr/bin/env python3
"""Gửi bài viết cho ChatGPT (OpenAI API) chấm điểm theo seo/tieu-chi-duyet-bai.md.

Mã API do proxy của môi trường gắn vào (Network secret kiểu Bearer cho host
api.openai.com), nên script không cần mã. Nếu chạy ở nơi khác, đặt OPENAI_API_KEY.
Đặt OPENAI_MODEL để chọn model cụ thể; mặc định script tự chọn model GPT mới nhất
mà tài khoản dùng được.

Cách dùng:
  python3 seo/scripts/openai_review.py --article bai.html --brief brief.json --out review.json

brief.json gồm: tu_khoa_chinh, tieu_de, meta_title, meta_description, duong_dan,
nhom_chu_de, nguon_tham_khao (danh sách link/ghi chú dùng để kiểm chứng).

Mã thoát: 0 = có kết quả chấm; 2 = không dùng được OpenAI (chưa có mã API,
mạng chặn, hết tiền...). Khi gặp 2, quy trình chuyển sang để Claude tự duyệt.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.openai.com/v1"
HERE = os.path.dirname(os.path.abspath(__file__))
RUBRIC = os.path.join(HERE, "..", "tieu-chi-duyet-bai.md")
SKIP = ("audio", "realtime", "search", "transcribe", "tts", "image", "embedding", "moderation",
        "instruct", "codex", "vision", "dall", "whisper", "computer", "research", "chat-latest", "oss")


def call(method, path, body=None):
    headers = {"Content-Type": "application/json", "User-Agent": "VBH-SEO-bot/1.0"}
    if os.environ.get("OPENAI_API_KEY"):
        headers["Authorization"] = "Bearer " + os.environ["OPENAI_API_KEY"]
    data = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())


def pick_model():
    if os.environ.get("OPENAI_MODEL"):
        return os.environ["OPENAI_MODEL"]
    ids = [m["id"] for m in call("GET", "/models").get("data", [])]
    cands = [m for m in ids if m.startswith("gpt-") and not any(s in m for s in SKIP)]
    if not cands:
        raise RuntimeError("Tài khoản OpenAI không có model GPT nào dùng được")

    def score(m):
        v = re.match(r"gpt-(\d+(?:\.\d+)?)", m)
        version = float(v.group(1)) if v else 0.0
        small = any(x in m for x in ("mini", "nano"))
        dated = bool(re.search(r"\d{4}-\d{2}-\d{2}", m))
        return (version, not small, not dated, -len(m))

    return max(cands, key=score)


def first_json(text):
    start = text.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        break
        start = text.find("{", start + 1)
    raise ValueError("Không tìm thấy JSON trong câu trả lời")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--article", required=True, help="file HTML nội dung bài")
    p.add_argument("--brief", required=True, help="file JSON mô tả bài")
    p.add_argument("--out", help="ghi kết quả JSON ra file")
    a = p.parse_args()

    with open(RUBRIC, encoding="utf-8") as f:
        rubric = f.read()
    with open(a.article, encoding="utf-8") as f:
        article = f.read()
    with open(a.brief, encoding="utf-8") as f:
        brief = json.load(f)

    system = (
        "Bạn là biên tập viên SEO tiếng Việt khó tính cho website bán đồ bảo hộ lao động vuabaoho.com "
        "(Công ty TNHH Vua Bảo Hộ). Chấm bài theo đúng bảng tiêu chí dưới đây. Soi kỹ mọi con số, quy định, "
        "giá, chính sách, chứng nhận: thứ gì không có trong nguồn tham khảo hoặc dữ liệu sản phẩm thì coi là "
        "chưa kiểm chứng. Chỉ trả về MỘT đối tượng JSON, không viết gì thêm.\n\n" + rubric
    )
    user = (
        "THÔNG TIN BÀI:\n" + json.dumps(brief, ensure_ascii=False, indent=1) +
        "\n\nNỘI DUNG BÀI (HTML):\n" + article +
        '\n\nTrả về JSON dạng: {"diem": <0-100>, "diem_tung_muc": {"<tên mục>": <điểm>}, '
        '"loi_nghiem_trong": ["..."], "can_sua": ["sửa cụ thể, chỉ rõ câu/đoạn"], '
        '"goi_y": ["..."], "nhan_xet": "..."}'
    )
    try:
        model = pick_model()
        res = call("POST", "/chat/completions", {
            "model": model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        })
        verdict = first_json(res["choices"][0]["message"]["content"])
    except urllib.error.HTTPError as e:
        print(f"Không dùng được OpenAI: HTTP {e.code} {e.read().decode(errors='replace')[:300]}", file=sys.stderr)
        sys.exit(2)
    except (urllib.error.URLError, OSError, RuntimeError, ValueError, KeyError) as e:
        print(f"Không dùng được OpenAI: {e}", file=sys.stderr)
        sys.exit(2)

    diem = verdict.get("diem", 0)
    verdict["model"] = model
    verdict["dat"] = isinstance(diem, (int, float)) and diem >= 85 and not verdict.get("loi_nghiem_trong")
    text = json.dumps(verdict, ensure_ascii=False, indent=1)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)


if __name__ == "__main__":
    main()
