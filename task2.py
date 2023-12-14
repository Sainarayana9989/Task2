
import mysql.connector
import pandas as pd
db_con = mysql.connector.connect(host='localhost',
                                 database='sai',
                                 user='root',
                                 password='123456789')

cursor = db_con.cursor( )


sql = "select * from Persons where Salary=(select max(Salary) from Persons);" #these sql query prints highest salary and his details
#sql="select * from Persons"

cursor.execute(sql)

data=cursor.fetchall()
#print(data)
for i in data:
    #print(data)
    df = pd.DataFrame(data,columns=['person_id','last_name','first_name','city','salary'])
print(df)
print(type(df))

