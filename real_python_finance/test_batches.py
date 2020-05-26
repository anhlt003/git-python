from datetime import date,datetime,timedelta
from model import Batch, OrderUnit

today = datetime.now()
tomorrow = today + timedelta(days=1)

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch('batch_01','BitCoin',300,today)
    order  = OrderUnit('order_01','BitCoin',today,None,290,1,1,0,300)
    batch.start_order(order)

    assert batch.batch_available_money == 10