# pylint: disable=protected-access
import model
import repository
import decimal
from datetime import datetime

def test_repository_can_save_batch(session):

    session.execute('delete from tbl_batches where batch_id =:batch_id',dict(batch_id='batch_88'))
    batch=model.Batch("batch_88","BRE",decimal.Decimal("300.00"),"2020-05-26 14:53:46")
    repo = repository.SqlArchemyAbstractRepository(session)
    repo.add(batch)
    session.commit()

    # row = list(session.execute(
    #     'SELECT * FROM tbl_batches WHERE batch_id=:batch_id',
    #     dict(batch_id='batch_88')
    # ))

    row= [session.query(model.Batch).filter_by(batch_id='batch_88').one()]
    expected = [model.Batch("batch_88","BRE",decimal.Decimal("300.00"),datetime(2020, 5, 26, 14, 53, 46))]
    
    print('DEBUG: ROW',row)
    print('DEBUG: EXPECTED ',expected)
    assert row == expected
    #assert True