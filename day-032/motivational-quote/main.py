# send motivational quotes to a user on mondays
import datetime as dt
import random
import smtplib

# get today and check if it is monday to send the quote
now = dt.datetime.now()
weekday = now.weekday()
# check if today is monday then send the mail
if weekday == 0:
    # read data from quotes
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = random.choice(quotes)

    my_email = "a.fatahu95@gmail.com"
    password = "adafa"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dealrega@yahoo.com",
            msg=f"Subject: Monday Motivation\n\n{random_quote}")
        connection.close()
