from sqlalchemy import create_engine, Column, Date, Integer, String, Table, MetaData
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd


engine = create_engine("sqlite:///test1.sqlite")
Base = declarative_base()

class School(Base):
    __tablename__ = "woot"

    id = Column(Integer, primary_key = True)
    name = Column(String)


    def __init__(self, name):
        self.name = name


Base.metadata.create_all(engine)

connection = engine.connect()


s1 = School(name="MIT")
s2 = School(name="Harvard")
engine.execute("INSERT INTO woot (name) VALUES ('HARVARD')")

results = engine.execute('SELECT * FROM woot')
print(results.fetchall())


woot = Table('woot', Base.metadata, autoload=True, autoload_with=engine)

query = select([woot])
df = pd.DataFrame(connection.execute(query).fetchall())
print(df.head())


