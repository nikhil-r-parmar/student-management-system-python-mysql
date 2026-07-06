from database import connection, cursor
import mysql.connector

def update_age():

    try:
        id = int(input("\nEnter id of that student: "))
        cursor.execute("SELECT * FROM Students WHERE id = %s;", (id, ))

        if not cursor.fetchone():
            print("\nSelected Student is not in the data.")

        else:

            cursor.fetchall()

            age = int(input("Enter New Age You want to update: "))

            if age < 0 or age > 120 :
                cursor.execute(
                    "UPDATE Students SET age = %s WHERE id = %s;", (age, id)
                )

                connection.commit()
                print("Student Age Updated...")

            else :
                print("Age must be between 1 and 120")

    except ValueError:
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e:
        print("Database Error: ", e)
        connection.rollback()
