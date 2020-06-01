from __future__ import annotations

import model
from model import OrderUnit
from repository import ISqlArchemyAbstractRepository


class InvalidOrderItem(Exception): 
    pass

def is_valid_order_item(batch_order_item, batches):
    return batch_order_item in {b.batch_order_item for b in batches}

def allocate(orderUnit: OrderUnit, repo:ISqlArchemyAbstractRepository , session) -> str:
    batches = repo.list()
    if not is_valid_order_item(orderUnit.order_item, batches): 
        raise InvalidOrderItem(f'Invalid OrderItems')
    
    batch_id = model.allocate(orderUnit,batches)
    session.commit()
    return batch_id

