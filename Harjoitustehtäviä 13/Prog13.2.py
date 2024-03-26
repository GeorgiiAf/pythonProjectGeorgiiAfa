from flask import Flask, request , jsonify
app = Flask(__name__)
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True)

def search_airport(ident):
    sql = 'SELECT name, municipality FROM airport WHERE ident = %s'
    kursori = yhteys.cursor()
    kursori.execute(sql, (ident,))
    tulos = kursori.fetchone()
    return tulos


"""  esimerkiksi  http://127.0.0.1:3000/kentt%C3%A4?ICAO=EFHK 
    http://127.0.0.1:3000/kentt%C3%A4?ICAO=SDRS     """

@app.route('/kenttä')
def ICAO_KOODI_LENTOKENTTÄ():
    icao = request.args.get("ICAO")

    if icao is None:
        return "ICAO not defined", 400  # Palautetaan virhekoodi 400

    airport_data = search_airport(icao)
    if airport_data:
        name, municipality = airport_data
        return jsonify({"ICAO": icao, "Name": name, "Municipality": municipality})
    else:
        return 'Error: Lentokenttää ei löydy', 404  # Palautetaan virhekoodi 404, jos lentokenttää ei löydy

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)