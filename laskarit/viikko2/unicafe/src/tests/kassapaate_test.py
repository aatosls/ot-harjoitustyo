import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateismaksu_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)

    def test_edullisen_kateismaksun_vaihtoraha(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtorahat, 60)

    def test_maukas_kateismaksu_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)

    def test_maukkaan_kateismaksun_vaihtoraha(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtorahat, 100)

    def test_edullinen_kateismaksu_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateismaksu_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_osto_jos_raha_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtorahat, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_osto_jos_raha_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtorahat, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_kortilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo, 500-240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_osto_kortilla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo, 500-400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_osto_kortilla_kun_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_maukkaan_osto_kortilla_kun_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kortin_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+1000)

    def test_kortin_lataus_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.maksukortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)