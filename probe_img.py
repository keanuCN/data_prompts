import urllib.request

urls = [
    "https://img.jiling.cc/static/pindou.webp",
    "https://img.jiling.cc/static/templates/aojiao.webp",
    "https://img.jiling.cc/static/templates/qipao-gala/cover.webp",
]
variants = [
    {"User-Agent": "Mozilla/5.0", "Referer": "https://www.jiling.cc/"},
    {"User-Agent": "Mozilla/5.0"},
    {"User-Agent": "curl/8.5.0", "Accept": "*/*"},
    {"User-Agent": "Mozilla/5.0", "Referer": "https://docs.jiling.cc/"},
]
for u in urls:
    print("###", u)
    for v in variants:
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=v), timeout=20)
            b = r.read()
            print("   OK", len(b), r.headers.get("content-type"), r.headers.get("x-cache"), v.get("Referer", "-"))
            break
        except Exception as e:  # noqa: BLE001
            print("   ERR", type(e).__name__, e, "ref:", v.get("Referer", "-"))
