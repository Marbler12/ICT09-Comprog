#Course Enrollment System

class Course:
    def __init__(self, course_id, name, year_level, section):
        self.course_id = course_id
        self.name = name
        self.year_level = year_level
        self.section = section
        self.enrolled_students = []

    def course_details(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Name: {self.name}\n"
            f"Year Level: {self.year_level}\n"
            f"Section: {self.section}\n"
            f"Enrolled Students: {len(self.enrolled_students)}\n"
        )


class EnrollmentSystem:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("Available Courses:")
            for course in self.courses:
                print(f"- {course.name} (ID: {course.course_id})")

    def search_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None


enrollment_system = EnrollmentSystem()

while True:
    print("\nCourse Enrollment Menu:")
    print("1. Add New Course")
    print("2. Enroll a Student in a Course")
    print("3. Display All Courses")
    print("4. Display Students in a Specific Course")
    print("5. Exit")
    print()
    choice = input("Enter choice: ")
    print()

    # Add New Course
    if choice == "1":
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")

        while True:
            try:
                year_level = int(input("Enter Year Level : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            section = input("Enter Section: ").upper()
            if len(section) == 1 and section.isalpha():
                break
            else:
                print("Invalid input. Please enter a single letter.")

        new_course = Course(course_id, name, year_level, section)
        enrollment_system.add_course(new_course)
        print("New course added.")

    # Enroll a Student in a Course
    elif choice == "2":
        course_id = input("Enter Course ID: ")
        course = enrollment_system.search_course(course_id)
        if course:
            student_name = input("Enter Student Name: ")
            course.enrolled_students.append(student_name)
            print(f"Student {student_name} enrolled in {course.name}.")
        else:
            print("Course not found.")

    # Display All Courses
    elif choice == "3":
        enrollment_system.display_courses()

    # Display Students in a Specific Course
    elif choice == "4":
        course_id = input("Enter Course ID: ")
        course = enrollment_system.search_course(course_id)
        if course:
            if not course.enrolled_students:
                print(f"No students enrolled in {course.name}.")
            else:
                print(f"Students Enrolled in {course.name}:")
                for student in course.enrolled_students:
                    print(f"- {student}")
        else:
            print("Course not found.")

    # Exit Program
    elif choice == "5":
        print("Exiting Course Enrollment System.")
        break

    else:
        print("Invalid choice. Try again.")
