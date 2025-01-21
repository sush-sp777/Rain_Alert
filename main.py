import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="44bc06d03efcf4141ad71dff2b7e7360"
account_sid = '__YOUR_TWILIO_ACCOUNT_ID__'
auth_token = '__YOUR_TWILIO_AUTH_TOKEN__'

Weather_params={
    "lat":18.516726,
    "lon":73.856255,
    "appid":api_key,
    "cnt":4
}

response=requests.get(OWM_Endpoint,params=Weather_params)
weather_data=response.json()

will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's Rain Today. Remember To bring an umbrella ☔️",
    from_="YOUR TWILIO VIRTUAL NUMBER",
    to='YOUR TWILIO VERIFIED REAL NUMBER'
    )
    print(message.status)
