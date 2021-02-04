# ComIT Lecture 8

## Program Components

- **Lexicons** for writting correct words

- **Syntax** for writing valid sentences

- **Semantics** for interpretation to the sentences

Writing a program = coding | We are writing source code.

## Python Programming

Comments are ignored by the compiler, serving annotations that are useful for human.

- #Comment

- """Multi-line comment"""

Identifiers = symbolic name we give to a program element (variable, object, etc.)

- In Python, class names start with an uppercase letter. All other identifiers start with a lowercase letters. 

- Starting an identifier with a single leading underscore (_) means the identifier is *private*.

- Starting an identifier with two leading underscores (__) means the identifier is *strongly private*.

- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

Reserved words = pre-defined sequence of characters to specify what we want to do with the program: specific instructions (`if`, `while`, `for`), declarations (`class`, `def`), flow management (`continue`, `break`, `return`, `try`), and cannot be re-defined.

Lines & Indentation - Python uses indentation for flow control, provides no brace to indicate the block code.

Line continuation character (\) allows new lines of code
total = item_one + \
       item_two + \
       item_three

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is 
made up of many sentences."""

Escape character (\) tells program not to interpret.

some_random_string = "It is said \"hello\"."

There is no constant in Python, a variable can be used as constant instead and declased with UPPERCASE.

