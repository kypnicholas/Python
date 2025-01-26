# CHECK PERFORMANCE OF YOUR CODE

# We will create two functions that do the same thing and check which one is more efficient. 

'''
Given a number n, returns a list of string integers
['0','1','2',...'n]
'''

import time 

def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))

print(func_two(10))

## OPTION ONE: Get the start and end time and calculate the elapsed time

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Get end time
end_time = time.time() 
# Step 4: Calculate total time elapsed
elapsed_time = end_time - start_time

print(elapsed_time)



## OPTION TWO: Timeit Module 
'''
MORE PRECISE
The timeit module takes in two STRINGS, a statement (stmt) and a setup. 
It then runs the setup code and runs the stmt code some n number of times and reports back average length of time it took.
'''

import timeit

# remember your functions are passed in as strings

stmt = 'func_one(100)'
setup = '''                         
def func_one(n):
    return [str(num) for num in range(n)]
'''

timeit.timeit(stmt,setup,number=100000)

stmt2 = 'func_two(100)'
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

timeit.timeit(stmt2,setup2,number=100000)
