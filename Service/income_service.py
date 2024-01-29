import pyodbc
from faker import Faker
from Service import employee_service, connection_service

con_string = connection_service.get_con_str()

#used to generate random salaries for the set employees in our database
def random_salary_gen():
    con = pyodbc.connect(con_string)

    faker = Faker()

    employees = employee_service.get_employ_no_income()

    payscale = range(30000, 200000)

    for employee in employees:
        pay = faker.random.choice(payscale)
        con.execute(f"INSERT INTO income(employeeid, pay) VALUES ('{employee}','{pay}')")
    con.commit()
    con.close()