import mysql.connector
import pandas as pd
from sqlalchemy import URL
from sqlalchemy import create_engine
query = """SELECT * FROM Persons"""

engine = create_engine("mysql+mysqldb://root:123456789@localhost:3306/sai")
df = pd.read_sql(query, engine)
print(df)
