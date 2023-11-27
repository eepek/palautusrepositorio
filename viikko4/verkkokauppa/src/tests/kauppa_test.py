import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa

from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 13

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 42:
                return 5
            elif tuote_id == 2:
                return 10
            elif tuote_id == 6:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 42:
                return Tuote(42, "mehu", 7)
            elif tuote_id == 2:
                return Tuote(2, "limu", 4)
            elif tuote_id == 6:
                return Tuote(6, "banaani", 1)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan self.kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock,
                        viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pökkä", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pökkä", 13, "54321", ANY, 7)

    def test_kahden_eri_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pökkä", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pökkä", 13, "54321", ANY, 11)

    def test_kahden_saman_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pökkä", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pökkä", 13, "54321", ANY, 8)

    def test_kahden_tuotteen_joista_toinen_loppu_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(6)
        self.kauppa.tilimaksu("pökkä", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pökkä", 13, "54321", ANY, 7)

    def test_aloita_asiointi_nollaa_ostoskorin(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pökkä", "54321")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pökkä", 13, "54321", ANY, 7)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):

        self.viitegeneraattori_mock.uusi.side_effect = [6, 7, 8]

        def asioi():
            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(42)
            self.kauppa.tilimaksu("pökkä", "54321")

        asioi()

        self.pankki_mock.tilisiirto.assert_called_with(
            ANY, 6, ANY, ANY, ANY)

        asioi()

        self.pankki_mock.tilisiirto.assert_called_with(
            ANY, 7, ANY, ANY, ANY)

        asioi()

        self.pankki_mock.tilisiirto.assert_called_with(
            ANY, 8, ANY, ANY, ANY)

    def test_tuotteen_poisto_lisaa_varasto_saldoa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.poista_korista(42)
        self.varasto_mock.palauta_varastoon.assert_called_with(
            Tuote(42, "mehu", 7))

    def test_tuotteen_poisto_poistaa_tuotteen_ostoskorista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(42)
        self.kauppa.tilimaksu("pökkä", "54321")
        self.pankki_mock.tilisiirto.assert_called_with(
            ANY, ANY, ANY, ANY, 4)
