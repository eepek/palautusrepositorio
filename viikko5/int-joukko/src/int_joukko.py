KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is not None and kasvatuskoko is not None:
            if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
                raise Exception(
                    "Kapasiteetin täytyy olla positiivinen kokonaisluku")

        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        self.listajono = self._luo_lista(self.kapasiteetti)

        self.listan_pituus = 0

    def kuuluu(self, lisattava_luku):
        on = 0

        for luku in self.listajono:
            if luku == lisattava_luku:
                return True
            else:
                continue

        return False

    def lisaa(self, lisattava_luku):
        if self.listan_pituus == 0:
            self.listajono[0] = lisattava_luku
            self.listan_pituus = self.listan_pituus + 1
            return True
        else:
            pass

        if not self.kuuluu(lisattava_luku):
            self.listajono[self.listan_pituus] = lisattava_luku
            self.listan_pituus = self.listan_pituus + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.listan_pituus % len(self.listajono) == 0:
                taulukko_old = self.listajono
                self.kopioi_lista(self.listajono, taulukko_old)
                self.listajono = self._luo_lista(
                    self.listan_pituus + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.listajono)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.listan_pituus):
            if n == self.listajono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.listajono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.listan_pituus - 1):
                apu = self.listajono[j]
                self.listajono[j] = self.listajono[j + 1]
                self.listajono[j + 1] = apu

            self.listan_pituus = self.listan_pituus - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.listan_pituus

    def to_int_list(self):
        taulu = self._luo_lista(self.listan_pituus)

        for i in range(0, len(taulu)):
            taulu[i] = self.listajono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.listan_pituus == 0:
            return "{}"
        elif self.listan_pituus == 1:
            return "{" + str(self.listajono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.listan_pituus - 1):
                tuotos = tuotos + str(self.listajono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.listajono[self.listan_pituus - 1])
            tuotos = tuotos + "}"
            return tuotos
