
# COLLECITONS MODULE
# A built-in module that implements specialized container data types (alternatives to the basic: dict, list, set, and tuple.)

### COUNTER ###  
# A dict subclass which helps count hashable objects. 
# Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

from collections import Counter

# Counter() with lists
lst = [1,2,2,2,2,3,3,3,1,2,1,12,'a','b','b']

print(Counter(lst))

# Counter with strings

print(Counter('aabsbsbsbhshhbbsbs'))


# Common patterns when using the Counter() object

sentence = 'How many times does each word show up in this sentence word times each each word'

words = sentence.split()

print(Counter(words))

c = Counter(words)

print(c.most_common(2))         # returns the most common words in the sentence. 


### DEFAULTDICT ###
# returns a dictionary-like object.
# The functionality of both dictionaries and defaultdict is almost the same except for the fact that defaultdict never raises a KeyError. 
# It provides a default value for the key that does not exist.

from collections import defaultdict

# Normal dictionary
d = {}
d['WrongKey']  # this will throw a keyError as the key I requested does not exist (my dictionary is empty). 

# defaultdict

d = defaultdict(lambda: 0)      # I define my defaultdict and whatever keys we are missing are initialized to 0 (zero). 

print(d['WrongKey'])




### NAMEDTUPLE ### 

# The standard tuple uses numerical indexes to access its members, for example:

t = (12,13,14)
print(t[0]) 


# For simple use cases, this is usually enough. 
# However, this can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. 
# A namedtuple assigns names, as well as the numerical index, to each member.

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")

print(sam.age)
print(sam[0])

