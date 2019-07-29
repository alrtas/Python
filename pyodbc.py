

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="client",

)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM table_client_old ")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

#mostra todos os dados da tabela