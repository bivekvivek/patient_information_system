import pymysql
conn = pymysql.connect('localhost','root','12345','cba')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE patient (pid int primary key auto_increment,name varchar(50),phone varchar(10), payment varchar(20),problem varchar(50),doctor varchar(100))""")
print("Table name %s created")