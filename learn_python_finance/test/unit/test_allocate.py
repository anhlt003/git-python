from datetime import date,datetime,timedelta
import pytest
from model import allocate,allocate_one, OrderUnit, Batch, RunOutAccount

today = datetime.now()
tomorrow = today + timedelta(days=1)

def test_raises_out_of_stock_exception_if_cannot_allocate(): 
    batch = Batch('batch_01','BitCoin',300,today)
    allocate(OrderUnit('order_01','BitCoin',today,None,300,1,1,0,300),[batch])

    with pytest.raises(RunOutAccount, match = 'Account is broken: Ether'):
        allocate(OrderUnit('order_02','Ether',tomorrow,None,300,1,1,0,300),[batch])

def test_returns_batch_id_after_allocate_one_batch(): 
    batch_01 = Batch('batch_01','BitCoin',300,today) 
    order = OrderUnit('order_01','BitCoin',today,None,300,1,1,0,300)
    rtnValue = allocate(order,[batch_01])
    
    assert rtnValue == batch_01.batch_id

def test_returns_batch_id_after_allocate_two_batches(): 
    batch_01 = Batch('batch_01','BitCoin',300,today) 
    batch_02 = Batch('batch_02','BitCoin',300,tomorrow) 
    order = OrderUnit('order_01','BitCoin',today,None,300,1,1,0,300)
    rtnValue = allocate(order,[batch_01,batch_02])
    
    assert rtnValue == batch_01.batch_id

def test_return_true_after_allocate_one_batch(): 
    batch_01 = Batch('batch_01','BitCoin',300,today) 
    order = OrderUnit('order_01','BitCoin',today,None,300,1,1,0,300)
    rtnValue = allocate_one(order,batch_01)

    assert rtnValue == True