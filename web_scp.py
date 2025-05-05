import requests
import openpyxl
import time
from datetime import datetime

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Crypto Prices"
sheet.append(["Vaxt", "BNB/USDT", "SOL/USDT", "ADA/USDT"])

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

try:
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bnb = get_price("BNBUSDT")
        sol = get_price("SOLUSDT")
        ada = get_price("ADAUSDT")

        print(f"[{now}] Qiymətlər: BNB: {bnb}, SOL: {sol}, ADA: {ada}")
        
        sheet.append([now, bnb, sol, ada])
        workbook.save("crypto_prices.xlsx")
        time.sleep(600)

except KeyboardInterrupt:
    print("Dayandırıldı. Excel faylı saxlanıldı.")
    workbook.save("crypto_prices.xlsx")
