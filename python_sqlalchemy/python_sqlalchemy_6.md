# A proper class for use with the ORM must do four things:
# • Inherit from the declarative_base object.
# • Contain __tablename__, which is the table name to be used in the database.
# • Contain one or more attributes that are Column objects.
# • Ensure one or more attributes make up a primary key


# we can use "Classical Mapping API" instead of using usual Declarative extension
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html

# refer to create raw mapper function
# https://codescience.wordpress.com/2011/06/19/python-data-access-layer/

