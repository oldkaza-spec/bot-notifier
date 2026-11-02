import os, requests
TOKEN_M7M7 = os.getenv("TOKEN_M7M7")
TOKEN_PENNY = os.getenv("TOKEN_PENNY")
CHAT_ID = os.getenv("CHAT_ID")

def send(token, text):
    if not token: return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": True})

msg = """⚠️ *فحص فوري - تاسي*

السوق الآن: تاسي
الإغلاق 9882 +0.45%
لا يوجد سهم يحقق كامل شروط WWW الآن
الأقرب: سيسكو 2190 - ضمن 1.8% من EMA21
[TradingView](https://www.tradingview.com/chart/?symbol=TADAWUL%3A2190)"""

send(TOKEN_M7M7, msg)
send(TOKEN_PENNY, msg)
print("Sent!")
