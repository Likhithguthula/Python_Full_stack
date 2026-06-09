class Person:
    university_name = "CODEGNAN"

    def __init__(self, name, age, education_background, gender, department):
        self.name = name
        self.age = age
        self.education_background = education_background
        self.gender = gender
        self.department = department

    def display(self):
        print(f"University Name      : {Person.university_name}")
        print(f"Name                 : {self.name}")
        print(f"Age                  : {self.age}")
        print(f"Education Background : {self.education_background}")
        print(f"Gender               : {self.gender}")
        print(f"Department           : {self.department}")


class Student(Person):
    student_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, student_id, course, year):
        super().__init__(name, age, education_background, gender, department)
        self.student_id = student_id
        self.course = course
        self.year = year
        Student.student_count += 1

    def display_info(self):
        print("\n===== STUDENT DETAILS =====")
        self.display()
        print(f"Student ID           : {self.student_id}")
        print(f"Course               : {self.course}")
        print(f"Year                 : {self.year}")


class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, faculty_id, designation):
        super().__init__(name, age, education_background, gender, department)
        self.faculty_id = faculty_id
        self.designation = designation
        Faculty.faculty_count += 1

    def display_info(self):
        print("\n===== FACULTY DETAILS =====")
        self.display()
        print(f"Faculty ID           : {self.faculty_id}")
        print(f"Designation          : {self.designation}")


class Security(Person):
    security_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, security_id, shift):
        super().__init__(name, age, education_background, gender, department)
        self.security_id = security_id
        self.shift = shift
        Security.security_count += 1

    def display_info(self):
        print("\n===== SECURITY DETAILS =====")
        self.display()
        print(f"Security ID          : {self.security_id}")
        print(f"Shift                : {self.shift}")


class OfficeClerk(Person):
    clerk_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, clerk_id, section):
        super().__init__(name, age, education_background, gender, department)
        self.clerk_id = clerk_id
        self.section = section
        OfficeClerk.clerk_count += 1

    def display_info(self):
        print("\n===== OFFICE CLERK DETAILS =====")
        self.display()
        print(f"Clerk ID             : {self.clerk_id}")
        print(f"Section              : {self.section}")


class NonTeachingStaff(Person):
    staff_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, staff_id, role):
        super().__init__(name, age, education_background, gender, department)
        self.staff_id = staff_id
        self.role = role
        NonTeachingStaff.staff_count += 1

    def display_info(self):
        print("\n===== NON-TEACHING STAFF DETAILS =====")
        self.display()
        print(f"Staff ID             : {self.staff_id}")
        print(f"Role                 : {self.role}")


class OfficeStaff(Person):
    office_staff_count = 0

    def __init__(self, name, age, education_background, gender,
                 department, emp_id, responsibility):
        super().__init__(name, age, education_background, gender, department)
        self.emp_id = emp_id
        self.responsibility = responsibility
        OfficeStaff.office_staff_count += 1

    def display_info(self):
        print("\n===== OFFICE STAFF DETAILS =====")
        self.display()
        print(f"Employee ID          : {self.emp_id}")
        print(f"Responsibility       : {self.responsibility}")


# Students
s1 = Student("ABCD", 22, "Intermediate MPC", "Male",
             "CSE", "S101", "Python Full Stack", "4th Year")

# Faculty
f1 = Faculty("DEFG", 30, "M.Tech", "Male",
             "CSE", "F001", "Trainer")

# Security
sec1 = Security("PQRS", 45, "10th Pass", "Male",
                "Security", "SEC001", "Night Shift")

# Office Clerk
clerk1 = OfficeClerk("SUVW", 35, "B.Com", "Male",
                     "Administration", "CL001", "Admissions")

# Non-Teaching Staff
nts1 = NonTeachingStaff("KLMN", 40, "Degree", "Female",
                        "Maintenance", "NT001", "Lab Assistant")

# Office Staff
os1 = OfficeStaff("HIJK", 32, "MBA", "Female",
                  "Accounts", "OS001", "Fee Management")


# Display Information
s1.display_info()
f1.display_info()
sec1.display_info()
clerk1.display_info()
nts1.display_info()
os1.display_info()

# Counts
print("\n===== TOTAL COUNTS =====")
print("Students           :", Student.student_count)
print("Faculties          :", Faculty.faculty_count)
print("Security Staff     :", Security.security_count)
print("Office Clerks      :", OfficeClerk.clerk_count)
print("Non-Teaching Staff :", NonTeachingStaff.staff_count)
print("Office Staff       :", OfficeStaff.office_staff_count)
