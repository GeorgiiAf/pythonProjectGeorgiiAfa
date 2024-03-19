class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto  = Auto(" ABC-123", 142)
print(f"Uuden auton rekisteritunnus : {uusi_auto.rekisteritunnus} huippunopeus km/h : {uusi_auto.huippunopeus} km/h"
      f" tämänhetkinen_nopeus : {uusi_auto.tämänhetkinen_nopeus} km/h  kuljettu_matka : {uusi_auto.kuljettu_matka} km/h")
