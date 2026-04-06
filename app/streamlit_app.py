#!/usr/bin/env python3
"""
startup-idea Streamlit Web App
创业想法验证工具 - Web 界面版本

使用方法:
    pip install streamlit openai
    streamlit run streamlit_app.py
"""

import streamlit as st
import requests
import json
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="startup-idea - 创业想法验证",
    page_icon="🚀",
    layout="wide"
)

# 标题
st.title("🚀 startup-idea")
st.subheader("30分钟系统验证创业想法，帮早期团队快速判断靠谱程度")

st.markdown("---")

# 侧边栏 - 使用说明
with st.sidebar:
    st.header("📖 使用说明")
    st.markdown("""
    1. 在下方输入你的创业想法
    2. 点击"开始验证"按钮
    3. 等待 AI 完成7维分析
    4. 查看完整验证报告
    """)
    
    st.header("📊 7维评估体系")
    st.markdown("""
    - 痛点强度 (20%)
    - 差异化 (15%)
    - 时机 (15%)
    - 团队 (15%)
    - 商业模式 (15%)
    - 竞争壁垒 (10%)
    - 风险合规 (10%)
    """)
    
    st.header("🔗 关联项目")
    st.markdown("[vc-diligence → 深度尽调](https://github.com/tonyfeng2018/vc-diligence)")

# 主界面
col1, col2 = st.columns([2, 1])

with col1:
    idea_input = st.text_area(
        "💡 输入你的创业想法",
        height=120,
        placeholder="例如：做一个面向HR的AI面试工具，帮助企业快速筛选简历..."
    )
    
    stage = st.selectbox(
        "📍 项目阶段",
        ["Idea", "Pre-MVP", "MVP", "早期增长", "成长期"]
    )

with col2:
    st.markdown("### ⚡ 快速模板")
    st.code("帮我看看这个想法靠不靠谱：\n[你的创业想法]", language="markdown")

# 验证按钮
if st.button("🚀 开始验证", type="primary", use_container_width=True):
    if not idea_input.strip():
        st.warning("请输入创业想法")
    else:
        with st.spinner("🔍 搜索中..."):
            # 这里应该调用 AI API
            # 为了演示，我们展示一个示例输出
            st.success("验证完成！")
            
            # 示例报告
            st.markdown("---")
            st.markdown("## 📊 验证报告")
            
            # 评分卡
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("总分", "7.2/10", "⭐⭐⭐⭐☆")
            with col_b:
                st.metric("推荐", "建议尝试", "需验证")
            with col_c:
                st.metric("数据完整度", "85%", "部分待验证")
            
            # 7维评分表
            st.markdown("### 📈 7维评分表")
            
            scores = {
                "痛点强度": (8, "招聘效率低下是HR痛点"),
                "差异化": (7, "AI面试差异化明确"),
                "时机": (8, "AI面试赛道处于上升期"),
                "团队": (6, "团队背景待进一步了解"),
                "商业模式": (7, "B2B SaaS模式清晰"),
                "竞争壁垒": (6, "需建立数据和算法壁垒"),
                "风险合规": (7, "数据隐私合规需注意")
            }
            
            total = 0
            weights = [0.20, 0.15, 0.15, 0.15, 0.15, 0.10, 0.10]
            
            for i, (dim, (score, note)) in enumerate(scores.items()):
                weighted = score * weights[i]
                total += weighted
                st.progress(score / 10, text=f"{dim}: {score}/10 ({weighted:.1f})")
                st.caption(f"   → {note}")
            
            st.metric("加权总分", f"{total:.1f}/10")
            
            # 最小验证动作
            st.markdown("### 🎯 最小验证动作")
            
            actions = [
                ("竞品体验", "2天", "Moka北森官网"),
                ("HR访谈", "1周", "脉脉/LinkedIn"),
                ("客户调研", "2周", "预约10家目标客户"),
                ("技术验证", "1周", "POC原型开发")
            ]
            
            for action, time, platform in actions:
                st.checkbox(f"{action} ({time})", value=False, key=action)
                st.caption(f"   平台: {platform}")
            
            # 底部提示
            st.markdown("---")
            st.info("💡 提示：建议配合 [vc-diligence](https://github.com/tonyfeng2018/vc-diligence) 进行深度尽调")

# 页脚
st.markdown("---")
st.caption(f"startup-idea v5.3 | 数据截止: {datetime.now().strftime('%Y-%m-%d')}")
