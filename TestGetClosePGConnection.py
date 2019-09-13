from unittest import TestCase

from PyCodeChallenge import GetPGConnection,ClosePGConnection

class TestGetClosePGConnection(TestCase):
    def setUp(self):
        self.pg_connect = GetPGConnection()
        self.close_pg_connect = ClosePGConnection()

    def test_get_pg_connection(self):
        self.assertEqual((self.pg_connect.get_pg_connection()).closed, 0)

    def test_close_pg_connection(self):
        self.assertTrue(self.close_pg_connect.close_pg(self.pg_connect.get_pg_connection()))
