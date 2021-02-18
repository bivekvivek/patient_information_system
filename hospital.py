from dboperations import DbOperations
from patient import Patients
from patient import Doctors
from patient import Reports
from patient import Tests
from patient import Medicines
from beautifultable import BeautifulTable

class Hospital:

    def __init__(self):
        self.cs = DbOperations()

    def add_patient(self):
        pid = int(input("Enter Patient ID : "))
        name = str(input("Enter Patient Name : "))
        phone = str(input("Enter Patient's Phone No. : "))
        payment = str(input("Enter Patient's Payment Method : "))
        problem = str(input("Enter Patient's Problem : "))
        doctor = str(input("Enter Doctor's Name For Appointment : "))
        contact = Patients(pid,name, phone,payment,problem,doctor)
        self.cs.add_patient(contact)
        self.show_all_contacts()

    def add_doctor(self):
        did = int(input("Enter Doctor's ID : "))
        name = str(input("Enter Doctor's Name : "))
        phone = str(input("Enter Doctor's Phone Number : "))
        speciality = str(input("Enter Doctor's Speciality : "))
        experience = str(input("Enter Doctor's Experience(in yr) : "))
        contact = Doctors(did,name,phone,speciality,experience)
        self.cs.add_doctor(contact)
        self.show_all_doctors()

    def add_report(self):
        report_id = int(input("Enter Doctor's ID : "))
        patient = str(input("Enter Doctor's Name : "))
        suggested_medicine = str(input("Enter Doctor's Phone Number : "))
        suggested_test = str(input("Enter Doctor's Speciality : "))
        report = Reports(report_id,patient,suggested_medicine,suggested_test)
        self.cs.add_report(report)
        self.show_report()

    def add_medicine(self):
        med_id = int(input("Enter Doctor's ID : "))
        name = str(input("Enter Doctor's Name : "))
        chemical_compositions = str(input("Enter Doctor's Phone Number : "))
        usages = str(input("Enter Doctor's Speciality : "))
        medicine = Medicines(med_id,name,chemical_compositions,usages)
        self.cs.add_medicine(medicine)
        self.show_medicine()

    def add_test(self):
        test_id = int(input("Enter Doctor's ID : "))
        name = str(input("Enter Doctor's Name : "))
        description = str(input("Enter Doctor's Phone Number : "))
        doctor = str(input("Enter Doctor's Speciality : "))
        test = Tests(test_id,name,description,doctor)
        self.cs.add_test(test)
        self.show_test()

    def show_all_contacts(self):
        contacts = self.cs.get_all_contacts()
        Hospital.paint_data_list(contacts)

    def show_all_doctors(self):
        contacts = self.cs.get_all_doctors()
        Hospital.paint_data_doctors(contacts)

    def show_report(self):
        report = self.cs.get_report()
        Hospital.paint_data_report(report)

    def show_test(self):
        test = self.cs.get_tests()
        Hospital.paint_data_tests(test)
    def show_medicine(self):
        medicine = self.cs.get_medicine()
        Hospital.paint_data_medicine(medicine)

    def search_contact(self):
        name = input("Enter search name :")
        contacts = self.cs.search_contact(name)
        if contacts:
            Hospital.paint_data_list(contacts)
        else:
            print("No data found with search name :{}".format(name))

    @staticmethod
    def paint_data_list(data):
        table = BeautifulTable()
        table.column_headers = ["PID", "NAME", "PHONE", "PAYMENT","PROBLEM","DOCTOR"]
        for li in data:
            table.append_row([li.pid, li.name, li.phone, li.payment,li.problem,li.doctor])
        print(table)

    @staticmethod
    def paint_data_doctors(data):
        table = BeautifulTable()
        table.column_headers = ["DID", "NAME", "PHONE", "SPECIALITY","EXPERIENCE"]
        for li in data:
            table.append_row([li.did, li.name, li.phone, li.speciality,li.experience,])
        print(table)

    @staticmethod
    def paint_data_report(data):
        table = BeautifulTable()
        table.column_headers = ["REPORT_ID", "PATIENT", "SUGGESTED_MEDICINE", "SUGGESTED_TEST"]
        for li in data:
            table.append_row([li.report_id, li.patient, li.suggested_medicine, li.suggested_test,])
        print(table)

    @staticmethod
    def paint_data_tests(data):
        table = BeautifulTable()
        table.column_headers = ["TEST_ID", "NAME", "DESCRIPTION", "DOCTOR"]
        for li in data:
            table.append_row([li.test_id, li.name, li.description, li.doctor,])
        print(table)

    @staticmethod
    def paint_data_medicine(data):
        table = BeautifulTable()
        table.column_headers = ["MED_ID", "NAME", "CHEMICAL_COMPOSITIONS", "USAGES",]
        for li in data:
            table.append_row([li.med_id, li.name, li.chemical_compositions, li.usages])
        print(table)



