import pyodbc
from faker import Faker
from Service import connection_service,employee_service
import pandas as pd

con_string = connection_service.get_con_str()

#used to generate random contacts for each employee
def random_contact_gen():
    con = pyodbc.connect(con_string)

    faker = Faker()

    employees = employee_service.get_employ_no_income()

    for employee in employees:
        contact = []
        address = faker.street_address()
        phone = faker.phone_number()
        fake_city = faker.city()
        fake_state = faker.state()
        zip = faker.zipcode()

        con.execute(f"INSERT INTO contact(state, city, contactnumber, employeeid, address, zipcode) VALUES('{fake_state}','{fake_city}','{phone}','{employee}','{address}','{zip}')")

    con.commit()
#used to clean up each phone number from the generated contact list
def cleaned_random_contacts():
    con = pyodbc.connect(con_string)

    results = con.execute("SELECT * FROM contact")

    for row in results:
        old_phone = row.contactnumber
        cleaned_phone = old_phone.replace('-', '').replace('.', '').replace('(','').replace(')',"")
        new_phone = "-".join([cleaned_phone[:3], cleaned_phone[3:6], cleaned_phone[6:]])

        con.execute(f"UPDATE contact SET contactnumber = '{new_phone}' WHERE contactnumber = '{cleaned_phone}'")

    con.commit()
    con.close()