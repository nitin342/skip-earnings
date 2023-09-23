import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

user_token = os.getenv("USER_TOKEN")
app_token = os.getenv("APP_TOKEN")
user_id = os.getenv("USER_ID")

def format_price(price):
    return format(price / 100, '.02f')

headers = {"user-token": user_token, "app-token": app_token}

response = requests.get(f"https://api-courier.skipthedishes.com/v4/couriers/{user_id}/statements", headers=headers)
statements = response.json()["statements"]

print("{} {:>20} {:>20} {:>20}".format("Statement Date", "Total", "Tips", "Total - Tip"))
totalEarningsWithoutTip = 0
totalEarningsWithTip = 0

for statement in statements:
    if statement["netAmount"] > 0:
        stmtId = statement["statementId"]
        timeInMS = statement['periodEnd']
        date = datetime.datetime.fromtimestamp(timeInMS/1000.0)
        if date > datetime.datetime(2022,1,1) and date < datetime.datetime(2023,1,1):
            stmtRes = requests.get(f"https://api-courier.skipthedishes.com/v2/couriers/{user_id}/statements/{stmtId}", headers=headers)
            details = stmtRes.json()
            orders = details['orders']
            totalEarnings = statement["totalEarnings"]
            tips = sum(item[0]['tip'] for item in orders)
            earningsWithoutTip = totalEarnings - tips
            totalEarningsWithoutTip = totalEarningsWithoutTip + earningsWithoutTip
            totalEarningsWithTip = totalEarningsWithTip + totalEarnings
            print(f"{date.date()} {format_price(totalEarnings) :>20} {format_price(tips) :>20} {format_price(earningsWithoutTip) :>20}")

print(f"Total Earnings without Tip: {format_price(totalEarningsWithoutTip)}")
print(f"Total Earnings with Tip: {format_price(totalEarningsWithTip)}")
