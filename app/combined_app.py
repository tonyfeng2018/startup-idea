#!/usr/bin/env python3
"""
AI创业工具箱 - 合并版
startup-idea + vc-diligence 在同一个网站
通过按钮切换不同功能
"""

import os
import streamlit as st
import requests
from datetime import datetime

# ==================== 配置 ====================
API_BASE = os.environ.get("API_BASE", "http://localhost:5001")

# ==================== VC阶段权重配置 ====================
VC_STAGES = {
    "天使/Pre-Seed": {"team": 40, "market": 30, "product": 20, "traction": 20, "biz": 10, "competition": 10, "finance": 5},
    "种子轮": {"team": 35, "market": 25, "product": 20, "traction": 25, "biz": 15, "competition": 10, "finance": 10},
    "A轮": {"team": 30, "market": 20, "product": 20, "traction": 30, "biz": 20, "competition": 10, "finance": 15},
    "B轮+": {"team": 20, "market": 15, "product": 15, "traction": 25, "biz": 25, "competition": 15, "finance": 25},
    "二级市场": {"team": 10, "market": 15, "product": 15, "traction": 20, "biz": 20, "competition": 15, "finance": 30},
}

# ==================== 通用样式 ====================
st.set_page_config(
    page_title="AI创业工具箱",
    page_icon="🧰",
    layout="wide"
)

def set_bg_color():
    st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    div[data-testid="stHorizontalBlock"] > div { border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

set_bg_color()

# ==================== Session State 初始化 ====================
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# ==================== 页面定义 ====================

def render_home():
    """首页 - 工具选择"""
    st.title("🧰 AI创业工具箱")
    st.markdown("#### YC+A16Z方法论驱动，数据验证决策")
    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 30px; border-radius: 16px; text-align: center; box-shadow: 0 4px 20px rgba(102,126,234,0.3);">
            <h2 style="color: white; margin-bottom: 15px;">🚀 startup-idea</h2>
            <p style="color: #e0e0e0; font-size: 15px; margin-bottom: 20px;">30分钟验证创业想法<br/>七维评估体系 · 数据驱动</p>
            <p style="color: #c0c0c0; font-size: 13px;">痛点 | 差异化 | 时机 | 团队<br/>商业 | 壁垒 | 合规</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 启动 startup-idea", use_container_width=True, type="primary"):
            st.session_state["current_page"] = "startup"
            st.rerun()

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 50px 30px; border-radius: 16px; text-align: center; box-shadow: 0 4px 20px rgba(17,153,142,0.3);">
            <h2 style="color: white; margin-bottom: 15px;">📊 vc-diligence</h2>
            <p style="color: #e0e0e0; font-size: 15px; margin-bottom: 20px;">AI生成项目尽调报告<br/>六维评估 · 结构化输出</p>
            <p style="color: #c0c0c0; font-size: 13px;">团队 | 市场 | 产品 | 增长<br/>商业 | 竞争</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 启动 vc-diligence", use_container_width=True, type="primary"):
            st.session_state["current_page"] = "vc"
            st.rerun()

    st.markdown("---")
    st.caption(f"AI创业工具箱 | {datetime.now().strftime('%Y-%m-%d')}")


def render_startup():
    """startup-idea 工具"""
    st.title("🚀 startup-idea")
    st.caption("七维评估体系 · YC+A16Z方法论")
    st.markdown("---")

    if st.button("← 返回工具箱", use_container_width=True):
        st.session_state["current_page"] = "home"
        st.rerun()

    with st.sidebar:
        st.header("📖 使用说明")
        st.markdown("""
        1. 输入你的创业想法
        2. 选择分析深度
        3. 等待 AI 完成分析
        4. 查看详细验证报告
        """)
        st.header("📊 七维评估体系")
        st.markdown("""
        - **痛点强度** (20%)
        - **差异化** (15%)
        - **时机窗口** (15%)
        - **团队匹配** (15%)
        - **商业模式** (15%)
        - **竞争壁垒** (10%)
        - **风险合规** (10%)
        """)
        st.header("⚡ 分析模式")
        mode = st.radio("选择分析深度",
            ["⚡ 快速验证（30秒）", "📊 完整验证（3分钟）"],
            index=0, label_visibility="collapsed")
        analysis_mode = "quick" if "快速" in mode else "full"

    idea_input = st.text_area(
        "💡 输入你的创业想法",
        height=120,
        placeholder="例如：做一个面向HR的AI面试工具，帮助企业快速筛选简历..."
    )

    col_btn, col_mode = st.columns([1, 3])
    with col_btn:
        submit = st.button("🚀 开始验证", type="primary", use_container_width=True)
    with col_mode:
        st.caption(f"当前模式: {'快速验证' if analysis_mode == 'quick' else '完整验证'}")

    if submit or idea_input:
        if not idea_input.strip():
            st.warning("请输入创业想法")
        else:
            with st.spinner("🔍 分析中，请稍候（首次约30秒）..."):
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
                        save_path = f"/tmp/idea-validation-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.md"
                        with open(save_path, "w") as f:
                            f.write(f"# 创业想法验证报告\n\n## 想法\n{idea_input}\n\n## 报告\n{result}\n")
                        st.info(f"💾 报告已保存: {save_path}")
                    else:
                        st.error(f"API错误: {resp.status_code}")
                except requests.exceptions.ConnectionError:
                    st.error("❌ 无法连接后端API，请确保服务已启动")
                except Exception as e:
                    st.error(f"分析失败: {str(e)}")

    st.markdown("---")
    st.caption(f"startup-idea v5.4 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")


def render_vc():
    """vc-diligence 工具 - 简化版，AI生成"""
    st.title("📊 vc-diligence 项目尽调")
    st.caption("六维评估体系 · 投资人心智")
    st.markdown("---")

    if st.button("← 返回工具箱", use_container_width=True):
        st.session_state["current_page"] = "home"
        st.rerun()

    with st.sidebar:
        st.header("📖 使用说明")
        st.markdown("""
        1. 输入投资/考察的项目名称和描述
        2. 选择分析深度
        3. 等待 AI 生成尽调报告
        """)
        st.header("📊 六维评估体系")
        st.markdown("""
        - **团队** — 创始人背景、团队完整性
        - **市场** — 规模、增速、痛点
        - **产品** — 解决方案、差异化
        - **Traction** — 用户数据、收入
        - **商业模式** — 如何赚钱、单位经济
        - **竞争格局** — 护城河、竞品对比
        """)
        st.header("⚡ 分析模式")
        mode = st.radio("选择分析深度",
            ["⚡ 快速验证（30秒）", "📄 完整报告（3分钟）"],
            index=0, label_visibility="collapsed")
        analysis_mode = "quick" if "快速" in mode else "full"

    st.subheader("📝 输入要尽调的项目")

    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input(
            "项目名称",
            placeholder="例如：MiniMax / 字节跳动AI教育"
        )
        funding_stage = st.selectbox(
            "融资阶段",
            list(VC_STAGES.keys()),
            index=1
        )
    with col2:
        weights = VC_STAGES[funding_stage]
        st.caption("当前阶段权重参考：")
        for dim, w in weights.items():
            st.caption(f"  · {dim}: {w}%")

    idea_input = st.text_area(
        "💡 项目介绍",
        height=120,
        placeholder="描述这个项目是做什么的、核心优势、融资情况、创始人背景等..."
    )

    col_btn, col_mode = st.columns([1, 3])
    with col_btn:
        submit = st.button("📊 开始尽调", type="primary", use_container_width=True)
    with col_mode:
        st.caption(f"当前模式: {'快速验证' if analysis_mode == 'quick' else '完整报告'}")

    if submit or idea_input:
        if not idea_input.strip():
            st.warning("请输入项目介绍")
        elif not project_name.strip():
            st.warning("请填写项目名称")
        else:
            with st.spinner("🔍 尽调分析中，请稍候（首次约30秒）..."):
                try:
                    prompt = build_vc_prompt(project_name.strip(), funding_stage, idea_input.strip(), analysis_mode)
                    resp = requests.post(
                        f"{API_BASE}/analyze",
                        json={"idea": prompt, "mode": analysis_mode},
                        timeout=180
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        result = data["result"]
                        st.success("✅ 尽调报告生成完成！")
                        st.markdown("---")
                        st.markdown(f"## 📊 尽调报告 — {project_name}")
                        st.markdown(f"**阶段**: {funding_stage} | **分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
                        st.markdown("---")
                        st.markdown(result)
                        save_path = f"/tmp/vc-diligence-{project_name.replace('/', '-')}-{datetime.now().strftime('%Y-%m-%d')}.md"
                        with open(save_path, "w") as f:
                            f.write(f"# 尽调报告 — {project_name}\n\n## 基本信息\n- **阶段**: {funding_stage}\n- **介绍**: {idea_input}\n\n## 报告\n{result}\n")
                        st.info(f"💾 报告已保存: {save_path}")
                    else:
                        st.error(f"API错误: {resp.status_code}")
                except requests.exceptions.ConnectionError:
                    st.error("❌ 无法连接后端API，请确保服务已启动")
                except Exception as e:
                    st.error(f"分析失败: {str(e)}")

    st.markdown("---")
    st.caption(f"vc-diligence v3.4 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")


def build_vc_prompt(name, stage, desc, mode):
    """构建VC尽调的prompt"""
    if mode == "quick":
        return f"""你是专业投资人，请对以下项目进行快速尽调验证。

项目名称：{name}
融资阶段：{stage}
项目介绍：{desc}

请输出：
1. **核心结论**（值得跟/观望/不建议）1句话
2. **六维评分简表**：团队/市场/产品/Traction/商业/竞争 各1-5星+1句话说明
3. **最关键的一件事**：作为投资人最需要验证的一件事
4. **最小验证动作**：2个具体可执行的下一步（带平台和关键词）

格式简洁，总字数不超过400字。"""
    else:
        return f"""你是YC+A16Z方法论驱动的专业投资人，请对以下项目进行深度尽调。

项目名称：{name}
融资阶段：{stage}
项目介绍：{desc}

请输出完整尽调报告，必须包含：

### 1. 核心结论
（值得跟/需深入验证/不建议）+ 3句话理由

### 2. 六维评分（必须量化）
| 维度 | 评分(1-5) | 量化数据 | 说明 |
|------|-----------|---------|------|
| 团队 | ⭐ | [创始人背景/经历] | |
| 市场 | ⭐ | [TAM/增速/痛点频率] | |
| 产品 | ⭐ | [解决方案/差异化程度] | |
| Traction | ⭐ | [用户数/收入/留存] | |
| 商业模式 | ⭐ | [ARPU/CAC/LTV] | |
| 竞争 | ⭐ | [护城河深度] | |

### 3. 竞品 Feature Matrix
| 竞品 | 核心功能 | 定价 | 市场份额 | 差评痛点 |
|------|---------|------|---------|---------|
| [主要竞品] | | | | |

### 4. SWOT 分析
| 优势(S) | 劣势(W) |
|---------|---------|
| | |
| 机会(O) | 威胁(T) |
|---------|---------|

### 5. 关键假设验证清单
| 假设 | 验证方式 | 当前状态 |
|------|---------|---------|
| | | ✅已验证/❓待验证/❌不成立 |

### 6. 最小验证动作（带时间+平台+关键词）
| # | 动作 | 时间 | 平台 | 关键词 | 具体操作 |
|---|------|------|------|--------|---------|

### 7. 风险评估
Top3风险 + 缓解方案 + 严重程度

### 8. 数据来源脚注
每项评分必须注明数据来源或标注"需进一步验证"

格式详细完整，总字数1500-3000字。"""


# ==================== 路由 ====================
if st.session_state["current_page"] == "home":
    render_home()
elif st.session_state["current_page"] == "startup":
    render_startup()
elif st.session_state["current_page"] == "vc":
    render_vc()
