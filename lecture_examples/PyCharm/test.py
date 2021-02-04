print("Hello World!")

"""
To run this file in terminal,
(base): ~/Desktop/ComIT/django_learning/lecture_examples$ python PyCharm/test.py
Hello World!
"""

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is 
made up of several sentences."""
print(word + " " + sentence + " " + paragraph)

# \ is used as line continuation character, and as escape character
some_random_string = "Someone said 'hello'" + \
                     " and someone replied \"hello\"."
print(some_random_string)

# "is" check whether two variables point to the same object
print(word is sentence)
