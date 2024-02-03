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
    def tulosta_tilanne(self):
        print("{:<15} {:<15} {:<20}".format(self.rekisteritunnus, self.tämänhetkinen_nopeus,
                                            self.kuljettu_matka))

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus , akkukapasiteetti ):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def lataa_akku(self, lisäkapasiteetti):
        self.akkukapasiteetti += lisäkapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bens_koko):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bens_koko  = bens_koko
    def tankkaa_bensa(self, lisää_bensaa):
        self.bens_koko += lisää_bensaa

# pääohjelma
S_auto = Sähköauto(" ABC-15", 180, 52.5)
P_auto = Polttomoottoriauto(" ACD-123", 165, 32.3)


S_auto.kiihdytä(50)
P_auto.kiihdytä(40)

# Ajetaan autoja kolmen tunnin verran
for tunti in range(3):
    S_auto.kulje(1)
    P_auto.kulje(1)

# Tulostetaan matkamittarilukemat
print("\nSähköauto:")
S_auto.tulosta_tilanne()

print("\nPolttomoottoriauto:")
P_auto.tulosta_tilanne()