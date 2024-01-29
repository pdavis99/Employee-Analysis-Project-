import pyodbc
from Service import connection_service

con_string = connection_service.get_con_str()

#grabs all employee IDs from Employee table
def get_employees():
    con = pyodbc.connect(con_string)

    employees = []
    results = con.execute('SELECT employeeid FROM employee')
    for row in results:
        employees.append(row[0])

    con.close()
    return employees

#used to grab the newly-added employees without an income
def get_employ_no_income():
    con = pyodbc.connect(con_string)

    employees = []
    results = con.execute('SELECT e.employeeid FROM employee e JOIN income i ON e.employeeid = i.employeeid WHERE i.pay IS NULL')
    for row in results:
        employees.append(row[0])

    con.close()
    return employees