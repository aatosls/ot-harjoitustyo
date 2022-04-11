import unittest
from services.kare_service import KareService

class TestKareService(unittest.TestCase):
    def setUp(self):
        self.kare_service = KareService()

    def test_soundfile_import(self):
        self.kare_service.import_soundfile(["./kare/src/tests/hello.wav"])
        list = self.kare_service.get_sound_object_names()
        self.assertEqual(list, ["hello"])