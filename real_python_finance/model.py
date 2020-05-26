from __future__ import annotations
from dataclasses import dataclass
from datetime import date , datetime
from typing import Optional, List, Set

class RunOutAccount(Exception):
    pass

def allocate(order:OrderUnit, batches: List[Batch]) -> str: 
    try: 
        batch = next(
                b for b in sorted(batches) if b.can_allocate(order)
            )
        batch.start_order(order)
        return batch.batch_id
    except StopIteration: 
        raise RunOutAccount(f'Account is broken: {order.order_item}')

@dataclass(frozen=True)
class OrderUnit:
    order_id: str
    order_item : str
    order_start_time: datetime
    order_end_time: datetime
    order_price : float
    order_lot : float
    order_margin: int 
    order_stoploss: float
    order_takeprofit: float

class Batch: 
    def __init__(self,  batch_id: str, 
                        batch_order_item: str, 
                        batch_total_money: int, 
                        batch_time: Optional[date]
                ):
        self.batch_id = batch_id
        self.batch_order_item = batch_order_item
        self.batch_time = batch_time
        self._batch_total_money = batch_total_money #can changed properties
        self._batch_ordered_allocations = set()  #list of order have to be set

    def __repr__(self):
        return f'<Batch {self.batch_id}>'

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.batch_id == self.batch_id
    
    def __hash__(self):
        return hash(self.batch_id)

    def __gt__(self, other):
        if self.batch_time is None:
            return False
        if other.batch_time is None:
            return True
        return self.batch_time > other.batch_time    
    
    def start_order(self, order: OrderUnit) :
        if self.can_allocate(order): 
            self._batch_ordered_allocations.add(order)

    def stop_order(self, order: OrderUnit) : 
        if order in self._batch_ordered_allocations: 
            self._batch_ordered_allocations.remove(order)

    @property
    def batch_ordered_money(self) -> int: 
        return sum((o.order_price*o.order_lot) for o in self._batch_ordered_allocations)

    @property
    def batch_available_money(self) -> int:
        return self._batch_total_money - self.batch_ordered_money

    def can_allocate(self, order: OrderUnit) -> bool: 
        return (self.batch_order_item == order.order_item and    
                self.batch_available_money >= (order.order_price*order.order_lot))
