import json
from collections import Counter
from pathlib import Path

d = json.loads(Path("output/jiling_templates.json").read_text(encoding="utf-8"))
t = d["templates"]
print("total:", len(t))
print("有提示词:", sum(1 for x in t if x["prompt"]))
print("提取方式:", Counter(x["prompt_extracted_by"] for x in t))
print("提示词长度 min/median/max:",
      min(len(x["prompt"]) for x in t),
      sorted(len(x["prompt"]) for x in t)[len(t)//2],
      max(len(x["prompt"]) for x in t))
print("含负面词提示:", sum(1 for x in t if ("负面" in x["prompt"])))
print("有本地图片:", sum(1 for x in t if x["image_count"]))
print("图片总张数:", sum(x["image_count"] for x in t))
print("多图模板:", [(x["slug"], x["image_count"]) for x in t if x["image_count"] > 1][:10])
print("缺字段统计:", {k: sum(1 for x in t if not x[k]) for k in
      ["category", "model", "aspect_ratio", "size", "scenarios", "tags", "score", "reviews", "steps", "usage_tips"]})
print("分类分布:", Counter(x["category"].split("·")[0].strip() for x in t).most_common(12))
print("模型分布:", Counter(x["model"].split("(")[0].strip() for x in t).most_common(8))
print("\n样例标签:", t[0]["slug"], t[0]["tags"], t[0]["score"], t[0]["reviews"])
print("失败图片:", [(x["slug"], i["url"], i.get("error", "")[:60])
                    for x in t for i in x["images"] if not i.get("local_path")])
kb = Path("output/images")
n = sum(1 for p in kb.rglob("*") if p.is_file())
print("images/ 实际文件数:", n)
