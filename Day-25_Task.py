import re
class UserValidation:
    def validate(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile Number: ")
        password = input("Enter Password: ")
        name_pattern = re.fullmatch(r"[A-Za-z ]{3,}", name)
        email_pattern = re.fullmatch(r"[a-zA-Z0-9._]+@gmail\.com", email)
        mobile_pattern = re.fullmatch(r"[6-9][0-9]{9}", mobile)
        password_pattern = re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}",password)
        if name_pattern:
            print(" Valid Name")
        else:
            print(" Invalid Name")

        if email_pattern:
            print(" Valid Email")
        else:
            print(" Invalid Email")

        if mobile_pattern:
            print(" Valid Mobile Number")
        else:
            print(" Invalid Mobile Number")

        if password_pattern:
            print(" Valid Password")
        else:
            print(" Invalid Password")
obj = UserValidation()
obj.validate()
