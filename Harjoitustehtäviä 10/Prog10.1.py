class hissi:
    """Luodaan luokka hissi"""
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
        """hissi ajaa  yhden kerroksen ylöspäin"""
        if self.nykyinen_kerros < max(self.kerrokset):
            self.nykyinen_kerros += 1
        self.ilmoita_kerros()

    def kerros_alas(self):
        """hissi ajaa  yhden kerroksen alaspäin"""
        if self.nykyinen_kerros > min(self.kerrokset):
            self.nykyinen_kerros -= 1
        self.ilmoita_kerros()

    def ilmoita_kerros(self):
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

h = hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(6)   # 1 , 2 ,3  ....
