import mysql.connector
from geopy.distance import geodesic


def search_airport(ident):
    sql = 'SELECT name,latitude_deg,longitude_deg FROM airport WHERE ident = %s'
    kursori = yhteys.cursor()
    kursori.execute(sql, (ident,))
    tulos = kursori.fetchone()
    return tulos


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True)

ident1 = input('Kirjoita ensimmäisen lentokentän ICAO-koodi: ')    # for example 0FL1 ,  00A
airport_data1 = search_airport(ident1)
if airport_data1:
    name, latitude, longitude = airport_data1
    paikka1 = (latitude, longitude)

    ident2 = input('Kirjoita toisen lentokentän ICAO-koodi: ')
    airport_data2 = search_airport(ident2)
    if airport_data2:
        name, latitude, longitude = airport_data2
        paikka2 = (latitude, longitude)

        etäisyys = geodesic(paikka1, paikka2).kilometers  # etäisyys kilometreinä
        print(f"Etäisyys paikan 1 ja paikan 2 välillä: {etäisyys} kilometriä")
    else:
        print(f"Lentokenttää {ident2} ei löydy tietokannasta.")
else:
    print(f"Lentokenttää {ident1} ei löydy tietokannasta.")
