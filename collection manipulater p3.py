print("=" * 40)
print("       collection manipulater")
print("=" * 40)




student_records = []


subjects_offered = set()



def add_student():
    print("\n========== Add Student ==========")

    try:
        
        student_id = int(input("Student ID: "))

        
        for student in student_records:
            if student["personal_info"][0] == student_id:
                print("Student ID already exists!")
                return

        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")

       
        dob = input("Date of Birth (YYYY-MM-DD): ")
        personal_info = (student_id, dob)

        
        subject_input = input("Subjects (comma-separated): ")

        
        subjects = [
            subject.strip()
            for subject in subject_input.split(",")
            if subject.strip()
        ]

        
        student = {
            "personal_info": personal_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        
        student_records.append(student)

        
        subjects_offered.update(subjects)

        print("\nStudent added successfully!")

    except ValueError:
        print("Invalid input! Student ID and Age must be numbers.")



def display_all_students():
    print("\n========== All Students ==========")

    if len(student_records) == 0:
        print("No student records found.")
        return

    for student in student_records:

        student_id = student["personal_info"][0]
        dob = student["personal_info"][1]

        print("\n----------------------------------")
        print(f"Student ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Grade      : {student['grade']}")
        print(f"DOB        : {dob}")
        print(f"Subjects   : {', '.join(student['subjects'])}")
        print("----------------------------------")



def update_student():
    print("\n========== Update Student ==========")

    try:
        student_id = int(input("Enter Student ID to update: "))

        for student in student_records:

            if student["personal_info"][0] == student_id:

                print("\nStudent Found!")
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Grade")
                print("4. Update Subjects")
                print("5. Back")

                choice = input("Enter your choice: ")

                if choice == "1":
                    student["name"] = input("Enter new name: ")
                    print("Name updated successfully!")

                elif choice == "2":
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated successfully!")

                elif choice == "3":
                    student["grade"] = input("Enter new grade: ")
                    print("Grade updated successfully!")

                elif choice == "4":
                    subject_input = input(
                        "Enter new subjects (comma-separated): "
                    )

                    new_subjects = [
                        subject.strip()
                        for subject in subject_input.split(",")
                        if subject.strip()
                    ]

                    # List is mutable, so we can modify it
                    student["subjects"] = new_subjects

                    # Update unique subjects Set
                    subjects_offered.update(new_subjects)

                    print("Subjects updated successfully!")

                elif choice == "5":
                    return

                else:
                    print("Invalid choice!")

                return

        print("Student ID not found.")

    except ValueError:
        print("Invalid input! Student ID and Age must be numbers.")



def delete_student():
    print("\n========== Delete Student ==========")

    try:
        student_id = int(input("Enter Student ID to delete: "))

        for index, student in enumerate(student_records):

            if student["personal_info"][0] == student_id:

                # del keyword used as required
                del student_records[index]

                print("Student deleted successfully!")
                return

        print("Student ID not found.")

    except ValueError:
        print("Invalid Student ID!")



def display_subjects():
    print("\n========== Subjects Offered ==========")

    if len(subjects_offered) == 0:
        print("No subjects available.")
        return

    print("Unique Subjects:")

    for subject in sorted(subjects_offered):
        print(f"- {subject}")



def main():

    print("\n==========================================")
    print(" Welcome to the Student Data Organizer!")
    print("==========================================")

    while True:

        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_subjects()

        elif choice == "6":
            print("\n==========================================")
            print("Thank you for using Student Data Organizer!")
            print("Goodbye!")
            print("==========================================")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()
