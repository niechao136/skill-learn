---
name: currency-hedging
description: 当用户询问不同货币之间的换算，特别是涉及大额交易的对冲成本（Hedging Cost）计算时，激活此技能。
---

# 货币对冲计算专家

## 激活场景
用户提到类似：“100万美金换成人民币是多少？考虑到 2% 的对冲成本，我最后能拿多少？”

## 执行逻辑
1. **参数提取**：从用户输入中提取 `amount` (金额), `from_cur` (原货币), `to_cur` (目标货币)。
2. **脚本调用**：必须通过运行 `scripts/calculate_fx.py` 来获取精确计算结果。
    - 命令格式：`python3 scripts/calculate_fx.py [amount] [from_cur] [to_cur]`
3. **输出规范**：
    - 必须先列出当前的“模拟汇率”。
    - 必须明确指出“扣除对冲成本后”的最终金额。

## 参数提取准则 (Strict Extraction)
- **Amount**: 必须是纯数字。如果用户说“几十万”，请追问具体数值，严禁盲目填充 500,000。
- **Currency Code**: 必须使用标准 ISO 三位代码（如 USD, CNY, EUR）。
- **兜底逻辑**：如果用户提到的货币不在 [USD, CNY, EUR, JPY] 范围内，不要调用脚本，直接回复：“抱歉，我目前仅支持美、中、欧、日货币的对冲计算。”
