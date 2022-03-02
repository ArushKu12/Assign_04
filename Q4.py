#Making a class of employee

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_number=roll_no
    def information(self):
        print(f"Name of student is {self.name}")
        print(f"Roll no of {self.name} is {self.roll_number}")
    def __del__(self):
        print(f"{self.name} record has been deleted ")
# object is created
student_1=Student(name="Anmol gupta",roll_no=21103114)

student_2=Student(name="Aman Choudhary",roll_no=21103118)

student_3=Student(name="Pratyaksh mahajan",roll_no=21103116)


student_1.information()
print()
student_2.information()
print()

student_3.information()
print()
# using destructor

del student_1

del student_2

del student_3