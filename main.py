import requests
import os 
from twilio.rest import Client

PARALLUVIALAT=-37.472287
PARALLUVIALON=-72.353410
MY_LAT = -33.512917
MY_LON = -70.678255
API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT ="https://api.openweathermap.org/data/2.5/forecast?"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters= {
    "lat":MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "lang": "es",
    "cnt": 4,
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather = weather_data['list'][0]["weather"][0]["id"]
will_rain = False

for x in range(len(weather_data['list'])):
    clima_id = int(weather_data['list'][x]['weather'][0]['id'])
    clima = weather_data['list'][x]['weather'][0]["description"]
    if clima_id <= 701:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Va a llover hoy. Recuerda llevar paraguas ☂️",
        from_= "+16616056925",
        to="+56 9 9493 3022",
    )
    print(message.status)
