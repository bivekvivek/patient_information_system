try:
    connection = DbUtil.get_connection()
    with connection.cursor() as cursor:
        pid = int(input("Enter name : "))
        name = str(input("Enter email: "))
        phone = str(input("Enter mobile : "))
        payment = str(input("Enter mobile : "))
        problem = str(input("Enter mobile : "))
        doctor = str(input("Enter mobile : "))
        cursor.execute("insert into patient(pid,name, phone,payment,problem,doctor) values(%s,%s,%s,%s,%s,%s)", (pid,name, phone,payment,problem,doctor))

    connection.commit()
    print(name,"Added")

except pymysql.MySQLError as error:
    print("While inserting Data ...")
    print('Exception number: {}, value {!r}'.format(error.args[0], error))
finally:
    DbUtil.close_connection(connection)
    DbUtil.close_cursor(cursor)
