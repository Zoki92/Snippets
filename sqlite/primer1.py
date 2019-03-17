from sqlalchemy import (create_engine, Table, 
                        Column, Integer, String, 
                        MetaData, ForeignKey)

from sqlalchemy.sql import select



engine = create_engine("sqlite:///testdb.sqlite")
metadata = MetaData()

users = Table('users', metadata, 
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('fullname', String),
            )

addresses = Table('addresses', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('users.id')),
                Column('email_address', String, nullable=False),
                )

metadata.create_all(engine)



# ins = users.insert().values(name="jack", fullname="Jack Jones")
connection = engine.connect()
# result = connection.execute(ins)
# add = addresses.insert().values(user_id=1, email_address="jack@jones.com")
# connection.execute(add)





