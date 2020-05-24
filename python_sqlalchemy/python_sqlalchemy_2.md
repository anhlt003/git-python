# SQL Expression Language (SEL) provided by SQLAlchemy Core
# we can insert single or multiple row. 
# using insert statement or insert function.
# INSERT SEL
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
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
        cookie_name="dark chocolate",
        cookie_recipe_url="http://some.aweso.me/cookie/darkchoco.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
    )

    # print(str(ins))
    result = connection.execute(ins)
    # insert function 
    #----------------------------------------------
    ins = insert(cookies).values(
        cookie_name="white chocolate",
        cookie_recipe_url="http://some.aweso.me/cookie/whitechoco.html",
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


# --------------------------------------------------------------------------------
# RESULT PROXY SEL/ SELECT SEL
# --------------------------------------------------------------------------------
#     -> select([object.c.<column_name1>, object.c.<column_name_2> ])
#     -> first(): return the first record of results in connection.execute()
#     -> fetchone(): Returns one row, and leaves the cursor open
#     -> scalar(): Returns a single value if a query results in a single record with one column

# Controlling the Columns in the Query:
#     -> object.c.<column-name>
# Ordering: 
#     -> result.order_by(object.c.<column-name>)
# Limiting:
#     -> result.limit(<n>)   
# Built-in function in SEL: 
#     ->  <func_name>_<position>
#     ->  record = result.first()
#     ->  record.count_1 
# Filtering 
#     -> .where(condition)
# ClauseElements
# Operators
# Operators
# Boolean Operators
# Conjunctions

# --------------------------------------------------------------------------------
# RESULT PROXY SEL/ INSERT/DELETE/JOIN/ALIASES/GROUP/CHAINING SEL
# --------------------------------------------------------------------------------
#       -> rs= Update(<objects>).where(filter_condition)
#       -> rs= rs.value(<set_condition>) 
#       -> Delete(<object>).where(del_condition)
    # Querying data.
    from sqlalchemy import create_engine
    from sqlalchemy import select 
    from urllib import parse
    from python_sqlalchemy_1 import cookies

    engineString = 'mysql+pymysql://root:%s@localhost/pythondb' % parse.unquote_plus('P@ssw0rd')
    engine = create_engine(engineString,echo = True)
    connection = engine.connect()

    s = cookies.select()
    rs = connection.execute(s)
    results = rs.fetchall()         
    firstrow = results[0]
    print('This is first row data : ',firstrow)
    print('#################################')

    s = cookies.select()
    rs = connection.execute(s)
    print("This is list name of cookies: ")
    for record in rs: 
        print(record.cookie_name)

    connection.close()
    #TBD: Will define other SEL after/ just refer basic infomation.// Using storeprocedure insteadly
    # study learn SEL: 
    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_functions.htm
# --------------------------------------------------------------------------------
# RAW QUERY AND STOREPROCEDURE in SqlAlchemy
# --------------------------------------------------------------------------------
# https://docs.sqlalchemy.org/en/13/core/connections.html
# There are some cases when SQLAlchemy does not provide a genericized way at access some DBAPI functions, like support storeprocedure -> we new use DBAPI connection directly. It's called raw_connection. 
# When use raw_connection / we need catch exception by module pymysql.

    from sqlalchemy import create_engine
    from sqlalchemy import select 
    from urllib import parse
    from python_sqlalchemy_1 import cookies
    import pprint

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
        args = [45]
        cursor = dbapi_connection.cursor()
        cursor.callproc('SP_GET_FROM_COOKIES_BY_ID', args)
        results_second = list(cursor.fetchall())
        print('KQ raw call proc query : ')
        printer.pprint(results_second)
        cursor.close()    

    finally: 
        dbapi_connection.close()


