# Birthday wisher project
# My solution
import datetime as dt
import pandas
import smtplib
from random import choice

MY_EMAIL = "a.fatahu95@gmail.com"
MY_PASSWORD = "comb553gift343"

def send_email(email_address, message):
    """send birthday message to the email_address"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=message)
        connection.close()

letters = []
def get_random_letter(name):
    """selects a random letter and replaces the name in it and then returns it"""
    with open("letter_templates/letter_1.txt") as letter_file:
        letters.append(letter_file.read())

    with open("letter_templates/letter_2.txt") as letter_file:
        letters.append(letter_file.read())

    with open("letter_templates/letter_2.txt") as letter_file:
        letters.append(letter_file.read())
    # replace the
    random_letter = choice(letters).replace("[NAME]", name)
    return  random_letter


# get today's date
now = dt.datetime.now()
today_date = (now.day, now.month)

# get data from the birthday csv
birthdays_data = pandas.read_csv("birthdays.csv")
# get data into dictionary
birthdays_dict = {row.names : {"email": row.email, "year": row.year, "month":row.month, "day":row.day} for (index, row) in birthdays_data.iterrows()}

for name_ in birthdays_dict:
    friend_birthday = (birthdays_dict[name_]["day"], birthdays_dict[name_]["month"])
    # search if someone's birthday is today, then send the person a mail
    if friend_birthday == today_date:
        email_ = birthdays_dict[name_]["email"]
        send_email(email_, get_random_letter(name_))