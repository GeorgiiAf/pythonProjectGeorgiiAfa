class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.kerrokset = list(range(alin_kerros, ylin_kerros + 1))

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros != kohde_kerros:
            if self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
            elif self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < max(self.kerrokset):
            self.nykyinen_kerros += 1
        self.ilmoita_kerros()

    def kerros_alas(self):
        if self.nykyinen_kerros > min(self.kerrokset):
            self.nykyinen_kerros -= 1
        self.ilmoita_kerros()

    def ilmoita_kerros(self):
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            hissi = self.hissit[hissi_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Invalidi hissin numero.")

# Pääohjelma
talo = Talo(1, 10, 2)  # Luodaan talo, jossa on kaksi hissiä

# Ajaminen hissillä 0 kerrokseen 5
talo.aja_hissiä(0, 5)

# Ajaminen hissillä 1 kerrokseen 8
talo.aja_hissiä(1, 8)
