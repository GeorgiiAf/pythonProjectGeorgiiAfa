import json
import requests

#  API KEY 468c0b3f70b49c1ba5d2c17702056ff3
#   funktio
# Espoo     lat': 60.2047672, 'lon': 24.6568435
def säätiedot(lat,lon):
    exclude_parts = 'minutely,current,alerts'
    säätiedot_linkki = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude_parts}&appid=ea160710d29362e47dabb6650ab0a046"
    weather_response = requests.get(säätiedot_linkki)
    weather_data = weather_response.json()
    return weather_data

#   pääohjelma
name = input('Kirjoita paikkakunnan nimi    :')
sijainnin_koordinaatit = f'http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid=ea160710d29362e47dabb6650ab0a046'
#
response = requests.get(sijainnin_koordinaatit)
sijainnin_data = response.json()
print(sijainnin_data)

try:
    if sijainnin_data:
        lat = sijainnin_data[0]['lat']
        lon = sijainnin_data[0]['lon']
        weather_data_final = säätiedot(lat,lon)

    # tulostaa paikkakunnan nimi ,  säätiedot ,  lämpötilä Kelvineina
        print("\nSäätiedot paikkakunnalle", name)
        print("----------------------------")
        print("Current weather:", weather_data_final['current']['weather'][0]['description'])
        print("Temperature:", weather_data_final['current']['temp'], "K")
    else:
        print("Paikkakuntaa ei löytynyt. Tarkista oikeinkirjoitus ja yritä uudelleen.")
except KeyError:
    print("Virhe: Sijaintitietoja ei löydy vastauksesta.")
#  API KEY 468c0b3f70b49c1ba5d2c17702056ff3
