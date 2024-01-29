import os

#connects to PostgresSql Server
def get_con_str():
    driver = 'DRIVER={PostgreSQL ODBC Driver(ANSI)};'
    server = 'Server=localhost;'
    database = 'Database=business;'
    port = 'Port=5432;'
    user = f"UID={os.getenv('PostgresUser')};"
    password = f"PWD={os.getenv('PostgresPass')};"

    con_string = f'{driver}{server}{database}{port}{user}{password}'
    return con_string