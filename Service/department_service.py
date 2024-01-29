import pyodbc
from Service import connection_service

con_string = connection_service.get_con_str()

#used to grab all of the department IDs from Department table
def get_depts():
    con = pyodbc.connect(con_string)

    departments = []
    results = con.execute('''
    SELECT * FROM department
    ''')

    for row in results:
        departments.append(row[0])
    con.close()
    return departments
