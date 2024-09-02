## SYNTAX ##
#  try:
#    You do your operations here...
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
# else:
#    If there is no exception then execute this block. 
# 
# finally: 
#   This block of code will always be run regardless if there was an exception

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))   
        except:                                                         # This will check for any exception and then execute this print statement
        # except UnboundLocalError:                                     # This will check only for an UnboundLocalError exception 
            print("Looks like you did not enter an integer!")

        else:
            print("Yep that's an integer!")
            print(val)
            break

        finally:
            print("End of error handling!")


askint()

# Exercise 1
try: 
    for i in ['a','b','c']:
        print(i**2)
except: 
    print("An error occurred")


# Exercise 2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')

# Exercise 3

def ask():
    while True: 
        try: 
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
    print('Thank you, your number squared is: ',n**2)

ask()