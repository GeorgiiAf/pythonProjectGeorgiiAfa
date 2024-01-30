class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
        # kiihdytä-metodi,
    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

uusi_auto = auto(" ABC-123", 142)
uusi_auto.kiihdytä(30)
print("Auton nopeus:", uusi_auto.tämänhetkinen_nopeus, "km/h")
uusi_auto.kiihdytä(70)
print("Auton nopeus:", uusi_auto.tämänhetkinen_nopeus, "km/h")
uusi_auto.kiihdytä(50)
print("Auton nopeus:", uusi_auto.tämänhetkinen_nopeus, "km/h")
uusi_auto.kiihdytä(-200)
print("Auton nopeus:", uusi_auto.tämänhetkinen_nopeus, "km/h")

print(f"Uuden auton rekisteritunnus : {uusi_auto.rekisteritunnus} huippunopeus km/h : {uusi_auto.huippunopeus} km/h"
      f" tämänhetkinen_nopeus : {uusi_auto.tämänhetkinen_nopeus} km/h  kuljettu_matka : {uusi_auto.kuljettu_matka} km/h")
