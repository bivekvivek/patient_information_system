import pymysql
from beautifultable import BeautifulTable
from util import DbUtil
from contactservice import ContactService

class Other():
    def mysql_add_patient():
        cs = ContactService()
        cs.add_patient()
