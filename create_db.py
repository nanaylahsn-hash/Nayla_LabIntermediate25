import mysql.connector 

db = mysql.connector.connect (
    host = "local host" ,
    user = "root" ,
    password = "" , 
    port = 3306
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_mainan")

print =("Database toko_mainan berhasil dibuat")