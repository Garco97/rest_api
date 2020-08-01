import mysql.connector as mysql
# enter your server IP address/domain name
HOST = "sql7.freemysqlhosting.net" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "sql7358025"
# this is the user you create
USER = "sql7358025"
# user password
PASSWORD = "BWmhDXBKyj"
# connect to MySQL server
connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", connection.get_server_info())


query = input()
while(query != ""):
    
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if "insert" in query:
            connection.commit()
        else:
            for i in cursor.fetchall():
                print(i)
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        query = input()
        cursor.close()
    except mysql.Error as err:
        print("Something went wrong: {}".format(err))
        break

connection.close()