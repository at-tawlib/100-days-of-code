# Day 32 sending emails
# import smtplib
#
# my_email = "a.fatahu95@gmail.com"
# password = "adafa"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="dealrega@yahoo.com", msg="Hello")
#     connection.close()

# Datetime
import datetime as dt
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(f"now: {now}, year: {year}, month: {month}, day: {day_of_week}")

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)