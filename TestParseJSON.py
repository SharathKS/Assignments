from unittest import TestCase
from PyCodeChallenge import ParseJSON


class TestParseJSON(TestCase):
    def setUp(self):
        self.parse_json_obj = ParseJSON()

    def test_parse_json(self):
        self.assertTrue(self.parse_json_obj.parse_json("2018-01-20"))
