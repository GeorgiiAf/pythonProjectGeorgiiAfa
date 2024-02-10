lentoasemat = {}   # sanakirja
def lisaa_lentoasema():
    icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao_koodi] = nimi      #   sanakirja  key : value
    print(f"Lentoasema {nimi} lisätty ICAO-koodilla {icao_koodi}")
def hae_lentoasema():
    icao_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ")
    nimi = lentoasemat.get(icao_koodi, "Lentoasemaa ei löytynyt.")  # get key
    print(f"Lentoaseman nimi: {nimi}")
while True:
    print("\nValitse toiminto:")
    print("1. Lisää uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valintasi (1/2/3): ")

    if valinta == "1":
        lisaa_lentoasema()
    elif valinta == "2":
        hae_lentoasema()
    elif valinta == "3":
        print("Ohjelma päättyy.")
        break
    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")
