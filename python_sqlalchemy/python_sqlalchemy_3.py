from sqlalchemy import select, insert
from python_sqlalchemy_2 import users
from python_sqlalchemy_2 import connection


ins = insert(users).values(
    username="cookiemon",
    email_address="mon@cookie.com",
    phone="111-111-1111",
    password="password"
)

# print(str(ins))
result = connection.execute(ins)
print(result.inserted_primary_key)