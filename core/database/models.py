from sqlalchemy import Column, VARCHAR, TEXT
from sqlalchemy.dialects.postgresql import TIMESTAMP

from .base import Base


class Brand(Base):
    title = Column(
        VARCHAR(32),
        unique=True,
        nullable=False,
    )


class Product(Base):
    title = Column(
        VARCHAR(32),
        nullable=False,
    )
    serial_number = Column(
        VARCHAR(128),
        unique=True,
    )


class Service_Center(Base):
    title = Column(
        VARCHAR(32),
        unique=True,
        nullable=False,
    )
    contact = Column(
        TEXT,
    )


class Document(Base):
    document_type = Column(
        VARCHAR(32),
        unique=True,
    )
    number = Column(
        VARCHAR(64),
        unique=True,
    )
    date = Column(
        TIMESTAMP,
    )


class Client(Base):
    name = Column(
        VARCHAR(64),
        unique=True,
        nullable=False,
    )
    contact = Column(
        TEXT,
    )


class Provider(Base):
    title = Column(
        VARCHAR(32),
        unique=True,
        nullable=False,
    )
    contact = Column(
        TEXT,
    )
