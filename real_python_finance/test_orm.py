import model
from datetime import datetime
import decimal
import time

# test tbl_order
def test_order_unit_can_add_to_table_by_raw_query(session):
    session.execute('DELETE FROM tbl_allocations')
    session.execute('DELETE FROM tbl_order_unit')
    session.commit()
    session.execute(
        'INSERT INTO tbl_order_unit(order_id,order_item,order_start_time,order_end_time,order_price,order_lot,order_margin,order_stoploss,order_takeprofit) VALUES ' 
        '("order01", "BITCOIN", "2020-05-26 14:53:46","2020-05-26 14:53:46",1000,0.1,1,0,100),'
        '("order02", "ETH", "2020-05-26 14:53:47","2020-05-26 14:53:47",700,0.2,1,0,140),'
        '("order03", "BCASH", "2020-05-26 14:53:48","2020-05-26 14:53:48",100,0.3,1,0,30)'
    )
    session.commit()
    expected = [
        model.OrderUnit("order01", "BITCOIN", 
                        datetime(2020,5, 26, 14, 53, 46),
                        datetime(2020, 5, 26, 14, 53, 46),
                        1000,
                        decimal.Decimal("0.10"),
                        1,
                        decimal.Decimal("0.00"),
                        decimal.Decimal("100.00")),

        model.OrderUnit("order02", 
                        "ETH", 
                        datetime(2020, 5, 26, 14, 53, 47),
                        datetime(2020, 5, 26, 14, 53, 47),
                        700,
                        decimal.Decimal("0.20"),
                        1,
                        decimal.Decimal("0.00"),
                        decimal.Decimal("140.00")),

        model.OrderUnit("order03", 
                        "BCASH", 
                        datetime(2020, 5, 26, 14, 53, 48),
                        datetime(2020, 5, 26, 14, 53, 48),
                        100,
                        decimal.Decimal("0.30"),
                        1,
                        decimal.Decimal("0.00"),
                        decimal.Decimal("30.00"))
    ]

    
    assert session.query(model.OrderUnit).all() == expected


def test_order_unit_can_add_to_table_by_raw_orm(session):
    new_order = model.OrderUnit("order04", "LITECOIN", 
                        datetime(2020,5, 26, 14, 53, 46),
                        datetime(2020, 5, 26, 14, 53, 46),
                        1000,
                        0.10,
                        1,
                        0.00,
                        100.00)

    session.add(new_order)
    session.commit()

    row = list(session.execute('SELECT * from tbl_order_unit WHERE order_id = "order04"'))
    assert row ==[( 'order04', 
                    'LITECOIN', 
                    datetime(2020, 5, 26, 14, 53, 46), 
                    datetime(2020, 5, 26, 14, 53, 46), 
                    decimal.Decimal('1000.00'), 
                    decimal.Decimal('0.10'), 
                    1, 
                    decimal.Decimal('0.00'), 
                    decimal.Decimal('100.00'))]

# test tbl_batches.
def test_batch_can_add_to_table_by_raw_query(session):
    session.execute('DELETE FROM tbl_allocations')
    session.execute('DELETE FROM tbl_batches')
    session.commit()
    session.execute(
        'INSERT INTO  tbl_batches(batch_id,batch_order_item,_batch_total_money,batch_time)'
        ' VALUES ("batch_01","BitCoin",300,"2020-05-26 14:53:46")'
    )
    session.commit()

    expected = [
        model.Batch("batch_01","BitCoin",decimal.Decimal("300.00"),datetime(2020, 5, 26, 14, 53, 46))
    ]

    assert session.query(model.Batch).all() == expected

def test_batch_can_add_to_table_by_orm(session):
    session.execute('DELETE FROM tbl_allocations')
    session.commit()
    batch = model.Batch("batch_05","ERM",300,"2020-05-26 14:53:46")
    order = model.OrderUnit("order05", "ERM", 
                        datetime(2020,5, 26, 14, 53, 46),
                        datetime(2020, 5, 26, 14, 53, 46),
                        1000,
                        0.10,
                        1,
                        0.00,
                        100.00)
    batch.start_order(order)
    session.add(batch)
    session.commit()

    row = list(session.execute('SELECT batch_id,order_id FROM tbl_allocations'))
    assert row == [(batch.batch_id,order.order_id)]

def test_get_allocation_prop_by_mapper(session):
    #insert order unit
    session.execute(
    'INSERT INTO tbl_order_unit(order_id,order_item,order_start_time,order_end_time,order_price,order_lot,order_margin,order_stoploss,order_takeprofit) VALUES ' 
    '("order99", "BIT", "2020-05-27 14:53:46","2020-05-27 14:53:46",999,0.1,1,0,99.9)'
    )

    [[orderid]] = session.execute(
        'SELECT order_id FROM tbl_order_unit WHERE order_id=:order_id AND order_item=:order_item',
        dict(order_id='order99', order_item='BIT')
        )

    #insert batch
    session.execute(
    'INSERT INTO  tbl_batches(batch_id,batch_order_item,_batch_total_money,batch_time)'
    ' VALUES ("batch_99","BIT",3000,"2020-05-26 14:53:46")')

    [[batchid]] = session.execute(
        'SELECT batch_id FROM tbl_batches WHERE batch_id=:batch_id AND batch_order_item=:batch_order_item',
        dict(batch_id='batch_99', batch_order_item='BIT')
    )

    #insert allocation
    session.execute(
        'INSERT INTO tbl_allocations(order_id, batch_id) VALUES (:orderid, :batchid)',
        dict(orderid=orderid, batchid=batchid)
    )
    session.commit()

    # batch = session.query(model.Batch).one()
    batch = session.query(model.Batch).filter_by(batch_id = batchid).one()
    # print(batch._batch_ordered_allocations)
    # time.sleep(10) 
    assert batch._batch_ordered_allocations == {
        model.OrderUnit("order99", "BIT", 
                    datetime(2020,5, 27, 14, 53, 46),
                    datetime(2020, 5, 27, 14, 53, 46),
                    999,
                    decimal.Decimal("0.10"),
                    1,
                    decimal.Decimal("0.00"),
                    decimal.Decimal("99.90"))
    }
        

