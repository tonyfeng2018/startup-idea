#!/usr/bin/env python3
"""
startup-idea Flask API Server
创业想法验证后端服务
"""

import os
import sys
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MiniMax API配置
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")
MINIMAX_URL = "https://api.minimax.chat/v1/chat/completions"
MODEL = "MiniMax-Text-01"

def call_minimax(prompt, max_tokens=8000, temperature=0.7):
    """调用MiniMax API"""
    headers = {
        "Authorization": f"Bearer {MINIMAX_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    try:
        resp = requests.post(MINIMAX_URL, headers=headers, json=payload, timeout=120)
        if resp.status_code == 200:
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        else:
            return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def build_analysis_prompt(idea):
    """构建完整的七维分析prompt"""
    return f"""你是YC+A16Z方法论驱动的创业想法验证专家。请对以下创业想法进行深度七维评估。

## 创业想法
{idea}

## 评估要求
请依次完成以下6个维度的深度分析（必须包含真实数据支撑）：

### 维度1：痛点强度（1-5星）
- 用户多久疼一次？（每天/每周/每月）
- 不解决会怎样？（直接影响收入/效率/体验）
- 是否有调研数据支撑痛点出现频率？

### 维度2：竞品分析（必须包含）
请搜索以下信息：
- 主要竞品有哪些？（至少5个，包括用友大易、北森等）
- 竞品最新融资和估值？
- 竞品定价是多少？（具体¥/月或¥/年）
- 竞品差评Top痛点是什么？（占比%）
- 空白点：哪个需求没有被竞品满足？

### 维度3：市场规模
- TAM/SAM/SOM分别是多少亿？
- 赛道近2年增速数据？
- 渗透率/使用率数据？

### 维度4：时机窗口
- 为什么是2025-2026年而不是更早或更晚？
- 有哪些结构性变化？（政策/技术/用户习惯）

### 维度5：商业模式
- 怎么赚钱？（订阅/交易抽成/增值/广告）
- 客单价（ARPU）预估？
- 获客成本（CAC）预估？
- LTV/CAC能>3x吗？

### 维度6：风险与合规
- Top3风险是什么？严重程度？缓解方案？
- 隐私合规/算法偏见/AI监管风险各如何？

### 维度7：团队匹配
- 这个方向需要什么基因的团队？
- 典型创始人背景是什么？

## 输出格式
请输出详细的markdown格式报告，包含：
1. 核心结论（能做/需差异化/不建议）
2. 七维评分表（每维1-5星+量化数据支撑）
3. 竞品Feature Matrix表格
4. 空白点分析
5. SWOT分析
6. 关键假设验证清单
7. 最小验证动作（带时间+平台+关键词）
8. 数据来源脚注

请基于真实市场数据进行分析，不要编造数字。"""
    # 维度8：退出参考
    # - 行业有哪些上市/被收购案例？
    # - 估值参考？

def build_quick_prompt(idea):
    """快速验证prompt"""
    return f"""你是YC+A16Z方法论驱动的创业想法验证专家。请快速评估以下创业想法。

想法：{idea}

请输出：
1. 核心结论（能做/需差异化/不建议）1句话
2. 七维评分简表：痛点/差异化/时机/团队/商业/壁垒/合规（各1-5星+1句话说明）
3. 最重要的一件事：如果这个想法靠谱，最需要验证的一件事是什么？
4. 最小验证动作：2个具体可执行的下一步（带平台和关键词）

格式简洁，总字数不超过500字。"""

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    idea = data.get("idea", "").strip()
    mode = data.get("mode", "quick")  # quick or full
    
    if not idea:
        return jsonify({"error": "请输入创业想法"}), 400
    
    if not MINIMAX_API_KEY:
        return jsonify({"error": "API Key未配置"}), 500
    
    # 构建prompt
    if mode == "full":
        prompt = build_analysis_prompt(idea)
        max_tokens = 8000
    else:
        prompt = build_quick_prompt(idea)
        max_tokens = 2000
    
    # 调用API
    result = call_minimax(prompt, max_tokens=max_tokens)
    
    return jsonify({
        "idea": idea,
        "mode": mode,
        "result": result
    })

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "startup-idea API",
        "version": "1.0",
        "endpoints": {
            "POST /analyze": "分析创业想法（body: {idea, mode: 'quick'|'full'}）",
            "GET /health": "健康检查"
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"🚀 startup-idea API 启动于端口 {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
