#Students CLI(Command - Line Interface) Tool
#Date : 04 / 07 / 2026
#Author : Nikhil R.Parmar

from features.add_students import add_student
from features.all_students import view_all_students
from features.delete import delete_student
from features.search import search_student
from features.update_name import update_name
from features.update_age import update_age
from features.update_city import update_city
from database import connection, cursor


def update_students_data(): 
    print("\n---------------")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update City")
    print("4. Exit Program")
    print("---------------")
    try: 
        choice = int(input("Enter Your choice(1-4): "))

        if choice == 1: 
            update_name()
        elif choice == 2: 
            update_age()
        elif choice == 3: 
            update_city()
        elif choice == 4: 
            print("\nProgram exited...") 
            return False
        else: 
            print("\nInvalid Choice, Please try again...")
    except ValueError: 
        print("\nPlease Enter a valid input as asked...")


while True: 
    print("\n=======================") 
    print("() Student CLI Tool") 
    print("=======================") 
    print("1. Add Student") 
    print("2. View All Students") 
    print("3. Search Student") 
    print("4. Update Student Data") 
    print("5. Delete Student") 
    print("6. Exit Program") 
    print("-----------------------")

    try: 
        choice = int(input("Enter Your choice(1-6): "))

        if choice == 1: 
            add_student()
        elif choice == 2: 
            view_all_students()
        elif choice == 3: 
            search_student()
        elif choice == 4: 
            if update_students_data() == False: 
                break
        elif choice == 5: 
            delete_student()
        elif choice == 6: 
            print("\nProgram exited...") 
            break
        else: 
            print("\nInvalid Choice, Please try again...")
    except ValueError: 
        print("\nPlease Enter a valid input as asked...")

cursor.close() 
connection.close()
