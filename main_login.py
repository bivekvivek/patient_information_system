import pymysql
from beautifultable import BeautifulTable
from util import DbUtil
from hospital import Hospital
from patient import Patients
from patient import Reports
from patient import Tests
from patient import Medicines

with open("patient.txt","r") as file:
    patlist = [line.strip() for line in file]
with open("patient.txt","r") as file:
    doclist = [line.strip() for line in file]

def mysql_add_patient():
    cs = Hospital()
    cs.add_patient()

def mysql_add_doctor():
    cs = Hospital()
    cs.add_doctor()

def mysql_add_report():
    cs = Hospital()
    cs.add_report()

def mysql_add_test():
    cs = Hospital()
    cs.add_test()

def mysql_add_medicine():
    cs = Hospital()
    cs.add_medicine()

def patient_login():
    patlog = str(input("Enter Username : "))
    patr = list(patlist)
    patr.remove("")
    if patlog in patr:
        patient()
    else:
        print("First Go And Register!!")

def doctor_login():
    doclog = str(input("Enter Username : "))
    dr = list(patlist)
    dr.remove("")
    if doclog in dr:
        doctor()
    else:
        print("First Go And Register!!")

def patient():
    for i in range(1,100):
        print("******************")
        print("+  1:Reports   +")
        print("+  2:Medicines +")
        print("+  3:Tests     +")
        print("+  4:Doctors   +")
        print("+  5:Back      +")
        print("******************")
        choice = int(input('Enter your choice:'))
        if (choice == 1):
            print("I")
        elif (choice == 2):
            print("I")
        elif (choice == 3):
            print("Created By Bivek")
        elif (choice == 4):
            break
        else:
            print("Disconnecting from database...")
            break

def doctor():
    for i in range(1,100):
        print("***************************")
        print("+   1:See Patient List    +")
        print("+   2:Create Report       +")
        print("+   3:Test Applied        +")
        print("+   4:Back                +")
        print("***************************")
        choice = int(input('Enter your choice:'))
        if (choice == 1):
            print("I")
        elif (choice == 2):
            print("I")
        elif (choice == 3):
            print("Created By Bivek")
        else:
            print("Disconnecting from database...")
            break

def add_patient():
    with open("patient.txt","a") as file:
        pt = str(input("Enter username for login\n"))
        file.writelines(f'\n{pt}')
    mysql_add_patient()


def add_doctor():
    with open("doctor.txt","a") as file:
        dk = str(input("Enter username for login\n"))
        file.writelines(f'\n{dk}')
    mysql_add_doctor()

def others():
    for i in range(1,100):
        print("********************************")
        print("+ 1:Add Patient 3:Edit Patient +")
        print("+ 2:Add Doctor  4:Edit Doctor  +")
        print("+ 5:Medicines list             +")
        print("+ 6:Test List 7:Back           +")
        print("********************************")
        choice = int(input('Enter your choice:'))
        if (choice == 1):
            add_patient()
        elif (choice == 2):
            mysql_add_doctor()
        elif (choice == 3):
            mysql_add_medicine()
        elif (choice == 4):
            mysql_add_medicine()
        elif (choice == 5):
            mysql_add_medicine()
        else:
            print("Disconnecting from database...")
            break

for i in range(1,100):
    print("******LOG-IN*******")
    print("+   1:Patient    +")
    print("+   2:Doctor     +")
    print("+   3:Others     +")
    print("+   4:Exit       +")
    print("********************")
    choice = int(input('Enter your choice:'))
    if (choice == 1):
        patient_login()
    elif (choice == 2):
        doctor_login()
    elif (choice == 3):
        others()
    else:
        print("Disconnecting from database...")
        break