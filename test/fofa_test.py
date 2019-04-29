import sys
import unittest
import components.fofa_sdk.client as client
from config import secure
sys.path.append('../')


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = client.Client(secure.EMAIL, secure.KEY)

    def test_get_userinfo(self):
        userinfo = self.client.get_userinfo()
        self.assertIn("isvip", userinfo)

    def test_get_data_normal(self):
        query = """fofa.so"""
        data = self.client.get_data(query_str=query)
        self.assertIn("results", data)
        self.assertIn("page", data)
        self.assertIn("mode", data)

    def test_get_data_field(self):
        """
        测试返回结果是否在fields范围之内
        :return:
        """
        query = """host = 'fofa.so'"""
        fields = "host, title, port, country"
        data = self.client.get_data(query, fields=fields)
        # TODO: 写入样本数据（只写入一次）
        self.assertIn("results", data)
        self.assertIn("page", data)
        self.assertIn("size", data)
        self.assertIn("mode", data)
        self.assertIn("query", data)

        self.assertEqual(len(data["results"][0]), len(fields.split(',')))

    def test_get_domain(self):
        data = self.client.get_domains(ip="91.223.115.81")
        self.assertGreater(len(data), 0)
        error_data = self.client.get_domains(ip="12.12.12.12")
        self.assertEqual(error_data, 'No results')

    def test_get_ip_basic(self):
        data = self.client.get_ip_basic(ip="8.8.8.8")
        print(data)
        self.assertGreater(len(data), 0)
        self.assertEqual(len(data["results"][0]), 4)

if __name__ == '__main__':
    unittest.main()
