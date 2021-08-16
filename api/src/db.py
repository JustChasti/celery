import sys
import os
import psycopg2
import config

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

from src.base import Link, Review, Numeric
from src.base import Session


def append_link(link):
    session = Session()
    try:
        link = Link(url=link)
        session.add(link)
        session.commit()
    except Exception as e:
        create_tabless(user, passs, name)
        link = Link(url=link)
        session.add(link)
        session.commit()
    session.close()


def update_link(link, name, price, articul, k_otz, rev_list):
    session = Session()
    try:
        upd = session.query(Link).filter(Link.url == link).one()
        upd.name = name
        if upd.price != int(price) or upd.articul != int(articul) or upd.col_otz != int(k_otz):
            num = Numeric(product_id=upd.id, price=int(price),
                          articul=int(articul), col_otz=int(k_otz))
            session.add(num)
            upd.price = int(price)
            upd.articul = int(articul)
            upd.col_otz = int(k_otz)
        id = upd.id
        session.commit()
        session.close()
        update_reviews(id, rev_list)
    except Exception as e:
        print(link)


def update_reviews(link_id, rev_list):
    session = Session()
    for i in rev_list:
        try:
            review = session.query(Review).filter(Review.product_id == link_id,
                                                  Review.comment == i['Com']).one()
        except Exception as e:
            review = Review(product_id=link_id, user=i['Name'],
                            mark=int(i['Mark']), comment=i['Com'])
            session.add(review)
    session.commit()
    session.close()


def get_links():
    session = Session()
    try:
        links = session.query(Link).all()
        urls = []
        for i in links:
            if i.url == 'link1':
                pass
            else:
                req = {}
                req['link'] = i.url
                urls.append(req)
        return urls
    except Exception as e:
        return []
    session.close()


def get_all():
    session = Session()
    try:
        links = session.query(Link).all()
        urls = []
        for i in links:
            req = {}
            if i.url == 'link1':
                pass
            else:
                try:
                    req['url'] = i.url
                    req['name'] = i.name
                    req['price'] = i.price
                    req['articul'] = i.articul
                    req['col_otz'] = i.col_otz
                    urls.append(req)
                except Exception as e:
                    req['url'] = i.url
                    urls.append(req)
        session.close()
        return urls
    except Exception as e:
        session.close()
        return []


if __name__ == "__main__":
    pass
