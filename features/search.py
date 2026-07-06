from database import connection, cursor
import mysql.connector

def search_student() :

    try :
        id = int(input("\nEnter Student id you wanted to search: "))
        
        cursor.execute(
            "SELECT * FROM Students WHERE id= %s", (id, )
        )
        student = cursor.fetchone()

        if not student :
            print("\nSearched Student is not in database.") 

        else :
            print("\n==================")
            print("ID : ", student[0])
            print("Name : ", student[1])
            print("Age : ", student[2])
            print("City : ", student[3])
            print("==================")

    except ValueError :
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e :
        print("Database Error: ", e)