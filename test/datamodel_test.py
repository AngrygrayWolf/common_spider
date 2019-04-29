import unittest

from model.Basic import Fofa


class DataModelTestCase(unittest.TestCase):
    # 需要测试用例
    def setUp(self):
        self.fofa = Fofa

    def test_fofa_query_basic(self):
        try:
            test = Fofa.add_basic(
                ip="8.8.8.8",
                country_name="China",
                province="xinjiang",
                latitude="12",
                longitude="13",
            )
        except EOFError as e:
            pass
        source = self.fofa.query('8.8.8.8')
        self.assertGreater(len(source), 0)
        self.assertEqual(source[0].country_name, "China")

    def test_fofa_add_basic(self):
        try:
            test = Fofa.add_basic(
                ip="8.8.8.9",
                country_name="China",
                province="xinjiang",
                latitude="12",
                longitude="13",
            )
        except EOFError as e:
            pass
        finally:
            source = self.fofa.query("8.8.8.9")
            self.assertGreater(len(source), 0)
            self.assertEqual(source[0].latitude, "12")

    def test_fofa_delete_basic(self):
        self.fofa.delete_basic("8.8.8.8")
        self.fofa.delete_basic("8.8.8.9")
        one = self.fofa.query("8.8.8.8")
        two = self.fofa.query("8.8.8.9")
        self.assertFalse(one)
        self.assertFalse(two)

