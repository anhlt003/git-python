from sqlalchemy import create_engine
from sqlalchemy import insert
from urllib import parse
from python_sqlalchemy_1 import cookies


engineString = 'mysql+pymysql://root:%s@localhost/pythondb' % parse.unquote_plus('P@ssw0rd')
engine = create_engine(engineString,echo = True)
connection = engine.connect()

#delete all from table
result = connection.execute("DELETE FROM cookies where 1")
# insert statement
#----------------------------------------------
ins = cookies.insert().values(
    cookie_name="insert statement",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)

# print(str(ins))
result = connection.execute(ins)
# insert function 
#----------------------------------------------
ins = insert(cookies).values(
    cookie_name="insert function",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC02",
    quantity="32",
    unit_cost="0.67"
)

# print(str(ins))
result = connection.execute(ins)


# insert multiple rows. 
#----------------------------------------------
ins = cookies.insert()
inventory_list = [
    {
    'cookie_name': 'peanut butter',
    'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
    'cookie_sku': 'PB01',
    'quantity': '24',
    'unit_cost': '0.25'
    },
    {
    'cookie_name': 'oatmeal raisin',
    'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
    'cookie_sku': 'EWW01',
    'quantity': '100',
    'unit_cost': '1.00'
    }
]
result = connection.execute(ins, inventory_list)