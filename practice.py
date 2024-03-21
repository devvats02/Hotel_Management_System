import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",passwd="devvats657@",database="practice")
my_cursor=conn.cursor

conn.commit()
conn.close()

print("success")