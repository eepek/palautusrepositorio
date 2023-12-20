from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        super().pelaa()

    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
