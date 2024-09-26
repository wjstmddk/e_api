from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Test(Base):
    __tablename__='connect'

    id=Column(INT, nullable=False, primary_key=True)
    connect_status=Column(INT)
