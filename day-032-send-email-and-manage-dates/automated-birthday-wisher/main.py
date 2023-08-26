import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "again.meowya@gmail.com"
MY_PASSWORD = "iotmldmwjvxqvxgk"

today_datetime = dt.datetime.now()
today_month = today_datetime.month
today_day = today_datetime.day
today_date = (today_month, today_day)

birthdays_data = pandas.read_csv(filepath_or_buffer="birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays_data.iterrows()}

if today_date in birthdays_dict:
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter_data_read:
        letter_body = letter_data_read.read()
        letter_body = letter_body.replace("[NAME]", birthdays_dict[today_date]["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as wisher_connection:
        wisher_connection.starttls()
        wisher_connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        wisher_connection.sendmail(from_addr=MY_EMAIL,
                                   to_addrs=birthdays_dict[today_date]["email"],
                                   msg=f"Subject:Happy Birthday!\n\n{letter_body}")
