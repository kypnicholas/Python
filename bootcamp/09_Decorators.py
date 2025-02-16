
# DECORATORS
# Decorators can be thought of as functions which modify the functionality of another function. They help to make your code shorter and more "Pythonic".

# Functions within functions
def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

## Test
'''
hello()
# Notice that if I call the welcome() function outsie the hello() function it will fail 
welcome()  
'''

# Returning Functions
def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome

## Test 
'''
my_new_function = hello('Jose')
print(my_new_function())
'''

# Passing a function as an argument

def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

## Test 
'''
other(hello)
'''


# Creating a decorator

def new_decorator(original_func):

    def wrap_func():
        print("Extra code, BEFORE executing the original_func")

        original_func()

        print("Code here will execute AFTER the original_func")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

# Now re-assign the original function to the one with the decorator - to take advantage of the new functionality

func_needs_decorator = new_decorator(func_needs_decorator)

# Test
'''
func_needs_decorator()
'''

# NOW TO DO IT IN THE PYTHONIC WAY - WE USE THE @ SYMBOL.

@new_decorator                            # Now if you want to switch off the decorator you simply comment out this step without any risk to your code. 
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
