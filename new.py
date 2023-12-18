import mysql.connector
import pandas as pd
from sqlalchemy import URL
from sqlalchemy import create_engine
'''db_con = mysql.connector.connect(host='localhost',
                                 database='sai',
                                 user='root',
                                 password='123456789')

query = """SELECT * FROM Persons"""
df = pd.read_sql(query, db_con)
print(type(df))
print(df)'''
query = """SELECT * FROM Persons"""

engine = create_engine("mysql+mysqldb://root:123456789@localhost:3306/sai")
df = pd.read_sql(query, engine)
print(df)
