class Person:

    def __init__(self, fname, lname, *args, **kwargs):
        self.first_name = fname
        self.last_name = lname
        super().__init__(*args, **kwargs)
    
    def print_name(self):
        print(f"{self.first_name} {self.last_name}")

class Student(Person):
	pass

class Employee(object):

    def __init__(self, id, employer):
        self.id = id
        self.employer = employer
    
    def print_employer(self):
        print(f"Employer: {self.employer}")

class Teacher(Student, Employee):

    def print_name(self):
        super().print_name()
        print(" is a teacher.")

teacher = Teacher(fname="Jack", lname="Black", id="007", employer="M16")
teacher.print_name()
teacher.print_employer()
