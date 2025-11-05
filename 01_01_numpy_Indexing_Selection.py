
import numpy as np

arr = np.arange(0,11)
print(arr)

print(arr[2])       # Accessing an element at an index in the array
print(arr[0:5])     # Accessing a range of elements in the array


# 
# BROADCASTING 
# how NumPy treats arrays with different shapes during arithmetic operations. 
# Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.
# 
# Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python. 
# It does this without making needless copies of data and usually leads to efficient algorithm implementations. 
# There are, however, cases where broadcasting is a bad idea because it leads to inefficient use of memory that slows computation.  
#

arr = np.arange(0,11)
print(arr)

slice_of_arr = arr[0:6]         # IMPORTANT. When grabbing the slice of an array remember you are viewing part of the original array. So if you broadcast, you will affect the original array
print(slice_of_arr)

slice_of_arr[:] = 99            # Changing the values in the slice_of_arr will also change the values in the original array
print(slice_of_arr)
print(arr)

# If you do not want to affect the original array, you need to make a COPY of the array
arr = np.arange(0,11)       # Re-creating the array
print(arr)
arr_copy = arr.copy()
arr_copy[:] = 100            # Changing the values in the arr_copy will not affect the original array
print(arr_copy)



# Indexing a 2D array (matrix) # 

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

print(arr_2d[1])            # Accessing a row
print(arr_2d[1][2])         # Accessing an element in a row
print(arr_2d[1,2])          # Accessing the same element in a row as above

print(arr_2d[:,2])          # Accessing a column
print(arr_2d[2, :])          # Accessing a row
print(arr_2d[2, :2])         # Accessing a range of elements in a row


# SELECTION # 
arr = np.arange(1,11)
print(arr)

bool_arr = arr > 5        # Creating a boolean array
print(bool_arr)

print(arr[bool_arr])      # Using the boolean array to select elements in the original array where the condition is TRUE    
print(arr[arr > 5])       # Doing the same thing in one line. MOST COMMON WAY TO DO THIS. 




