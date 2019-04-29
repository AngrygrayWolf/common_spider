import components.fofa_sdk.client as fofa
import components.virustotal.client as vt
from config import secure


class Query:
    def __init__(self):
        self.fofa = fofa.Client(secure.EMAIL, secure.KEY)
        self.vt = vt.Client(secure.VT_KEY)

    def get_domains(self, ip):
        return self.fofa.get_domains(ip=ip)

    def get_sub_domains(self, domains):
        return self.vt.get_subdomains(domains)

    def get_all_domains(self, ip):
        return self.get_sub_domains(self.get_domains(ip))


