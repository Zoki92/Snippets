from sqlalchemy import create_engine, Column, Date, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///test1.sqlite")
Base = declarative_base()

class School(Base):
    __tablename__ = "woot"

    id = Column(Integer, primary_key = True)
    name = Column(String)


    def __init__(self, name):
        self.name = name


Base.metadata.create_all(engine)



s1 = School(name="MIT")
s2 = School(name="Harvard")
engine.execute("INSERT INTO 'woot' (name) VALUES ('HARVARD')")

results = engine.execute('SELECT * FROM woot')
print(results.fetchall())