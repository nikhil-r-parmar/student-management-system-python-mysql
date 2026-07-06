from database import connection, cursor
import mysql.connector

def add_student() :
    try :
        name = input("\nEnter Student Name: ").strip()
        if not name :
            print("\nName cannot be empty")
            return

        age = int(input("Enter Student age: "))
        if age < 0 or age > 120 :
            print("\nAge must be between 1 and 120")
            return
            
        city = input("Enter Student city: ").strip()
        if not city :
            print("\nCity cannot be empty")
            return

        cursor.execute(
            "INSERT INTO Students (name, age, city) VALUES (%s, %s, %s);", (name, age, city)
        )

        connection.commit()
        print("Student Added...")


    except ValueError :
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e :
        print("Database Error: ", e)
        connection.rollback()
