import sqlalchemy
from sqlalchemy import create_engine

# print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:MeghaArya@localhost/ScotlandYard?charset=utf8mb4")

with engine.connect() as conn:
  result=conn.execute(text("select * from Players"))
  print(result.all())