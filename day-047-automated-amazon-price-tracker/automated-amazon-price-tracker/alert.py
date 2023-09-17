import smtplib
import os

# MY_EMAIL and MY_PASSWORD stored as environment variable.
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class Alert:

    def __init__(self, product_data):
        """Creates an object of Alert class. Sends an email."""
        with smtplib.SMTP("smtp.gmail.com", port=587) as alert_connect:
            alert_connect.starttls()
            alert_connect.login(user=MY_EMAIL, password=MY_PASSWORD)
            alert_connect.sendmail(from_addr=MY_EMAIL,
                                   to_addrs="testing.meowya@gmail.com",
                                   msg=f"Subject:Amazon Price Alert!\n\n{product_data['name']} "
                                       f"is now ${product_data['price']}.\n"
                                       f"{product_data['url']}".encode("utf-8")
                                   )
