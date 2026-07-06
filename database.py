import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_database_password",
    database="school_db"
)

cursor = connection.cursor()

