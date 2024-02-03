import random
class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

        # kiihdytä-metodi
    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
            # kulje -metodi

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä

class kilpailu:
    """Luodaan  kilpailu class"""
    def __init__(self,kilpailun_nimi,pituus_km,autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot = autot
    # tunti_kuluu metodi

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)
    def tulosta_tilanne(self):
        print("\nKilpailun tilanne:")
        print("{:<15} {:<15} {:<20} {:<20} {:<20}".format("Rekisteri", "Nopeus (km/h)", "Kuljettu matka (km)",
                                                          "Huippunopeus (km/h)", "Maaliin"))
        print("-" * 90)

        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                maaliin = "Kyllä"
            else:
                maaliin = "Ei"
            print("{:<15} {:<15} {:<20} {:<20} {:<20}".format(auto.rekisteritunnus, auto.tämänhetkinen_nopeus,
                                                              auto.kuljettu_matka, auto.huippunopeus, maaliin))
        print("-" * 90)

        #    Tarkistetaan, onko auton kuljettu matka suurempi
        #    tai yhtä suuri kuin kilpailun kokonaiskilometrimäärä
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

autot_kilpailuun = [auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

kilpailu = kilpailu("Suuri romuralli", 8000, autot_kilpailuun)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

print('\nKilpailu on päättynyt')
kilpailu.tulosta_tilanne()
