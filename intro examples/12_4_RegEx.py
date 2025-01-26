

text = "The person's phone number is 408-555-1234"
print('phone' in text)                                      # Returns a boolean. 

### REGEX ### 
import re 

pattern = 'phone'
print(re.search(pattern,text))          # Indicates not only if there is a match but the start and end index of where it is found. 

match = re.search(pattern,text)         # python regex object which contains all the info we need. 
print(match)
print(match.span())
print(match.start())
print(match.end())
print(match.group())                    # groups (grabs) the actually string that matched

pattern = "NOT IN TEXT"
print(re.search(pattern,text))  


# Find ALL instances of a word 

# WITHOUT ITERATION
text = "my phone is a new phone"
match = re.search("phone",text)         # returns only the first instance

print(match)

# ITERATE 

matches = re.findall("phone",text)      # returns ALL instances
print(matches)

# To get actual match objects, use the iterator:

for match in re.finditer("phone",text):
    print(match.span())


## PATTERNS ## 

'''
Character	Description	        Example Pattern Code	Exammple Match
\d	        A digit	            file_\d\d	            file_25
\w	        Alphanumeric	    \w-\w\w\w	            A-b_1
\s	        White space	        a\sb\sc	                a b c
\D	        A non digit	        \D\D\D	                ABC
\W	        Non-alphanumeric	\W\W\W\W\W	            *-+=)
\S	        Non-whitespace	    \S\S\S\S	            Yoyo

Note: 'r' is in front of the string to indicate that it is not an escape slash (as is the case with strings, like \n for a new line etc...)
'''

import re

text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)

print(phone.group())


# QUANTIFIERS
# Allow you to write simpler code and indicate how many characters we are expecting (instead of writing \d twenty times for example)

'''
Character	Description	                Example Pattern Code	Exammple Match
+	        Occurs one or more times	Version \w-\w+	        Version A-b1_1
{3}	        Occurs exactly 3 times	    \D{3}	                abc
{2,4}	    Occurs 2 to 4 times	        \d{2,4}	                123
{3,}	    Occurs 3 or more	        \w{3,}	                anycharacters
\*	        Occurs zero or more times	A\*B\*C*	            AAACC
?	        Once or none	            plurals?	            plural
'''

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone.group())

## GROUPS
# Brackets() indicate grouping. It is useful when we want to use the results of the pattern matching for more than one purposes. 

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)

print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))


## ADDITIONAL SYNTAX

# Or operator |
re.search(r"man|woman","This man was here.")

# Wildcard character . 
re.findall(r".at","The cat in the hat sat here.")

# Starts with ^ -- # Starts with a number
re.findall(r'^\d','1 is the loneliest number.')

# Ends with $ -- Ends with a number
re.findall(r'\d$','This ends with a number 2')

# Exclusion: use the ^ symbol in conjunction with a set of brackets [].
phrase = "there are 3 numbers 34 inside 5 this sentence."
re.findall(r'[^\d]',phrase)

'''To get the words back together, use a + sign'''
re.findall(r'[^\d]+',phrase)

# Example: remove punctuation from a sentence.

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall('[^!.? ]+',test_phrase)
clean = ' '.join(re.findall('[^!.? ]+',test_phrase))
print(clean)


# Parenthesis for Multiple Options
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"

re.search(r'cat(fish|nap|claw)',text)
re.search(r'cat(fish|nap|claw)',texttwo)

