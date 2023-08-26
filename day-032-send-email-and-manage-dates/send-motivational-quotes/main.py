# import smtplib
# import random
#
# # Referencing datetime as dt to avoid confusing between datetime module and datetime class.
# import datetime as dt

# my_email = "again.meowya@gmail.com"
# my_password = "iotmldmwjvxqvxgk"

# # We create an object(i.e., connection) of SMTP class.
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# # starttles() - Where tls is Transport Layer Security. This function ensures that the message you send is secure.
# # Even if the message gets intercepted it can't be read because it is encrypted.
# connection.starttls()
#
# # We log in to our e-mail account using the login() function.
# connection.login(user=my_email, password=my_password)
#
# # We send e-mail using the sendmail() function.
# connection.sendmail(from_addr=my_email, to_addrs="testing.meowya@gmail.com", msg="Subject:Birthday Wisher "
#                                                                                  "Testing\n\nTesting....Testing!!!")
#
# connection.close()

# OR

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="testing.meowya@gmail.com", msg="Subject:Birthday Wisher "
#                                                                                      "Testing\n\nTesting....Testing!!!")

#
# # We can call the now() function using the datetime class object. The now() function gives us the datetime for today.
# datetime_now = dt.datetime.now()
#
# # We can also get individual data like year, month, day, day of the week, etc.,
# year_now = datetime_now.year
# month_now = datetime_now.month
# day_now = datetime_now.day
# day_of_week = datetime_now.weekday()
# day_of_week = datetime_now.strftime('%A')
# print(day_of_week)

# We can also create a datetime object of our own.
# date_of_birth = dt.datetime(year=1997, month=3, day=30)
#
# print(date_of_birth)


import smtplib
import random
import datetime as dt

datetime_now = dt.datetime.now()
day_of_week = datetime_now.strftime('%A')

with open(file="quotes.txt", mode="r") as quotes_txt:
    all_quotes = quotes_txt.read()
    quotes_list = all_quotes.split("\n")

pick_a_quote = random.choice(quotes_list)

my_email = "again.meowya@gmail.com"
my_password = "iotmldmwjvxqvxgk"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if day_of_week == "Monday":
        connection.sendmail(from_addr=my_email, to_addrs="testing.meowya@gmail.com",
                            msg=f"Subject: Motivational Quotes "
                                f"on Demand. \n\n{pick_a_quote}")

