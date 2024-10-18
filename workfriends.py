# Initialize an empty list to store student details
students = []

def add_students():
    num_students = int(input("Enter the number of students to add: "))
    for _ in range(num_students):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        place = input("Enter student's place: ")
        admission_number = input("Enter student's admission number: ")
        # Append student details as a dictionary
        students.append({
            "name": name,
            "age": age,
            "place": place,
            "admission_number": admission_number
        })

def search_student():
    search_name = input("Enter the name of the student to search: ")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student found:", student)
            found = True
            break
    if not found:
        print("Student not found.")

def show_all_students():
    if not students:
        print("No students to show.")
    else:
        print("\nList of All Students:")
        for student in students:
            print(student)

def main():
    while True:
        print("\nOptions:")
        print("1. Add Students")
        print("2. Search for a Student")
        print("3. Show All Students")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_students()
        elif choice == '2':
            search_student()
        elif choice == '3':
            show_all_students()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
