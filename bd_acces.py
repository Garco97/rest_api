import mysql.connector as mysql
class BdAcces:
    def __init__(self):
        # enter your server IP address/domain name
        self.HOST = "sql7.freemysqlhosting.net" # or "domain.com"
        # database name, if you want just to connect to MySQL server, leave it empty
        self.DATABASE = "sql7358025"
        # this is the user you create
        self.USER = "sql7358025"
        # user password
        self.PASSWORD = "BWmhDXBKyj"
        # connect to MySQL server
        self.connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)  
    def get(self, table):
        query = f"SELECT * FROM {table}"
        cursor = connection.cursor()
        cursor.execute(query)
        return query
    def insert(self, table, *values):
        query = f"INSERT INTO {table} VALUES {values}"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return query
    def exit(self):
        self.connection.close()