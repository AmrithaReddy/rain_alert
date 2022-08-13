import requests
from twilio.rest import Client
params = {"appid": "911c9e3361424d9e1fe7ecbbd1742d62", "lat": 17.385044, "lon": 78.486671,
          "exclude": "current,minutely,daily"}
account_sid = "ACb70193764b1a3ce675fdee199cb8898f"
auth_token = "91ad3d6dbd7107454df212ea574bc663"
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params)
response.raise_for_status()
weather_data = response.json()
id_l = []
id_list = []
for i in range(0, 12):
    id_l.append([weather_data["hourly"][i]["weather"][0]["id"]])
for i in id_l:
    id_list.append(i[0])

will_rain = False
for idd in id_list:
    if idd < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's gonna rain today!Be sure to carry an umbrella ❤️🐥",
        from_='+19513275670',
        to='+918074175105'
    )
    print(message.status)




