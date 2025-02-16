
# Rounding Numbers

import math 

value = 4.35

print(math.floor(value))
print(math.ceil(value))

# Mathematical Constants
print(math.pi)

print(math.e)

# Logarithmic values 
print(math.log(math.e))


''' 
math.log(x,base)
--> what number do I need to take the base to the power of, to return x
(i.e. 10^2 = 100)
'''
print(math.log(100,10))


## RANDOM ## 
## By default the random number generator uses the current system time.

import random

print(random.randint(0,100))

# SEED # 

'''
The seed() method is used to initialize the random number generator.
The random number generator needs a number to start with (a seed value), to be able to generate a random number.

Use the seed() method to customize the start number of the random number generator.
If you use the same seed value twice you will get the same random number twice. See example below
'''

random.seed(10)
print(random.random())


# Random with Sequences
# Grab a random item from a list

a = list(range(0,20))
print(a)
print(random.choices(population=a,k=10))         # choice() - Sample with Replacement
print(random.sample(population=a,k=10))          # sample() - Sample without Replacement


# Shuffle
a = list(range(0,20))
random.shuffle(a)
print(a)
