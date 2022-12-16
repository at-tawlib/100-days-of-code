# Birthday wisher project: Normal Mode
from datetime import datetime
import random
import smtplib
import pandas

MY_EMAIL = "a.fatahu95@gmail.com"
MY_PASSWORD = "comb553gift343"

# get current date
now = datetime.now()
today = (now.month, now.day)
# read csv with pandas
data = pandas.read_csv("birthdays.csv")
# create dictionary from the csv
birthdays_dict = {(row.month, row.day): row for (index, row)  in data.iterrows()}
# check if today's date exists in the birthday dict
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    # get random letter from the 3 letters
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # open file and replace name with person's name
    with open(file_path) as letter_file:
        contents = letter_file.read()
        send_letter = contents.replace("[NAME]", birthday_person["names"])

    # send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
