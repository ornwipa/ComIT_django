def insertNameAndGreeting():
    name = input("Enter name: ")
    print("Hello " + name)

def insertRadiusAndShowArea():
    radius = float(input("Enter radius: "))
    PI = 3.1416
    print(radius*radius*PI)

def simple():
    insertNameAndGreeting()
    insertRadiusAndShowArea()

if __name__ == "__main__":
    simple()

    print(__doc__)
    print(__file__)
    print(__name__)
    print(__package__)