# 🚀 startup-idea

> **30分钟系统验证创业想法，帮早期团队快速判断靠谱程度**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-v5.3-blue.svg)](./CHANGELOG.md)
[![Powered by YC+A16Z](https://img.shields.io/badge/Powered%20by-YC%2BA16Z-purple.svg)](https://www.ycombinator.com/)

---

## 🎯 一句话说明

这是一个基于 AI 的**创业想法验证 Skills**，帮助创业者在 **30分钟内** 系统性验证一个想法是否靠谱。核心方法论来自 YC + A16Z，结合中国市场实际情况，输出结构化的七维评估报告 + 可执行的最小验证动作。

---

## ✨ Features

- 📊 **七维评估体系** — 痛点 / 差异化 / 时机 / 团队 / 商业 / 竞争壁垒 / 风险合规
- 🔍 **并行搜索6项强制规则** — 竞品 / 市场规模 / 渗透率 / 定价 / 差评 / 融资，必须全部完成再生成报告
- 📈 **竞品 Feature Matrix** — 6个竞品全覆盖（功能/定价/市场份额/差评痛点）
- 💡 **SWOT + 关键假设清单** — 3-5条假设 + 验证方式 + 状态（✅已验证/❓待验证）
- 🎯 **最小验证动作** — 带时间/平台/关键词的具体可执行任务
- 📑 **Pitch Deck摘要** — 自动生成3页核心内容（问题解决/市场竞争/商业模式）
- 🛡️ **透明[待验证]处理** — 缺失数据主动标注，提供验证平台和关键词

---

## 📸 示例输出

### 7维评分表示例

| 维度 | 权重 | 评分 | 加权 |
|-----|------|------|------|
| 痛点强度 | 20% | 8 | 1.6 |
| 差异化 | 15% | 7 | 1.05 |
| 时机 | 15% | 8 | 1.2 |
| 团队 | 15% | 6 | 0.9 |
| 商业模式 | 15% | 7 | 1.05 |
| 竞争壁垒 | 10% | 6 | 0.6 |
| 风险合规 | 10% | 7 | 0.7 |
| **总计** | **100%** | - | **7.1** |

### 竞品矩阵（Mermaid）

```mermaid
| 竞品 | AI面试 | 简历筛选 | 薪资分析 | 定价 |
|-----|:------:|:--------:|:--------:|-----|
| Interview.ai | ✅ | ✅ | ❌ | ¥999/月 |
| 简历家 | ✅ | ✅ | ✅ | ¥499/月 |
| 薪人薪事 | ❌ | ✅ | ✅ | ¥1999/年 |
```

### SWOT 一句话总结

> **优势**：HR行业积累深 + AI技术储备足 | **劣势**：品牌认知弱 + 销售团队搭建中  
> **机会**：SaaS渗透率提升 + AI面试刚需 | **威胁**：大厂入场 + 经济下行企业缩减招聘

---

## ⚡ Quick Start

### 一键复制 Prompt

```
帮我看看这个想法靠不靠谱：[你的创业想法]
```

### 完整使用示例

```
用户：帮我看看这个想法：做一个面向HR的AI面试工具

AI：[按照7维体系分析，执行搜索，输出完整报告]
```

---

## 🎬 演示视频

> 正在录制中，敬请期待...

---

## 📋 适用场景

| 场景 | 说明 |
|------|------|
| 👨‍💼 **创业者** | 验证自己的创业想法是否靠谱 |
| 🏢 **孵化器** | 批量评估入驻项目 |
| 🏆 **大赛评委** | 快速评估参赛项目 |
| 💼 **投资人** | 早期项目快速筛选 |
| 🎓 **MBA/创业课程** | 教学演示框架 |

---

## 📁 目录结构

```
startup-idea/
├── README.md                    # 本文件
├── SKILL.md                     # 技能指令（含v5.3更新）
├── CHANGELOG.md                 # 版本历史
├── LICENSE                      # MIT License
├── app/
│   └── streamlit_app.py         # 🌐 Web演示界面（Streamlit）
├── examples/
│   └── demo_prompt.md          # 示例Prompt
├── report/
│   └── idea-validator-v5-full-report.md  # v5完整报告示例
├── template/
│   └── idea-validator-v5-template.md      # 七维评估标准模板
└── update-log/
    └── skills-update-log-...md           # 迭代更新日志
```

---

## 🛠️ 本地运行

### 方式一：Streamlit Web 界面（推荐）

```bash
cd app
pip install streamlit requests
streamlit run streamlit_app.py
```

然后在浏览器打开 `http://localhost:8501`

### 方式二：Python 脚本

```bash
cd examples
python run_analysis.py "你的创业想法"
```

---

## 🔗 关联项目

- **[vc-diligence](https://github.com/tonyfeng2018/vc-diligence)** — 投资尽职调查，完成想法验证后可继续进行深度尽调

---

## 📝 更新日志

👉 [CHANGELOG.md](./CHANGELOG.md)

记录了从 v1 到 v5.3 的所有迭代优化点。

---

## ⚠️ 数据说明

本项目中的报告和模板默认依赖外部搜索工具获取实时数据。

当搜索工具无法访问时，所有量化数据会标注 `[待验证]`，并提供具体验证平台（官网/报告名称/搜索关键词），确保可追溯和可补充。

---

## 🔑 核心设计原则

1. **数据驱动** — 每个评分必须有量化依据，无法量化则标注[待验证]
2. **诚实比完整更重要** — 宁可承认数据缺失，也不要假装有数据
3. **搜索失败是常态** — 必须设计降级方案，不能依赖单一搜索工具
4. **验证方式比数据更重要** — 用户拿着"待验证"标注可以去自行核实
5. **模板是骨架，思考是灵魂** — 结构化输出是下限，深度分析才是价值

---

## 📄 License

MIT License - see [LICENSE](./LICENSE) file.

---

*Last updated: 2026-04-06*  
*Author: Tony F*  
*GitHub: https://github.com/tonyfeng2018/startup-idea*
