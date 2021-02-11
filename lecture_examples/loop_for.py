# looping through a string
for letter in 'ComIT':
    print('Current Letter: {} {}'.format(letter, 'hi'))
    print(f'Current Letter: {letter}') # format string

strings = [f'Current Letter: {letter}' for letter in 'ComIT']
for string in strings:
    print(string)

result = [chr(ord(letter) + 2) for letter in 'ComIT'] # ord return unicode point for a one-character string
print(result)
result = [print(chr(ord(letter) + 2) for letter in 'ComIT')] # print doesn't return anything but 'None'
print(result)

# looping through a list
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print(f'Current Fruit: {fruit}')

# iterating a range of numbers (classic)
# similar to: for int i = 0; i < 10; i++
for index in range(len(fruits)):
    print(f'Current Fruit: {fruits[index]}')

class Example:
    def __str__(self):
        return "Hello I'm an example!"

example = Example()
print(f'This is the example object: {example} Isn\'t this great?') # preferred method to use string format
print('This is the example object: ' + str(example) + ' Isn\'t this great?')