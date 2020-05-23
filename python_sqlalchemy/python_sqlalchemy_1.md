# Definition
-- SQLAlchemy Core vs Sqlalchemy ORM 
-- https://docs.sqlalchemy.org/en/13/
-- Core is use to data warehouse / reporting/ analysis and other senarios
-- ORM is use in DDD 

# Install infrastructure
# SQLALCHEMY
-- $ pip install sqlalchemy

# DBAPI 
PostgreSQL:(Psycopg2) $ pip install psycopg2
MySQL:(PyMySQL) $ pip install pymysql

# Connecting to database. 
# The create_engine function returns an instance of an engine; however, it does not actually open a connection until an action is called that would require a connection, such as a query.
# sqllite 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cookies.db')
engine2 = create_engine('sqlite:///:memory:')
engine3 = create_engine('sqlite:////home/cookiemonster/cookies.db')
engine4 = create_engine('sqlite:///c:\\Users\\cookiemonster\\cookies.db')
print('create engine sqllite in memory success!')