from __future__ import annotations

from finance.domain import model
from finance.domain.model import OrderUnit
from finance.adapters.repository import ISqlArchemyAbstractRepository
from finance.servicelayer import unit_of_work


class InvalidOrderItem(Exception): 
    pass

def is_valid_order_item(order_item, batches):
    return order_item in {b.batch_order_item for b in batches}

# def allocate(orderUnit: OrderUnit, repo:ISqlArchemyAbstractRepository , session) -> str:
#     # batch = model.Batch("batch_55","E2E",3000,"2020-05-26 14:53:46")
#     # session.add(batch)
#     # session.commit()

#     batches = repo.list()
#     if not is_valid_order_item(orderUnit.order_item, batches): 
#         raise InvalidOrderItem(f'Invalid OrderItems')
    
#     batch_id = model.allocate(orderUnit,batches)
#     # session.add(orderUnit)
#     session.commit()
#     return batch_id

# def find_batch_match_order_item(order_item,batches):
#     return (b for b in batches if b.batch_order_item == order_item)

# def allocate_and_save_order_unit(orderUnit: OrderUnit, repo: ISqlArchemyAbstractRepository, session) -> str:
#     batches = repo.list()
#     if not is_valid_order_item(orderUnit.order_item, batches): 
#         raise InvalidOrderItem(f'Invalid OrderItems')
    
#     batch = find_batch_match_order_item(orderUnit.order_item, batches)
#     batch_id = model.allocate_one(orderUnit,batch)
#     print(batch_id)
#     print(orderUnit)    
#     session.add(orderUnit)
#     session.commit()
#     return batch_id

# def remove_order(orderUnit: OrderUnit,repo: ISqlArchemyAbstractRepository,session): 
#     result = repo.delele(orderUnit)
#     session.commit()

#     # return result

def add_batch ( batch_id: str, 
                batch_oder_item: str, 
                batch_total_money: float, 
                batch_time: Optional[date],
                uow: unit_of_work.AbstractUnitOfWork):   

    with uow:
        uow.batches.add(model.Batch(batch_id, batch_oder_item, batch_total_money, batch_time))
        uow.commit()
