import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, start_mappers
from urllib import parse

# @pytest.fixture
# def in_memory_db():
#     engine = create_engine('sqlite:///:memory:')
#     metadata.create_all(engine)
#     return engine
# @pytest.fixture
# def session(in_memory_db):
#     start_mappers()
#     yield sessionmaker(bind=in_memory_db)()
#     clear_mappers()

@pytest.fixture
def real_python_finance_db(): 
    engineString = 'mysql+pymysql://root:%s@localhost/real_python_finance_db?charset=utf8mb4' % parse.unquote_plus('P@ssw0rd')
    engine = create_engine(engineString,echo = True)
    metadata.create_all(engine)
    return engine

@pytest.fixture
def session(real_python_finance_db):
    start_mappers()
    yield sessionmaker(bind=real_python_finance_db)()
    clear_mappers()

