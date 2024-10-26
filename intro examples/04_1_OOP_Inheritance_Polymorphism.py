## INHERITANCE ## 
# A way to form new classes using classes that have already been defined. 
# The newly formed classes are called derived classes, the classes that we derive from are called base classes. 
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

class Animal:                           # BASE CLASS
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):                      # DERIVED CLASS
    def __init__(self):
        Animal.__init__(self)           # Create an instance of the Animal class
        print("Dog created")

    def whoAmI(self):                     # Overwrite base class method
        print("Dog")

    def bark(self):
        print("Woof!")

myDog = Dog()
print(myDog)
print(myDog.whoAmI())




## POLYMORPHISM ## 
# The same function name is being used for different types. 
# Each function is differentiated based on its data type and number of arguments.
# It is common practice to use abstract classes and inheritance

class Animal:                                       # ABSTRACT CLASS is one that never expects to be instantiated. Used as a Base class. 
    def __init__(self, name):    
        self.name = name

    def speak(self):              
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
maggie = Dog('Maggie')
felix = Cat('Felix')

#print(maggie.speak())
#print(felix.speak())


# Notice that the .speak() method is called both from the Dog and Cat classes. 
# When called, each object's .speak() method returns a result unique to the object.

for pet in [maggie,felix]:
    print(pet.speak())
