import unittest

from app import db


class BasicTests(unittest.TestCase):
    ''' Testing basic test cases '''

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_main(self):
        self.assertTrue(True)
