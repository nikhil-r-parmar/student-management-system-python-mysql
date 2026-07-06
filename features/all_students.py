from database import connection, cursor
import mysql.connector

def view_all_students() :
    try :
        connection.commit()

        cursor.execute(
            "SELECT * FROM Students;"
        )
        students = cursor.fetchall()

        if not students :
            print("\nNo Students Data Available")

        else : 
            print("\nAll Students List: ")

            for student in students:
                print("\n==================")
                print("ID : ", student[0])
                print("Name : ", student[1])
                print("Age : ", student[2])
                print("City : ", student[3])
                print("==================")

    
    except mysql.connector.Error as e :
        print("Database Error: ", e)
        connection.rollback()
