import mysql.connector
import pandas as pd

db_con = mysql.connector.connect(host='localhost',
                                 database='sai',
                                 user='root',
                                 password='123456789')
query = """SELECT * FROM Persons"""
df = pd.read_sql(query, db_con)
print(type(df))
print(df)