# ComIT Lecture 8-16

Note: to create a new virtual environment, run the command `python -m venv .venv` through Virtual Studio Code.

## Program Components

- **Lexicons** for writting correct words

- **Syntax** for writing valid sentences

- **Semantics** for interpretation to the sentences

Writing a program = coding | We are writing source code.

## Python Programming

Comments are ignored by the compiler, serving annotations that are useful for human.

- `#Comment`

- `"""Multi-line comment"""`

Identifiers = symbolic name we give to a program element (variable, object, etc.)

- In Python, class names start with an uppercase letter. All other identifiers start with a lowercase letters. 

- Starting an identifier with a single leading underscore (_) means the identifier is *private*.

- Starting an identifier with two leading underscores (__) means the identifier is *strongly private*.

- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

Reserved words = pre-defined sequence of characters to specify what we want to do with the program: specific instructions (`if`, `while`, `for`), declarations (`class`, `def`), flow management (`continue`, `break`, `return`, `try`), and cannot be re-defined.

Lines & Indentation - Python uses indentation for flow control, provides no brace to indicate the block code.

Line continuation character (\) allows new lines of code.
```
total = item_one + \
       item_two + \
       item_three
```

Quotation marks ("") to declare words, sentences, and paragraphs.
```
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is 
made up of many sentences."""
```

Escape character (\) tells program not to interpret.
```
random_string = "It is said \"hello\"."
```

There is no constant in Python, a variable can be used as constant instead and declased with UPPERCASE.

## Python Data Types

**Primitive** data type = indivisible value element (atomic): numeric, logic, characters.

- Primitive data type **variables** store **values** that represent data.

- Primitive data type **collections**: list, dictionary

**Classes**

- Objects: from the data prespective, an object is a **composite** data type.

- Class type **variables** store values which is a **reference** to an object of the class, i.e., reference variables.

## Sequence or Expression Statements

Sequence = direct operation to be performed by Python, i.e., a line of code that has to result in the other line of code.

Four types: assignment, invoke functions or methods, object creation, `Null` (empty line)

**Assignment**: `<itentifier var> = <expr>`

- Assign a value to a variable `dog.name = input("Enter dog's name: ")`

- Create a variable `emp1 = "Zara"`

**Method invocation**: `<identifier var or object>,<identifier method>(<arguments>)`

- Invoke an object or class method `dog.play_fetch(input("Throw something! "))` for the declared method `def play_fetch(self, item): print(self.name + " caught " item)`; in this case, arguments are `dog`/`self` and the input `item`.

**Construction**: `<class type> (<arguments>)`

- Create an object returning a reference, using a constructor `emp1 = Employee("Zara", 2000)`; use *positional parameters* following the order of the arguments i.e. Zara is mapped to name and 2000 is mapped to salary. Another way to construct is `emp2 = Employee(salary=3000, name="Sally")`

- Call a *constructor* with the same name as the class' name, but define an *initializer* using `__init__` method.

- Note: there is only one initializer (cannot overload with different arguments); use `**kwargs` dictionary instead. Or, to work around, give the default value(s) as `None`.

```
class Employee:
	def __init__(self, name=None, salary=None):
		self.name = name
		self.salary = salary
```

## Block and Scope

Each block helps define a scope. We tabulate to the right on each new block.

- Class definition

- Method definition

- Control flow structure (if, else, while and for define a scope)

## Object-oriented Programming

*State* of an object = all the object's attribute's current values.

`print(<var>)` prints the contents of a variable. Generally, it prints `__main__.Employee object at xxxxxx` unless specify `__str__` method.

```
class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary	

	def __str__(self: 'Employee') -> str:
		return f'Name: {self.name}, Salary: {self.salary}'
	
	def get_state(self):
		return f'Name: {self.name}, Salary: {self.salary}'

	def display(self):
		print(f'Name: {self.name}, Salary: {self.salary}')
```

*Instance* of an object = a reference or pointer to a memory allocation.

- Note: `name` is a parameter and a local variable; but `self.name` is an attribute of an object, which stays with the instance of the object.

```
class Employee:
	employee_count = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary	
		Employee.employee_count += 1

	def increase_salary(self, how_much):
		self.salary += how_much
		print(self.salary)
```

*Special variables* of an instance can be accessed: `print(employee_instance.__dict__['salary']` is equivalent to `print(employee_instance.salary)`. Thus, all members can be accessed in Python.

## Access Modifiers

- public: members that can be accessed anywhere

- protected(_): members that should be accessed within the same package or module

- private(__): members that should be accessed inside their class, 
e.g. `employee_instance.__name = "Sandra"` is outside the scope and should not be used; however,
`self.__name = "Bob"` inside the class definition is okay.

*Encapsulation* = a concept of hiding details of the implementation of private methods or parameters. Example: Nobody know how `print()` works internally; it is encapsulated. Encapsulating involves exposing the interface.

*Interface* = part of the object that is visible to the rest of the objects, i.e., the set of visible members of an object allowing user to operate

`@staticmethod` above the declaration of method is to access the method without the instance of the class.

```
@staticmethod
def get_employee_count():
	return Employee.__employee_count
```

In the example, the `get_employee_count()` class method is a part of public interface of the `Employee` class to access the private `__employee_count` attribute.

