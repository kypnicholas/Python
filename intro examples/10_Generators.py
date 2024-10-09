
# GENERATORS
# Generators allow us to generate as we go along, instead of holding everything in memory.
# We can construct our own Generators with the yield statement.

# When a generator function is compiled, they become an object thats supports an iteration protocol. 
# Best for calculating large sets of results in cases where we don’t want to allocate the memory for all of the results at the same time.

# For example, the range() function doesn't produce a list in memory from start to stop. 
# Instead, it keeps track of the last number and the step size, to provide a flow of numbers. 
# If the used does need the list, they need to cast the generator to a list 
# list(range(0,10))

# produce the list in memory    -- NOT EFFICIENT. What if n = 1,000,000
def create_cubes(n):
    result = []
    for x in range(n): 
        result.append(x**3)
    return result

# Test
'''
for x in create_cubes(10):
    print(x)
'''

# Generator function for the cube of numbers (power of 3)   -- MUCH MORE MEMORY EFFICIENT
def gencubes(n):
    for x in range(n):
        yield x**3

# Test
'''
for x in create_cubes(10):
    print(x)
'''


# Another example of the generator using the range() function

# Fibonacci - normal function
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output

# Test
'''
fibon(10)
'''

# Fibonacci - GENERATOR
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

# Test
'''
for num in genfibon(10):
    print(num)
'''


# next() built-in function

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()

# Test
'''
print(next(g))
print(next(g))
print(next(g))

'''

# iter() function
s = 'hello'

# Test
'''
for letter in s:
    print(letter)
'''

# you can also loop through the string using the built-in iter() generator function 
s_iter = iter(s)

# Test
'''
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
'''