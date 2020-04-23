

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="client",

)


mycursor = mydb.cursor()
mycursor.execute("SELECT telefone FROM table_client_old ")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

#mostra todos os dados da tabela


sql = "SELECT * FROM table_client_old WHERE telefone = 8409829376.0"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

#search for a specific number, then brings all the data from this row


sql1 = "SELECT * FROM table_client_old  WHERE nome  LIKE 'Mi%'"
mycursor.execute(sql1)
myresult = mycursor.fetchall()
for result1 in myresult:
    print(result1)



sql2 = "SELECT * FROM table_client_old WHERE nome = %s"

mycursor.execute(sql2,("Thiago",))
myresult = mycursor.fetchall()
for result2 in myresult:
    print(result2)

