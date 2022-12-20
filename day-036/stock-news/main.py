import requests

STOCK_API_KEY = "62NORLW171QQDJ6W"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "e4edab13198f48228640fea1f691e403"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"] # get only the daily series from json
# get the data from the dictionary into a list of the values
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]   # yesterday will be at position 0
# Get yesterday's closing stock price
yesterday_closing_price = float(yesterday_data["4. close"])
print(f"Yesterdays closing price: {yesterday_closing_price}")

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]  # the data will be at position 1
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(f"Day before yesterday closing price: {day_before_yesterday_closing_price}")

# Find the positive difference between yesterday and day before yesterday
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None  # holds emoji for increment or decrement
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(f"Positive difference: {difference}")
# percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = (difference / yesterday_closing_price) * 100
print(f"Percentage diff: {percentage}")


# If percentage(positive) is greater than 5 then use the News API to get the first articles related to Tesla
# set the value to 0.00 instead of 5.00 to test if there is news
if abs(percentage) > 0.00:
    # get news from the News API
    news_parameters = {
        "q": "tesla",
        "from": "2022-12-09",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    articles = response.json()["articles"]  # get the articles which is a list
    three_articles = articles[:3]   # get first 3 articles

    # TODO: send the articles to file output instead of using Twillio
    formatted_articles = [f"{STOCK_NAME}: {up_down}\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        print()
        print(article)
else:
    print("no news")