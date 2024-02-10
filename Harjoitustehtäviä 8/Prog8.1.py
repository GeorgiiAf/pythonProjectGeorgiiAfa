import mysql.connector
def search_airport(ident):
    sql = 'SELECT name, municipality FROM airport WHERE ident = %s'
    kursori = yhteys.cursor()
    kursori.execute(sql, (ident,))      # tuple
    tulos = kursori.fetchone()
    return tulos

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True)

ident = input('Korjoita ICAO-koodi : ')         # example 0FL1 ,  00A
airport_data = search_airport(ident)
if airport_data:
    name, municipality = airport_data
    print(f"Lentokenttä: {name}\nSijaintikunta: {municipality}")
else:
    print("Lentokenttätietoja ei löytynyt annetulla ICAO-koodilla.")
