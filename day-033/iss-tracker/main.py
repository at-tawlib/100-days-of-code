import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "a.fatahu95@gmail.com"
MY_PASSWORD = "abadanoaid"
# latitude and longitude got from latlong.net
MY_LAT = 7.946527
MY_LONG = -1.023194

def is_iss_overhead():
    """Returns true if iss is within my location"""
    # get the ISS position from the API
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    # get the latitude and longitude from the iss
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # your position is within +5 or -5 degrees to the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True;

def is_night():
    """return True if it is nigh time at my position"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # get sunset and sunrise times using the API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # get the sunrise time => split it => get time list [1] => split it and get the hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # get the current hour
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True;

# if the ISS is close to my current position, and it is currently dark
# Then email me to tell me to look up.
while True:
    time.sleep(60)
    # wait for 60 seconds
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up\n\nThe ISS is above you in the sty."
        )
        connection.close()