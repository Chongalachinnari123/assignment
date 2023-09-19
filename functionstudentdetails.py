#write a program to enter student deatials and also view the stored student details 
 # Initialize an empty dictionary to store student details
student_data = {}

def add_student():
    # Get student details from the user
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    # Create a dictionary to store the student's information
    student_info = {
        'Name': name,
        'Roll Number': roll_number,
        'Age': age,
        'Grade': grade
    }

    # Add the student information to the student_data dictionary
    student_data[roll_number] = student_info
    print("Student details added successfully!")

def view_students():
    # Check if there are any students in the dictionary
    if not student_data:
        print("No student records found.")
    else:
        print("Student Details:")
        for roll_number, student_info in student_data.items():
            print(f"Roll Number: {roll_number}")
            for key, value in student_info.items():
                print(f"{key}: {value}")
            print("")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3).")
