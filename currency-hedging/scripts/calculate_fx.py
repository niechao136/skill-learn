import sys
import json

# 增加支持列表
SUPPORTED_CURRENCIES = ["USD", "CNY", "EUR", "JPY"]

def get_exchange_rate(from_cur, to_cur):
    # 模拟 2026 年的固定汇率
    rates = {
        ("USD", "CNY"): 7.25,
        ("EUR", "USD"): 1.08,
        ("JPY", "CNY"): 0.048
    }
    return rates.get((from_cur, to_cur), 1.0)

def main():
    if len(sys.argv) < 4:
        print(json.dumps({"error": "Missing arguments"}))
        return

    amount = float(sys.argv[1])
    from_cur = sys.argv[2].upper()
    to_cur = sys.argv[3].upper()

    if from_cur not in SUPPORTED_CURRENCIES or to_cur not in SUPPORTED_CURRENCIES:
        # 返回结构化的错误信息，让 Agent 能看懂
        print(json.dumps({
            "error": "UNSUPPORTED_CURRENCY",
            "message": f"目前不支持 {from_cur} 到 {to_cur} 的转换",
            "supported": SUPPORTED_CURRENCIES
        }))
        return

    rate = get_exchange_rate(from_cur, to_cur)
    base_total = amount * rate
    hedge_cost = base_total * 0.02  # 固定的 2% 对冲成本
    final_amount = base_total - hedge_cost

    result = {
        "original_amount": amount,
        "rate": rate,
        "base_total": round(base_total, 2),
        "hedge_cost": round(hedge_cost, 2),
        "final_amount": round(final_amount, 2),
        "currency": to_cur
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
