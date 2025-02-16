## CLASS ## 
# The class is a blueprint that defines the nature of a future object. 
# From classes we can construct instances. 
# An instance is a specific object created from a particular class. 

## ATTRIBUTE ## 
# A characteristic of an object.
# We can have specific attributes to an instance of the class - i.e. Dog.Name = Maggie or Loulou etc. 
# OR we can have class object attributes which are same for any instance of the class - i.e. Dog.Species = "Mammal" 

## METHODS ## 
# Methods are functions that are defined inside of a class! 

class Dog():

    # Class object attribute - same for any instance of the class 
    species = 'mammal'

    def __init__(self,breed,name):               # this is the CONSTRUCTOR method and it is called automatically right after the object has been created.
        self.breed = breed                       # Attributes are defined inside the constructor method.
        self.name = name                        

    def bark(self,food):
        print("Woof! My name is " + self.name + " and my favourite food is " + food)


myDog = Dog(breed='Mixed breed',name='Maggie')

print(myDog.breed, myDog.name,myDog.species)           # Note we don't have parentheses, because it is an attribute and doesn't take any arguments.
print(myDog.bark("cheese"))




class Circle():
    # Class object attribute
    pi = 3.14

    # Constructor method 
    def __init__(self, radius=1):       # Instantiate the circle with a radius of 1
        self.radius = radius

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle()

print("My default circle circumference is: " + str(my_circle.getCircumference()))

my_circle = Circle(10)                  # You can overwrite the default value of the attribut
print("My new circle's circumference is: " + str(my_circle.getCircumference()))
