#!/usr/bin/env python3
"""
startup-idea CLI 工具
命令行版本创业想法验证

使用方法:
    python run_analysis.py "你的创业想法"
"""

import sys
import os

# 打印使用说明
def print_usage():
    print("""
🚀 startup-idea - 创业想法验证工具
=====================================

使用方法:
    python run_analysis.py "你的创业想法"

示例:
    python run_analysis.py "做一个面向HR的AI面试工具"
    python run_analysis.py "开发一个面向中小企业的SaaS财务工具"

注意事项:
    - 需要配置 OpenAI API Key (或使用其他兼容 API)
    - 可以通过环境变量设置: export OPENAI_API_KEY=your_key
""")

# 主函数
def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    idea = " ".join(sys.argv[1:])
    
    print(f"\n🚀 正在验证想法: {idea}\n")
    print("=" * 50)
    print("⚠️  注意: 此脚本需要配合 OpenClaw 或 Claude API 使用")
    print("=" * 50)
    print("""
请在 OpenClaw/Claude 中使用以下 Prompt:

帮我看看这个想法靠不靠谱：{idea}
""".format(idea=idea))

if __name__ == "__main__":
    main()
