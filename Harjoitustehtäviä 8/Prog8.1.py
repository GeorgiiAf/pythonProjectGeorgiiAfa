import mysql.connector
def hhh(icaokoodi):
    sql = f'SELECT airport.ident FROM airport'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f' Olen  {rivi[1]}')



yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
autocommit = True)

icaokoodi = input('Korjoita koodi : ')
hhh(icaokoodi)