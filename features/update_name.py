from database import connection, cursor
import mysql.connector


def update_name():

    try:
        id = int(input("\nEnter id of that student: "))
        cursor.execute("SELECT * FROM Students WHERE id = %s;", (id, ))

        if not cursor.fetchone():
            print("\nSelected Student is not in the data.")

        else:

            cursor.fetchall()

            name = input("Enter New Name You want to update: ").strip()

            if not name :
                print("\nName cannot be empty")
            else :
                cursor.execute(
                    "UPDATE Students SET name = %s WHERE id = %s;", (name, id)
                )

                connection.commit()
                print("Student Name Updated...")

    except ValueError:
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e:
        print("Database Error: ", e)
        connection.rollback()
