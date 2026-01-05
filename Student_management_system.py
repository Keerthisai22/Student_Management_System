students={}
def add_student():
    roll=int(input("Enter the roll number="))
    name=input("Enter the name=")
    marks=int(input("Enter the marks="))
    students[roll]={"Name":name,"Marks":marks}
    print("Student added successfully.")
def update_student():
    roll=int(input("Enter the roll number="))
    if roll in students:
        marks=int(input("Enter the marks="))
        students[roll]["Marks"]=marks
        print("Marks updated successfully")
    else:
        print("Student not found")
def delete_student():
    roll=int(input("Enter the roll number="))
    if roll in students:
        del students[roll]
        print("Deleted successfully.")
    else:
        print("Student not found")
def view_student():
    if not students:
        print("Students not found")
    else:
        for roll,data in students.items():
            print("Roll:",roll,"Name:",data["Name"],"Marks:",data["Marks"])
def menu():
    while True:
        print("\n======================STUDENT MANAGEMENT SYSTEM===========================\n")
        print("1.Add student")
        print("2.Update student")
        print("3.View students")
        print("4.Delete student")
        print("5.Exit")
        choice=int(input("Enter the choice="))
        if choice==1:
            add_student()
        elif choice==2:
            update_student()
        elif choice==3:
            view_student()
        elif choice==4:
            delete_student()
        elif choice==5:
            print("Thank you!")
            break
        else:
            print("Invalid choice")
menu()
    
    
        
    
