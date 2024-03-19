import random
class Auto:
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
autot = []
for i in range(1, 11):
    rekisteritunnus = f" ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

for auto_obj in autot:  # auto_obj , koska luokan nimi on Auto tehdään auto_obj konfliktin välttämiseksi
    nopeuden_muutos = random.randint(-10, 15)
    auto_obj.kiihdytä(nopeuden_muutos)
    auto_obj.kulje(1)
    if auto_obj.kuljettu_matka >= 10000:
        break

        # taulukko
print("\nLopulliset tulokset:\n")
print("{:<15} {:<15} {:<20} {:<20}".format("Rekisteri", "Nopeus (km/h)", "Kuljettu matka (km)", "Huippunopeus (km/h) "))
print("-" * 70)

for auto_obj in autot:
    print("{:<15} {:<15} {:<20} {:<20}".format(auto_obj.rekisteritunnus, auto_obj.tämänhetkinen_nopeus, auto_obj.kuljettu_matka , auto_obj.huippunopeus))
