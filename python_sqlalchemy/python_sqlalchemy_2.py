# Querying data.
from sqlalchemy import create_engine
from sqlalchemy import select 
from urllib import parse

engineString = 'mysql+pymysql://root:%s@localhost/pythondb' % parse.unquote_plus('P@ssw0rd')
engine = create_engine(engineString,echo = True)
connection = engine.connect()




