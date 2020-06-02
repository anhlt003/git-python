from __future__ import annotations

import model
from model import OrderUnit,Batch
from repository import ISqlArchemyAbstractRepository


class InvalidOrderItem(Exception): 
    pass

def is_valid_order_item(order_item, batches):
    return order_item in {b.batch_order_item for b in batches}

def allocate(orderUnit: OrderUnit, repo:ISqlArchemyAbstractRepository , session) -> str:
    # batch = model.Batch("batch_55","E2E",3000,"2020-05-26 14:53:46")
    # session.add(batch)
    # session.commit()

    batches = repo.list()
    if not is_valid_order_item(orderUnit.order_item, batches): 
        raise InvalidOrderItem(f'Invalid OrderItems')
    
    batch_id = model.allocate(orderUnit,batches)
    # session.add(orderUnit)
    session.commit()
    return batch_id

def find_batch_match_order_item(order_item,batches):
    return (b for b in batches if b.batch_order_item == order_item)

def allocate_and_save_order_unit(orderUnit: OrderUnit, repo: ISqlArchemyAbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_order_item(orderUnit.order_item, batches): 
        raise InvalidOrderItem(f'Invalid OrderItems')
    
    batch = find_batch_match_order_item(orderUnit.order_item, batches)
    batch_id = model.allocate_one(orderUnit,batch)
    print(batch_id)
    print(orderUnit)    
    session.add(orderUnit)
    session.commit()
    return batch_id

