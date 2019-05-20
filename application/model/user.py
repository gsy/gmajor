# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger, Column, Index, Integer, String, UniqueConstraint, Text, Float
from sqlalchemy.dialects.mysql import TINYINT

from application.model import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(12), nullable=False, index=True)
    username = Column(String(12), nullable=False, index=True)
    password = Column(String(36), nullable=False)
    status = Column(TINYINT(unsigned=True, display_width=2), nullable=True)
    create_time = Column(Integer, nullable=True)
    update_time = Column(Integer, nullable=True)
