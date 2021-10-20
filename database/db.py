import mysql.connector


con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='testing')

cursor = con.cursor()

query = "SELECT last_name, first_name FROM customers WHERE first_name=%s"
cursor.execute(query, ("Eric",))

for (lname, fname) in cursor:
    print(fname, lname)

cursor.close()
con.close()