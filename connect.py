import mysql.connector 

db = mysql.connector.connect (
    host = "local host" ,
    user = "root" ,
    password = "" , 
    port = 3306
)

if db.is_connect():
    print("Berhasil connect ke database")