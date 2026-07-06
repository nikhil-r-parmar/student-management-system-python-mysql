import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="school_db"
)

cursor = connection.cursor()

