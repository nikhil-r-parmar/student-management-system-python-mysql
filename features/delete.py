from database import connection, cursor
import mysql.connector


def delete_student():
    try:
        id = int(input("\nEnter Student id that you wanted to delete: "))
        cursor.execute("SELECT * FROM Students WHERE id = %s;", (id, ))
        student = cursor.fetchone()

        if not student:
            print("\nSelected Student is not in the data.")

        else:
            cursor.fetchall()

            conformation = input("\nAre You Sure to delete? (Y/N): ")

            if conformation.lower() == 'y':
                cursor.execute(
                    "DELETE FROM Students WHERE id = %s;", (id, )
                )
                
                connection.commit()
                print("Student Deleted...")

            elif conformation.lower() == 'n':
                print("Okay...")

            else:
                print("Invalid choice, please try again...")

    except ValueError:
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e:
        print("Database Error: ", e)
        connection.rollback()
