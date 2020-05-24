# Definition
-- SQLAlchemy Core vs Sqlalchemy ORM 
-- https://docs.sqlalchemy.org/en/13/
-- Core is use to data warehouse / reporting/ analysis and other senarios
-- ORM is use in DDD 

# Install infrastructure
# SQLALCHEMY
-- $ pip install sqlalchemy

# DBAPI 
## PostgreSQL:(Psycopg2) 
-- $ pip install psycopg2
## MySQL:(PyMySQL) 
- $ pip install pymysql

# Connecting to database. 
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# The create_engine function returns an instance of an engine; however, it does not actually open a connection until an action is called that would require a connection, such as a query.
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# sqllite 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cookies.db')
engine2 = create_engine('sqlite:///:memory:')
engine3 = create_engine('sqlite:////home/cookiemonster/cookies.db')
engine4 = create_engine('sqlite:///c:\\Users\\cookiemonster\\cookies.db')
print('create engine sqllite in memory success!')


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# mysql
from sqlalchemy import create_engine
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, create_engine)
from urllib import parse

engineString = 'mysql+pymysql://root:%s@localhost/pythondb' % parse.unquote_plus('P@ssw0rd')
engine = create_engine(engineString,echo = True)

print('create engine sqllite in memory success!',engine)

metadata = MetaData()

cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)
metadata.create_all(engine)

ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)

'''print(str(ins))'''
result = connection.execute(ins)

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# using mysql connector instead.
# install mysql connector 
# $ pip install mysql-connector-python
import mysql.connector
import pprint
printer = pprint.PrettyPrinter(indent=1)
connect_args = {
    "host": "localhost",
    "port": 3306, 
    "user": "root",
    "password": "P@ssw0rd",
    "database": "pythondb"
}

db1 = mysql.connector.connect(**connect_args)
db1.set_charset_collation(
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci")

result = db1.cmd_query("SELECT * FROM cookies WHERE cookie_id = 1")
print(f"id of db1 is {db1.connection_id}")
printer.pprint(result)

result_set = db1.get_rows()
printer.pprint(result_set)

db1.close()


