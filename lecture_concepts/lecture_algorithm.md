# ComIT Lecture 1-7

#### Logic

Logic studies the thoughts that have to do with reasoning. Thoughts that are linked to reasoning express information about something or someone. For example, "John is taller than Peter", "The moon is made of cheese"; these can be true or false.

Boolean logic: computer thinks as 0 or 1.

#### Proposition

Sentence that describes a property about someone or something. It has precise words and a clear sense.
- Atomic ~ simpliest, e.g. tomorrow I'll be studying.
- Molecular ~ joined by link terms 
	- conjunction: John goes to the movies *and* Maria makes supper.
	- disjunction: John goes to the movies *or* Maria makes supper.
	- negation: Maria does *not* make supper.
	
#### Formalization

Every sentence has an underlying structure that shows how it articulates the information elements. The structure is extracted via a formalization process. The structure is also called a propositional form.

Formalization process: underdtand the meaning of the sentence --> identify atomic propositons --> identify connectives --> group into molecular propositions

Interpretation: "if I don't get paid, I won't go to work" --> write in logical structure: p -> q. Only p and q are variables having different values.

#### Truth Tables

A single proposition can be true or false. A molecular proposition can also be true or false, e.g., "it's morning and the window is opened".

#### Algorithms

Interlocutor = entity (person or object) that can understand a stated method and carry out (execute it), i.e., a computer.

Action = description of something that has to be done and chanegs the environment; can be primitive or non-primitive.

Algorithm = an ordered set or sequence of primitive actions oriented to solve problems. Steps can be broken down into modules of sub-steps.

Language = the one we talk with the interlocutor to describe the algorithms, e.g., human language to tell someone to change a flat tire.

Assumption = facts that are not written but are part of solution (can narrow scope), e.g., for changing the light bulb, it can be assumed that the electricity is off.

#### Data vs. Information in Programming

Data = symbolic representation of properties and features of an entity; for binary, it's true or false, 1 or 0. & is a value about something

Information = data + context

Program = instructions + data

Instruction = operation that can be performed by the machine to manipulate data --> order of instructions = "execution flow" 

#### Writing Programs

Computer program is not a natural language. Bohm-Jacopini theorem proves that any algorithm can be described with the three types of (building blocks) actions: sequence, selection or conditional, iteration or repetition of actions under certain conditions.

Sequence: assignment [<var> <- <expr>], input [read(x)], output [print "welcome"], invocation of another algorithm

Expression: combination of operands connected to operators, e.g. y = x + 2, x and 2 are operands, + is an operator

Relationship operators: <, <=, >, >=, ==, !=

Logical operators: AND, OR, NOT

Identifiers: variable name or declaration, word or name must begin with a letter or a "_" and then an arbitrary sequence of letters, numbers or an underscore.

Reserved words: sequence of characters defined with purpose specifying within the program, such as print, input, True, False, if, elif, def, var, Number, const

Nomenclature: writing style applied to sentences or compound words (good practice) such as lowerCamelCase, UpperCamelCase, UPPER_CASE

#### Modular Programming

Purpose of modular programming is to decompose a program into smaller parts called modules, or in pseudo code, called sub-algorthm.

algorithm <name> (<parameters>): <type>
	// data
	// actions
	return <expr>
end algorithm

To use or invoke a sub-algorithm ... call its name with (), e.g. insertName()

#### Variables' Scope

Two variables of different scopes are two different variables even if they are declared with the same name. Variables have to belong to a scope to be accessed.

#### Programming Languages

Processor = brain of the computer

Machine language works directly with instruction represented as binary number (0, 1), doesn't understand human language.

Assembly language represents instruction with symbols readable by humans, and is architecture dependent, still low-level language.

Assembler translates from assembly language to machine language for computer to understand. Changing hardware means re-writing program.

Hardware abstraction makes programs compatible with several hardware architectures. If hardware manufacturers (e.g. AMD and Intel) don't agree to make universal models, then need different solution; that is, to invent a new language independent from specific architectures and providing a translator to convert a high-level language.

Translator is programmed in assembly language; one translator per architecture. There can be different high level languages if there is at least one translator for the language.

Compiler = program that receives something in high-level language and translate to machine-readable language; turns source code to object code prior to running the program

Interpreter = program that receives source codes in high-level language and interpret on the run to execute; interpret one by one source code instructions

Source program = set of source codes (all the files) that conform a program

Object code = what is written by compiler as a result of compilation, in some languages such as C++ 

Executable program = file that contains the program to execute

Program written in C, is neither compiled to an assembly language nor write directly to the memory location, but to the operating system = intermediate layer between the code and the hardware

Python is dynamically typed (data type of variable can be changed) and interpreted. There is no compiler for Python.

#### Examples

At the terminal, run the command to execute python code.
```
$ python hello_world.py
Hello world!
$ python hello_world.txt
Hello from text.
```

Or at the root directory
```
~$ python Desktop/ComIT/django_learning/lecture_examples/hello_world.py
```

