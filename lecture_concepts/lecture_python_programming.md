# ComIT Lecture 8-11

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

**Primitive** data type = indivisible value element (atomic): numeric, logic, characters

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

- Create an object returning a reference, using a constructor `emp1 = Employee("Zara", 2000)`

- Note: there is only one constructor (cannot overload with different arguments); use `**kwargs` dictionary instead.

## Block and Scopes

Each block helps define a scope. We tabulate to the right on each new block.

- Class definition

- Method definition

- Control flow structure (if, else, while and for define a scope)

