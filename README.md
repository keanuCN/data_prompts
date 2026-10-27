# 图像模板提示词数据集

批量采集的 AI 图像生成模板：**提示词 + 效果图 + 元信息**。

- 模板数：**217**（提示词提取成功率 100%）
- 效果图：**216** 张 / 约 15.5 MB
- 采集时间：2026-10-27

## 目录结构

```
scrape_jiling.py              采集脚本
verify.py                     数据集质量校验
probe.py / probe_img.py       页面结构与图片 URL 的调试探针
output/
  jiling_templates.json       结构化全量数据（推荐程序使用）
  jiling_templates.xlsx       表格版：templates 表 + images 表
  jiling_templates.md         阅读版：提示词代码块 + 内嵌效果图
  images/<slug>/              每个模板的效果图
  raw_html/<slug>.html        原始 HTML 备份，可离线重解析
```

## 字段说明

`templates[]` 每条记录：

| 字段 | 含义 |
| --- | --- |
| `slug` | 模板标识，也是图片目录名 |
| `title` / `description` | 模板名称与简介 |
| `category` | 分类，如 `AI变装 · 写真` |
| `tags` | 标签列表 |
| `model` | 站方推荐模型 |
| `aspect_ratio` / `size` | 默认画幅 / 默认尺寸 |
| `scenarios` | 适用场景 |
| `prompt` | **提示词全文**（含站方给出的负面词） |
| `prompt_extracted_by` | 提取路径标记，全部为 `section:提示词怎么改` |
| `steps` / `reference_image_advice` / `usage_tips` | 3 步上手、参考图建议、使用建议 |
| `score` / `reviews` | 站内评分与评价数 |
| `images[]` | `url` / `alt` / `role` / `local_path`（相对 `output/`）/ `bytes` / `format` |
| `docs_url` / `live_url` | 文档页与主站使用入口 |

分布概况：分类以 AI变装(52)、社媒内容(36)、电商(30)、广告创意(23)、IP形象/手办(23)、二次元(22) 为主；推荐模型为 GPT Image 2(117)、Nano Banana Pro(65)、Gemini 3.1 Flash Image Preview(35)。提示词长度中位数 204 字，最短 12 字（模板本身就这么短），最长 1149 字。

## 复现 / 更新

```bash
python scrape_jiling.py                # 全量（页面 + 图片）
python scrape_jiling.py --limit 20     # 试跑前 20 个
python scrape_jiling.py --no-images    # 只要提示词
python scrape_jiling.py --workers 10   # 调整并发
python verify.py                       # 校验完整性
```

脚本只用标准库（`urllib` + 正则 + `concurrent.futures`），写 xlsx 时才需要 `openpyxl`。

## 已知问题

3 个模板的效果图在站方 CDN 上本身就是 404（换 UA / Referer 结果相同），对应目录为空，URL 仍保留在 JSON 里：

`perler-bead-pixel-pattern` · `pink-tsundere-portrait` · `qipao-gala`

