from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import SQL_CONNECTION

engine = create_engine(SQL_CONNECTION)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# todo: 调整经纬度的存储方式
class Fofa(Base):
    """
    存储ip的基本信息，城市，省份，经纬度
    """
    __tablename__ = "fv_basic"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(255))
    country_name = Column(String(255))
    province = Column(String(20))
    latitude = Column(String(20))
    longitude = Column(String(20))

    # todo: Bad code, should refactor
    @staticmethod
    def query(ip):
        return session.query(Fofa).filter(Fofa.ip == ip).all()

    @staticmethod
    def add_basic(ip, country_name, province, latitude, longitude):
        count = Fofa.query(ip)
        if count:
            raise EOFError("Hav already one")
        one = Fofa(
            ip=ip,
            country_name=country_name,
            province=province,
            latitude=latitude,
            longitude=longitude,
        )
        session.add(one)
        session.commit()

    @staticmethod
    def delete_basic(ip):
        session.query(Fofa).filter(Fofa.ip == ip).delete(
            synchronize_session="fetch"
        )
        session.commit()

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.ip)


Base.metadata.create_all(engine)

