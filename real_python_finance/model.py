from __future__ import annotations
from dataclasses import dataclass
from datetime import date , datetime
from typing import Optional, List, Set

class RunOutAccount(Exception):
    pass

@dataclass(frozen=True)
class OrderUnit:
    order_id: str
    order_name : str
    order_start_time: datetime
    order_end_time: datetime
    order_price : float
    order_lot : float
    order_margin: int 
    order_stoploss: float
    order_takeprofit: float

class Batch: 
    def __init__(self, batch_unit_id: str, batch_unit_name: str, batch_order_money: int, batch_unit_time: Optional[date]):
        self.batch_unit_id = batch_unit_id
        self.batch_unit_name = batch_unit_name
        self.batch_unit_time = batch_unit_time
        self._ordered_money = batch_order_money #can changed properties
        self._ordered_allocations = set()  #list of order have to be set
    
    def call_set_order(self) -> int :
        return sum()