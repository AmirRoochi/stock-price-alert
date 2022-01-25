STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "3PRSWYI8VX57YHM2"
import requests
import datetime
from datetime import timedelta

# current_time = datetime.datetime.now()
# yesterday_date = current_time - timedelta(days=1)
# db_yesterday = yesterday_date - timedelta(days=1)
# print(yesterday_date.date())
# print(db_yesterday.date())

parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": API_KEY,
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_response.raise_for_status()
data = stock_response.json()
time_series = data["Time Series (Daily)"]
print(time_series)
yesterday = list(data["Time Series (Daily)"])[0]
db_yesterday = list(data["Time Series (Daily)"])[1]

y_price = float(time_series[yesterday]['4. close'])
dby_price = float(time_series[db_yesterday]['4. close'])
price_difference = y_price - dby_price
# stock_stat = ""
# if price_difference >= 0:
#     stock_stat = "increase"
# else:
#     stock_stat = "decrease"

percentage = price_difference / y_price * 100

if 5 >= percentage <= -5:
    print(f"get news {percentage}")

news_parameters = {
        "apikey": "1121698c6e3648b2865718764631804a",
        "q": COMPANY_NAME
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)
news_1_title = news_data["articles"][0]["title"]
news_1_desc = news_data["articles"][0]["description"]
news_1_url = news_data["articles"][0]["url"]




