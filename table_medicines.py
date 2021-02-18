import pymysql
conn = pymysql.connect('localhost','root','12345','cba')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE medicine (med_id int primary key auto_increment,name varchar(50),chemical_compositions varchar(200), usages varchar(200))""")
print("Table created")