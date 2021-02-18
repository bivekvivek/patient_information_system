import pymysql
conn = pymysql.connect('localhost','root','12345','cba')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE tests (test_id int primary key auto_increment,name varchar(50),description varchar(200), doctor varchar(200))""")
print("Table created")