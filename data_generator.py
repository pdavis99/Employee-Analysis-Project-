import pyodbc
from faker import Faker
from Service import employee_service, department_service,connection_service

con_string = connection_service.get_con_str()

#used to generate a random list of employees for the Employee table
def random_list():
    con = pyodbc.connect(con_string)

    faker = Faker()
    departments = department_service.get_depts()

    for i in range():
        first_name = faker.first_name()
        last_name = faker.last_name()
        dept_id =  faker.random.choice(departments)
        sql = f'''
        INSERT INTO employee(
        firstname,
        lastname,
        departmentid
        )
        VALUES ('{first_name}','{last_name}','{dept_id}')
        '''
        con.execute(sql)
    con.commit()
    con.close()





