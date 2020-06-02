import pytest
import model
import repository
import services
from datetime import datetime
import decimal
import time


class FakeRepository(repository.SqlArchemyAbstractRepository):

    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)


class FakeSession():
    committed = False

    def commit(self):
        self.committed = True


def test_returns_allocation(): 
    today = datetime.now()
    orderUnit = model.OrderUnit('order66','SER',today,None,290,1,1,0,300)
    batch = model.Batch('batch66','SER',300,today)
    repo = FakeRepository([batch])

    result = services.allocate(orderUnit,repo,FakeSession())
    
    # session.add(batch)
    # session.commit()
    assert result == "batch66"