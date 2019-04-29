import unittest

from components.fofa_sdk import client as fofa
from components.virustotal import client as vk
from config import secure


class ClientTestGetDomain(unittest.TestCase):
    def setUp(self):
        self.fofa = fofa.Client(secure.EMAIL, secure.KEY)
        self.vk = vk.Client(secure.VT_KEY)

    def test_get_domains(self):
        query = """ip = '91.223.115.81'"""
        fields = "domain"
        domain = self.fofa.get_json_data(query, fields=fields)
        print(domain)
        # domains = self.vk.get_domain_infos(domain=domain)