from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)
        super().pelaa()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
