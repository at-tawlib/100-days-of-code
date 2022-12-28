# 28-12-22 A bot which sends a complaint on twitter

from internet_speed_twitter_bot import InternetSpeedTwitterBot

# ISP's guaranteed internet speeds
PROMISED_DOWN = 150
PROMISED_UP = 10

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()