from unittest import TestCase
from PyCodeChallenge import BuildReqRes


class TestBuildReqRes(TestCase):
    def setUp(self):
        self.build = BuildReqRes()

    def test_get_api_url(self):
        self.assertTrue(self.build.get_api_url("2018-01-20"))

    def test_get_response(self):
        self.assertTrue(self.build.get_response(self.build.get_api_url("2018-01-20")))




