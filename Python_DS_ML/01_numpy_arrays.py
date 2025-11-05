

import numpy as np

my_list = [1,2,3]
print(my_list)

my_array = [1,2,3,4]
my_array = np.array(my_array)
print(my_array)


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix = np.array(my_matrix)
print(my_matrix)

## BUILT-IN METHODS ## 

my_array = np.arange(0,10)  # Return evenly spaced values within a given interval.
print(my_array)

my_array = np.arange(0,11,2)
print(my_array)

my_array = np.linspace(0,1,10)  # Return evenly spaced numbers over a specified interval.
print(my_array)

my_array = np.eye(4)  # Create an IDENTITY MATRIX. Return a 2-D array with ones on the diagonal and zeros elsewhere.
print(my_array)

my_array = np.zeros(3)  # Return a new array of given shape and type, filled with zeros.
print(my_array)

my_array = np.ones((3,3))  # Return a new matrix of given shape and type, filled with ones.
print(my_array)

my_array = np.full((2,2), 7)  # Return a new array of given shape and type, filled with a specified value.
print(my_array)


# 
# RANDOM METHODS 
# rand() Return random values in a given shape, from a uniform distribution over [0, 1).
# randn() Return a sample (or samples) from the “standard normal” distribution.
# randint() Return random integers from low (inclusive) to high (exclusive).
# 

my_array = np.random.rand(2)
print(my_array)

my_array = np.random.randn(2,2)
print(my_array)

my_array = np.random.randint(1,10,10)  
print(my_array)


## ARRAY ATTRIBUTES ##
arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

arr = arr.reshape(5,5)
print(arr)

print(arr.shape)    # Return a tuple of array dimensions.
print(arr.dtype)    # Return the data type of the array.

print(ranarr.max())  # Return the maximum value of the array.
print(ranarr.min())  # Return the minimum value of the array.

print(ranarr.mean())  # Return the average value of the array.  
print(ranarr.argmax())  # Return the index of the maximum value.


# linspace() Return evenly spaced numbers over a specified interval.
arr = np.linspace(0,1,20)
print(arr)