import unittest

from util.query import Query


class QueryTestCase(unittest.TestCase):
    def setUp(self):
        self.Query = Query()

    def test_util(self):
        ip = "91.223.115.81"
        domains = self.Query.get_domains(ip=ip)
        self.assertGreater(len(domains), 0)
        self.assertEqual(domains[0], 'ctif.org')

        subdomains = self.Query.get_sub_domains(domains)
        self.assertIn('ctif.org', subdomains)
        self.assertGreater(len(subdomains[domains[0]]), 0)
        self.assertIn('www.ctif.org', subdomains['ctif.org'])

        all_domains = self.Query.get_all_domains(ip=ip)
        self.assertEqual(all_domains, subdomains)