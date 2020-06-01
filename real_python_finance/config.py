import os 

def get_mysql_uri(): 
    host = os.environ.get('DB_HOST','localhost')
    port = 3306
    password = 'P@ssw0rd'
    user,db_name = 'root','P@ssw0rd'
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"

# print( os.environ.get('DB_HOST','localhost'))
# print(get_mysql_uri())

def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f"http://{host}:{port}"