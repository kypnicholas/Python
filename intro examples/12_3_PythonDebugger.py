'''
Python's built in debugger (pdb) is an interactive debugging environment. 
It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, 
so you can understand what your program actually does and find bugs in the logic.
'''

import pdb 

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)