import config
from util import DbUtil
import pymysql
from patient import Patients
from patient import Doctors
from patient import Reports
from patient import Tests
from patient import Medicines
class DbOperations:

    def add_patient(self, new):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into patient(pid,name, phone,payment,problem,doctor) values(%s,%s,%s,%s,%s,%s)", (new.pid,new.name, new.phone,new.payment,new.problem,new.doctor))
            connection.commit()
            print("Added")

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def add_doctor(self, new):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into doctor(did,name, phone,speciality,experience) values(%s,%s,%s,%s,%s)", (new.did,new.name, new.phone,new.speciality,new.experience))
            connection.commit()
            print("Added")

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def add_report(self, new):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into reports(report_id,patient, suggested_medicine,suggested_test) values(%s,%s,%s,%s)", (new.report_id,new.patient, new.suggested_medicine,new.suggested_test))
            connection.commit()
            print("Added")

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)
    def add_test(self, new):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into tests(test_id, name,description,doctor) values(%s,%s,%s,%s)", (new.test_id,new.name, new.description,new.doctor))
            connection.commit()
            print("Added")

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def add_medicine(self, new):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into medicine(med_id,name, chemical_compositions,usages) values(%s,%s,%s,%s)", (new.med_id,new.name, new.chemical_compositions,new.usages))
            connection.commit()
            print("Added")

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def get_1medicine(self,med_id):
        try:

            conn = DbUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("select  med_id,name, chemical_compositions,usages from medicine where med_id = %d", med_id)
            medicines = Contact(*cursor.fetchone())
            return  medicines
        except pymysql.DatabaseError as error:
            print("While getting data from DB using id... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(conn)
            DbUtil.close_cursor(cursor)

    def update_contact(self, contact):
        try:
            conn = DbUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("update contact set name = %s ,email = %s, mobile = %s where cid = %s", contact)
            conn.commit()

        except pymysql.DatabaseError as error:
            print("While updating ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(conn)
            DbUtil.close_cursor(cursor)

    def get_all_contacts(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name, phone,payment,problem,doctor from patient")
                rows = cursor.fetchall()
                contacts = self.get_list_data(rows)
                return contacts
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)
    def get_all_contacts(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name, phone,payment,problem,doctor from patient")
                rows = cursor.fetchall()
                contacts = self.get_list_data(rows)
                return contacts
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def get_medicine(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select med_id,name, chemical_compositions,usages from medicine")
                rows = cursor.fetchall()
                medicines = self.get_list_medicines(rows)
                return medicines
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def get_report(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select report_id, patient ,suggested_medicine,suggested_test from reports")
                rows = cursor.fetchall()
                reports = self.get_list_reports(rows)
                return reports
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)
    def get_tests(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select test_id,name, description,doctor from tests")
                rows = cursor.fetchall()
                tests = self.get_list_tests(rows)
                return tests
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def search_contact(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select cid, name, email, mobile from contact where name like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                contacts = self.get_list_data(rows)
                return contacts
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    @staticmethod
    def delete_contact(cid):
        try:
            connection = DbUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("delete from contact where cid = %s ", cid)
            connection.commit()

        except pymysql.DatabaseError as error:
            print("While deleting data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    @staticmethod
    def get_list_data(rows):
        return [Patients(*row) for row in rows]

    @staticmethod
    def get_list_doctors(rows):
        return [Doctors(*row) for row in rows]

    @staticmethod
    def get_list_reports(rows):
        return [Reports(*row) for row in rows]
    @staticmethod
    def get_list_tests(rows):
        return [Tests(*row) for row in rows]
    @staticmethod
    def get_list_medicines(rows):
        return [Medicines(*row) for row in rows]