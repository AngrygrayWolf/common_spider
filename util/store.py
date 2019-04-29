from model.Basic import Fofa


class Store:
    @staticmethod
    def insert_fofa_ip(ip, result):
        Fofa.add_basic(
            ip=ip,
            country_name=result[0],
            province=result[1],
            latitude=result[2],
            longitude=result[3]
        )









