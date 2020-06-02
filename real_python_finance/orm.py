from sqlalchemy import (
    Table,MetaData,Column,Integer,String,
    DateTime,ForeignKey,Numeric,Float
)
from sqlalchemy.orm import mapper,relationship
import model
from datetime import datetime

metadata = MetaData()

order_unit = Table(
    'tbl_order_unit', metadata,
    Column('order_id', String(10),primary_key = True),
    Column('order_item', String(20)),
    Column('order_start_time', DateTime, nullable = False),
    Column('order_end_time',DateTime),
    Column('order_price',Float(10,2)),
    Column('order_lot',Float(10,2)),
    Column('order_margin',Integer),
    Column('order_stoploss',Float(10,2)),
    Column('order_takeprofit',Float(10,2)),
)

batches = Table (
    'tbl_batches', metadata,
    Column('batch_id',String(10),primary_key=True),
    Column('batch_order_item',String(20)),
    Column('_batch_total_money',Float(11,2)),
    Column('batch_time',DateTime, nullable = False),
)

allocations = Table(
    'tbl_allocations', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('order_id', ForeignKey('tbl_order_unit.order_id')),
    Column('batch_id', ForeignKey('tbl_batches.batch_id')),
)

def start_mappers(): 
    order_mapper = mapper(model.OrderUnit, order_unit)
    # batch_mapper = mapper(model.Batch,batches)
    mapper(model.Batch, batches, properties={
        '_batch_ordered_allocations': relationship(
        order_mapper,
        secondary=allocations,
        collection_class=set,
        )
    })