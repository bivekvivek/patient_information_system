import pymysql
conn = pymysql.connect('localhost','root','12345','cba')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE doctor (did int primary key auto_increment,name varchar(50),phone varchar(10), speciality varchar(20),experience varchar(100))""")
print("Table name %s created")