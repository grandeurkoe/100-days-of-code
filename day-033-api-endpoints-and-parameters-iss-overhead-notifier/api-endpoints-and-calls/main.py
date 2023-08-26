# 'requests' package enables us to make API requests
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "again.meowya@gmail.com"
MY_PASSWORD = "iotmldmwjvxqvxgk"
MY_LAT = 19.182516
MY_LNG = 73.192604


def is_close():
    global MY_LNG, MY_LAT
    # Request the location of the ISS from the ISS API using the request.get() function.
    # Returns a response code on execution.
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Raises an HTTP Error if the request fails.
    iss_response.raise_for_status()

    # The response.json() function allows us to fetch the json data from the ISS API response.
    iss_data = iss_response.json()

    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])

    if MY_LNG - 5 <= iss_longitude <= MY_LNG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    # Create parameters for Sunset and sunrise times API.
    parameter = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)

    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split('+')[0].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split('+')[0].split(':')[0])

    date_time_now = datetime.now()
    time_hour_now = date_time_now.hour

    if time_hour_now >= sunset or time_hour_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_night() and is_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as iss_connection:
            iss_connection.starttls()
            iss_connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            iss_connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="testing.meowya@gmail.com",
                                    msg="Subject: Look Up!\n\nThe ISS is above you in the sky.",
                                    )
