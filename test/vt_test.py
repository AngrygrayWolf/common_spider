import sys
import unittest
import components.virustotal.client as client
from config import secure

sys.path.append('../')
print(sys.path)


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = client.Client(secure.VT_KEY)

    def test_get_domain(self):
        query = "fofa.so"
        domain_infos = self.client.get_domain_infos(query)
        print(domain_infos)
        self.assertIn("undetected_referrer_samples", domain_infos)
        self.assertIn("subdomains", domain_infos)

    def test_get_subdomains(self):
        """
        获取子域名信息
        :return:
        """
        domains = ["baidu.com", "qq.com", "google.com"]
        data = self.client.get_subdomains(domains=domains)

        self.assertEqual(len(data), len(domains))
        self.assertGreaterEqual(len(data), 0)
        self.assertIn(domains[0], data)
        self.assertGreater(len(data[domains[0]]), 0)
