import os 
from urllib import parse
import requests

def get_mysql_uri(): 
    host = os.environ.get('DB_HOST','localhost')
    port = 3306
    password = 'P@ssw0rd'
    user,db_name = 'root','real_python_finance_db'
    return f"mysql+pymysql://{user}:%s@{host}:{port}/{db_name}" % parse.unquote_plus('P@ssw0rd')
    # return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"


# print( os.environ.get('DB_HOST','localhost'))
# print(get_mysql_uri())

def get_api_url():
    host = os.environ.get('API_HOST', '127.0.0.1')
    port = 5000 if host == '127.0.0.1' else 80
    return f"http://{host}:{port}"
 
# print(get_api_url())

# requests.get(get_api_url())