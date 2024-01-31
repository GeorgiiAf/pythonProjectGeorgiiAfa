class Talo:
    def __init__(self, alin_kerros, ylin_kerros, h_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.h_lkm = []

    def aja_hissiä(self, h_n, kohde_kerros):
        for i in range(h_n):
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

t = Talo(1,10,3)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(6)  # 1 , 2 ,3  ....
