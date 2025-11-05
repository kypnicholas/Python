
import numpy as np

arr = np.arange(1,11)
print(arr)

# Adding, subtracting, multiplying two arrays, element by element.
print(arr + arr)     
print(arr - arr)
print(arr * arr)    

# Scalar operations on an array. Broadcasts a single number 
print(arr + 100)


# Universal Array Functions (UFUNC functions)
print(np.sqrt(arr))         # Square root of each element in the array
print(np.exp(arr))          # Exponential of each element in the array