import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.exc import OperationalError
from pathlib import Path
from orm import metadata, start_mappers
from urllib import parse
import requests
from requests.exceptions import ConnectionError
import time
import config
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
    engineString = 'mysql+pymysql://root:%s@localhost:3306/real_python_finance_db?charset=utf8mb4' % parse.unquote_plus('P@ssw0rd')
    engine = create_engine(engineString,echo = True)
    metadata.create_all(engine)
    return engine
# print('mysql+pymysql://root:%s@localhost/real_python_finance_db?charset=utf8mb4' % parse.unquote_plus('P@ssw0rd'))

@pytest.fixture
def session(real_python_finance_db):
    start_mappers()
    yield sessionmaker(bind=real_python_finance_db)()
    clear_mappers()


@pytest.fixture
def restart_api():
    (Path(__file__).parent/'flask_app.py').touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()


def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    url = config.get_api_url()
    # requests.get(url)
    while time.time() < deadline:
        try:
            return requests.get(url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail('API never came up')