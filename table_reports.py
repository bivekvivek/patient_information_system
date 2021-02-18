import pymysql
conn = pymysql.connect('localhost','root','12345','cba')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE reports (report_id int primary key auto_increment,patient varchar(50),suggested_medicine varchar(200), suggested_test varchar(200))""")
print("Table created")