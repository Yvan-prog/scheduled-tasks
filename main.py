import os
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

LATITUDE = "49.811253"
LONGITUDE = "4.869699"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()



will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It's going to rain today.",
        from_='+18145594893',
        to='+32477181404'
    )
    print(message.status)
else :
    client = Client(account_sid, auth_token)
    message = client.messages .create(body="It's not going to rain today.",from_='+18145594893',to='+32477181404')

