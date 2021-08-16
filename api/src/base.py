from time import sleep

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from loguru import logger

from config import base_user, base_pass, base_name, base_host, base_port

Base = declarative_base()


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String(512), nullable=False)
    name = Column(String(256), nullable=True)
    price = Column(Integer, nullable=True)
    articul = Column(Integer, nullable=True)
    col_otz = Column(Integer, nullable=True)


class Review(Base):
    __tablename__ = 'rewiews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Link.id), nullable=False)
    user = Column(String(64), nullable=False)
    mark = Column(Integer, nullable=False)
    comment = Column(String(10000), nullable=False)


class Numeric(Base):
    __tablename__ = 'numericpar'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Link.id), nullable=False)
    price = Column(Integer, nullable=True)
    articul = Column(Integer, nullable=True)
    col_otz = Column(Integer, nullable=True)


data = {
    'drivername': 'postgresql+psycopg2',
    'host': base_host,
    'port': base_port,
    'username': base_user,
    'password': base_pass,
    'database': base_name,
}
for i in range(3):
    try:
        engine = create_engine(URL(**data))
        engine.connect()
        Base.metadata.create_all(engine)
    except Exception as e:
        logger.warning('I cant connect to database. Creating her***')
        try:
            connection = psycopg2.connect(user=base_user, password=base_pass)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            sql_create_database = cursor.execute("create database " + base_name)
            cursor.close()
            connection.close()
            engine = create_engine(URL(**data))
            engine.connect()
            Base.metadata.create_all(engine)
            Base.metadata.bind = engine
        except Exception as e:
            print('pizdec')
            logger.exception("Postgres connection error")
            sleep(5)

Session = sessionmaker(bind=engine)
