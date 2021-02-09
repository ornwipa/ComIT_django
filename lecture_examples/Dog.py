from random import randint

class Dog:
    def __init__(self, name): # not a constuctor, but method that initialize an instant
        self.id = str(randint(0, 999))
        self.name = name
    
    def __str__(self):
       return self.name

    def display(self):
        print("The dog name is " + self.name)

    def play_fetch(self, item):
        print(self.name + " caught the " + item)

while True:
    dog = Dog("Sparky") # use a constructor
    print(dog)
    dog.name = input("Give a dog name: ")
    dog.display()
    dog.play_fetch(input("Throw something! "))

    # dog.best_friend = Dog("Sleepy")
    # dog.best_friend.name = "Mimo"
    # dog.best_friend.play_fetch("ball")

    keep_going = input("Keep going? (y/n)")
    
    if keep_going == "n":
        break