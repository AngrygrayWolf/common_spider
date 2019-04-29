from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# todo: 调整经纬度的存储方式
class Fofa(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(255))
    country_name = Column(String(255))
    province = Column(String(20))
    latitude = Column(String(20))
    longitude = Column(String(20))

