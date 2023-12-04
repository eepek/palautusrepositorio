from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._muisti = [0]

        self.komennot = {Komento.SUMMA: Summa(self._sovellus, self.lue_syote),
                         Komento.EROTUS: Erotus(self._sovellus, self.lue_syote),
                         Komento.NOLLAUS: Nollaa(self._sovellus),
                         Komento.KUMOA: Kumoa(self._sovellus, self._muisti)}

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovellus.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(
            columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except Exception:
            pass

    def _suorita_komento(self, komento):

        komento_olio = self.komennot[komento]

        arvo = komento_olio.suorita()

        if arvo is not None:
            self._muisti.append(arvo)

        print(self._muisti)

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovellus.arvo())


class Summa:
    def __init__(self, sovellus, io) -> None:
        self._sovellus = sovellus
        self.io = io

    def suorita(self):
        syote = self.io()
        self._sovellus.plus(syote)
        return self._sovellus.arvo()


class Erotus:
    def __init__(self, sovellus, io) -> None:
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        self.syote = self._io()
        self._sovellus.miinus(self.syote)
        return self._sovellus.arvo()


class Nollaa:
    def __init__(self, sovellus) -> None:
        self._sovellus = sovellus

    def suorita(self):
        self._sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus, muisti: list) -> None:
        self._sovellus = sovellus
        self.muisti = muisti

    def suorita(self):
        print(self.muisti)
        if len(self.muisti) > 1:
            self.muisti = self.muisti[0: -1]
        self._sovellus.aseta_arvo(self.muisti[-1])
