from __future__ import annotations
from dataclasses import dataclass
from datetime import date , datetime
from typing import Optional, List, Set

class OutOfAccount(Exception):
    pass

@dataclass(frozen=True)
class OrderLine:
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
    def __init__(self, batch_id: str, batch_unit_name: str, batch_total_money: int, batch_time: Optional[date]):
        self.batch_id = batch_id
        self.batch_unit_name = batch_unit_name
        self.batch_time = batch_time
        self._purchased_money = batch_total_money
        self._allocations = set()  
    
    def call_set_order(self) -> int :
        return sum()