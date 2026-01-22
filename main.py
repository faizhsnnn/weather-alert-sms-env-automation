import os
import requests
from twilio.rest import Client

OWN_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("TOKEN")

weather_params={
    "lat":26.2000,
    "lon":163.1833,
    "appid":api_key,
    "cnt":4
}
response=requests.get(OWN_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=os.environ.get("TWILIO_NUM"),
        to=os.environ.get("MY_PHONE")
    )
    print(message.status)




