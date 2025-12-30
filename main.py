# HTTP running on port -> 80
# HTTPS running on port -> 443
# API -> Application Programming Interface
#                 mode=""
# "a" = If the file exists, the handle is placed at the end of the file. If the file doesn't exist, it creates a new one.
# "w" = Opens the file for writing.
# "r" = Opens the file for reading.

from countryinfo import CountryInfo
from pprint import pprint
import json


# country_data = []
# while True:
#     country_name = input("Enter country name (eng): ").lower()
#     if country_name == "stop":
#         print("Program stopped")
#         with open('country_data.json', 'w', encoding='utf-8') as f:
#             json.dump(country_data, f, indent=4, ensure_ascii=False)
#             break
#     try:
#         get_country = CountryInfo(country_name)
#         data = get_country.info()
#         # data_2 = get_country.area()
#         # pprint(data)
#
#         Name = data["name"]
#         Capital = data["capital"]
#         Capital_latlng = data["capital_latlng"]
#         Currencies = data["currencies"]
#         CallingCodes = data["callingCodes"]
#         Languages = data["languages"]
#         Area = data["area"]
#         Population = data["population"]
#         Borders = data["borders"]
#         Provinces = data["provinces"]
#         Region = data["region"]
#         Timezones = data["timezones"]
#         Wiki = data["wiki"]
#
# #         print(f"""Name: {Name}
# # Capital: {Capital}
# # Capital Latlng: {Capital_latlng}
# # Currencies: {Currencies}
# # Area: {Area}
# # Population: {Population}
# # Borders: {Borders}
# # Provinces: {Provinces}
# # Timezones: {Timezones}
# # Wikipedia: {Wiki}""")
#
#         country_data.append({
#             'Name': Name,
#             'Capital': Capital,
#             'Capital_latlng': Capital_latlng,
#             'Currencies': Currencies,
#             'Languages': Languages,
#             'Area': Area,
#             'Population': Population,
#             'Borders': Borders,
#             'Provinces': Provinces,
#             'Timezones': Timezones,
#             'Wikipedia': Wiki
#         })
#         pprint(country_data)
#
#     except Exception as e:
#         print(e)
#         print("--> Error <--")


import requests

API = "Your API Key"

parameters = {
    "appid": API,
    "units": "metric",
    "lang": "en"
}

while True:
    city_name = input("Enter city name: ").lower()

    try:
        parameters["q"] = city_name
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                                params=parameters).json()
        # print(response)
        name = response["name"]
        description = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        wind_speed = response["wind"]["speed"]

        print(f"""In {name} temperature is {temp}
{description}
Wind speed: {wind_speed}""")

    except Exception as e:
        print(e)