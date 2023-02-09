import unittest

from get_data import *


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        ret = handler(None, None)
