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
    cursor = dbapi_connection.cursor()
    cursor.execute("select * from cookies")
    results_first = cursor.fetchall()
    print('KQ raw select query : ')
    printer.pprint(results_first)
    cursor.close()

finally: 
    dbapi_connection.close()


try:
    dbapi_connection = engine.raw_connection()
    # args = [a]
    args = [45]
    cursor = dbapi_connection.cursor()
    cursor.callproc('SP_GET_FROM_COOKIES_BY_ID', args)
    results_second = list(cursor.fetchall())
    print('KQ raw call proc query : ')
    printer.pprint(results_second)
    cursor.close()    

except pymysql.err.InternalError as error: 
    print("Have internal error as: ",error)
except NameError as error: 
    print("Have type error:", error)
except: 
    print("Not define error !!. Please review source carefully")
finally: 
    dbapi_connection.close()