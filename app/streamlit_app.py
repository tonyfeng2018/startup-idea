#!/usr/bin/env python3
"""
startup-idea Streamlit Web App
创业想法验证工具 - Web 界面版本

使用方法:
    pip install streamlit requests
    streamlit run streamlit_app.py
"""

import os
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

# API配置
API_BASE = os.environ.get("API_BASE", "http://localhost:5001")

# 标题
st.title("🚀 startup-idea")
st.subheader("YC+A16Z方法论 · 七维评估体系 · 数据驱动决策")

st.markdown("---")

# 侧边栏 - 使用说明
with st.sidebar:
    st.header("📖 使用说明")
    st.markdown("""
    1. 输入你的创业想法
    2. 选择分析深度（快速/完整）
    3. 等待 AI 完成分析
    4. 查看详细验证报告
    """)
    
    st.header("📊 七维评估体系")
    st.markdown("""
    - **痛点强度** (20%) — 不解决的代价
    - **差异化** (15%) — 比竞品好多少
    - **时机窗口** (15%) — 为什么是现在
    - **团队匹配** (15%) — 需要的基因
    - **商业模式** (15%) — 怎么赚钱
    - **竞争壁垒** (10%) — 护城河
    - **风险合规** (10%) — 隐患评估
    """)
    
    st.header("⚡ 分析模式")
    mode = st.radio("选择分析深度", ["⚡ 快速验证（30秒）", "📊 完整验证（3分钟）"], index=0)
    analysis_mode = "quick" if "快速" in mode else "full"
    
    st.header("🔗 相关项目")
    st.markdown("[vc-diligence → 深度尽调](https://github.com/tonyfeng2018/vc-diligence)")
    st.markdown("[查看示例报告 →](https://github.com/tonyfeng2018/startup-idea/blob/main/examples/idea-validator-v5-full-report.md)")

# 主界面
idea_input = st.text_area(
    "💡 输入你的创业想法",
    height=120,
    placeholder="例如：做一个面向HR的AI面试工具，帮助企业快速筛选简历..."
)

col1, col2 = st.columns([1, 3])
with col1:
    submit = st.button("🚀 开始验证", type="primary", use_container_width=True)
with col2:
    st.caption(f"分析模式: {'快速验证' if analysis_mode == 'quick' else '完整验证'}")

if submit or idea_input:
    if not idea_input.strip():
        st.warning("请输入创业想法")
    else:
        with st.spinner("🔍 分析中，请稍候..."):
            try:
                resp = requests.post(
                    f"{API_BASE}/analyze",
                    json={"idea": idea_input.strip(), "mode": analysis_mode},
                    timeout=180
                )
                if resp.status_code == 200:
                    data = resp.json()
                    result = data["result"]
                    
                    st.success("✅ 分析完成！")
                    st.markdown("---")
                    st.markdown("## 📊 验证报告")
                    st.markdown(result)
                    
                    # 保存到文件
                    save_path = f"/tmp/idea-validation-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.md"
                    with open(save_path, "w") as f:
                        f.write(f"# 创业想法验证报告\n\n## 想法\n{idea_input}\n\n## 报告\n{result}\n")
                    st.info(f"💾 报告已保存至: {save_path}")
                else:
                    st.error(f"API错误: {resp.status_code} - {resp.text}")
                    st.info("💡 提示：确保后端API服务已启动（python api_server.py）")
            except requests.exceptions.ConnectionError:
                st.error("❌ 无法连接到后端API服务")
                st.info("请在终端运行: `python api_server.py`")
            except Exception as e:
                st.error(f"分析失败: {str(e)}")

# 页脚
st.markdown("---")
st.caption(f"startup-idea v5.3 | 分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
