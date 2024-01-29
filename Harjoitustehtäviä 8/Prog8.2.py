import mysql.connector
def search_airport_type_amount(iso_country):
    sql = 'SELECT type, COUNT(*) as amount FROM airport WHERE iso_country = %s GROUP BY type'
    kursori = yhteys.cursor()
    kursori.execute(sql, (iso_country,))
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True)

iso_country = input('Korjoita maakoodi : ')         # for example FI  or US
airport_data = search_airport_type_amount(iso_country)
if airport_data:
    for tyyppi, maara in airport_data:
        print(f"Lentokenttiä tyypissä {tyyppi}: {maara} kpl")
else:
    print("Lentokenttätietoja ei löytynyt annetulla maakoodilla.")
