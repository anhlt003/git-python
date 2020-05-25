from sqlalchemy import Table,Column,Integer,Numeric,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class User(Base):
    __tablename__ = 'm_user'

    user_id = Column(Integer, primary_key = True)
    user_name = Column(String(50))
    user_password = Column(String(8))
    user_description = Column(String(500))

class Finance(Base):
    __tablename__ = 'm_finance'

    finance_obj_id = Column(String(5),primary_key = True)
    finance_obj_type = Column(Integer, index = True)
    finance_obj_name = Column(String(10))
    finance_obj_description = Column(String(256))

class Order(Base):
    __tablename__ = 'tr_order'

    order_id = Column(String(10), primary_key = True)
    order_name = Column(String(20))
    order_start_time = Column(DateTime())
    order_end_time = Column(DateTime())
    order_price = Column(Numeric(12,2))
    order_lot  = Column(Numeric(15,2))
    order_margin = Column(Integer(3))
    order_stoploss = Column(Numeric(12,2))
    order_takeprofit = Column(Numeric(12,2))

