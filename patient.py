from collections import namedtuple

Patients = namedtuple("Patients", ["pid","name", "phone", "payment","problem","doctor"])
Reports = namedtuple("Reports", ["report_id","patient","suggested_medicine","suggested_test"])
Doctors = namedtuple("Doctors", ["did","name", "phone","speciality","experience"])
Medicines = namedtuple("Medicines", ["med_id","name", "chemical_compositions","usages"])
Tests = namedtuple("Tests", ["test_id","name", "description","doctor"])