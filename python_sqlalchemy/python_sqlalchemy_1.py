# Connecting to database. 
# The create_engine function returns an instance of an engine; however, it does not actually open a connection until an action is called that would require a connection, such as a query.
from sqlalchemy import create_engine
# engine = create_engine('sqlite:///cookies.db')
engine2 = create_engine('sqlite:///:memory:')
# engine3 = create_engine('sqlite:////home/cookiemonster/cookies.db')
# engine4 = create_engine('sqlite:///c:\\Users\\cookiemonster\\cookies.db')

print('create engine in memory success!')

