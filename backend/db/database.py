from sqlalchemy import*
from sqlalchemy.orm import sessionmaker

DB_URL='mysql+pymysql://takealook:tmddk0908@db:3306/apidb'

class enginconn:
    def __init__(self):
        self.engine=create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session=sessionmaker(bind=self.engine)
        session=Session()
        return session

    def connection(self):
        conn=self.engine.connect()
        return conn