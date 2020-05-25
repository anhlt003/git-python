from sqlalchemy import create_engine
from sqlalchemy import select 
from sqlalchemy.exc import IntegrityError,InternalError,IdentifierError
from urllib import parse
from python_sqlalchemy_1 import cookies
import pprint
import pymysql

engineString = 'mysql+pymysql://root:%s@localhost/pythondb' % parse.unquote_plus('P@ssw0rd')
engine = create_engine(engineString,echo = True)
printer = pprint.PrettyPrinter()

try:
    dbapi_connection = engine.raw_connection()
    dbapi_connection.begin()
    
    cursor = dbapi_connection.cursor()

    args = [45,46]
    cursor.callproc('SP_UPDATE_COOKIES_BY_ID', args)

    args = [45]
    cursor.callproc('SP_GET_FROM_COOKIES_BY_ID', args)

    dbapi_connection.commit()    
    cursor.close()    

except: 
    print("Not define error !!. Please review source carefully")
    dbapi_connection.rollback()  
    raise
finally: 
    dbapi_connection.close()