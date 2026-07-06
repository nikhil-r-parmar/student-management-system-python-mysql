from database import connection, cursor
import mysql.connector

def update_city():

    try:
        id = int(input("\nEnter id of that student: "))
        cursor.execute("SELECT * FROM Students WHERE id = %s;", (id, ))

        if not cursor.fetchone():
            print("\nSelected Student is not in the data.")

        else:

            cursor.fetchall()

            city = input("Enter New City You want to update: ").strip()
            
            if not city :
                print("\nCity cannot be empty")
            else :
                cursor.execute(
                    "UPDATE Students SET city = %s WHERE id = %s;", (city, id)
                )

                connection.commit()
                print("Student City Updated...")


            

    except ValueError:
        print("\nPlease Enter a valid input as asked...")

    except mysql.connector.Error as e:
        print("Database Error: ", e)
        connection.rollback()
