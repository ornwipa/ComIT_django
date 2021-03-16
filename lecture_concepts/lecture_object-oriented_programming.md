# ComIT Lecture on Inheritance

The term "interitance" refers to how methods and attributes are "passed down" from one class definition to another, making it easier to create and maintain a complex applications, allowing user to reuse codes.

Attributes and methods defined in a parent `Person` class will be defined in child `Student(Person)` class.

```
class Person:
	def __init__(self, fname, lname):
		self.first_name = fname
		self.last_name = lname
		
	def print_name(self):
		print(f"{self.first_name} {self.last_name}")

class Student(Person):
	pass

student = Student("Joel", "Hill")
student.print_name()
```

A class can be inherited from several other classes such as `class Teacher(Student, Employee)`.

See the example on how to build a new (or modify) initializer by using `**kwargs`, i.e. the dictionary or wildcard placeholder of key word arguments, in the initializer of super class and `super().__init__(**kwargs)`, i.e. to keep looking for other class.

```
class Person:
	def __init__(self, fname, lname, **kwargs):
		self.first_name = fname
		self.last_name = lname
        	super().__init__(**kwargs)
```

Note: every class method defitions need `self` as attributes, e.g. `def print_name(self)`.

