
## REMEMBER TO RUN IN INTERACTIVE WINDOW ## 

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def f(x):
    return x

interact(f, x=10,);                                     # Integers generate a slider to interact with
interact(f, x=True);                                    # Booleans generate check-boxes
interact(f, x='Hi there!');                             # Strings generate text areas
interact(f, x=['option1', 'option2', 'option3']);       # Lists generate dropdowns


## interact can also be used as a decorator. This allows you to define a function and interact with it in a single shot.
## With the use of a DECORATOR (=functions which modify the functionality of other functions.)
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


## Pass a 3-tuple of integers (min,max,step size) // if you don't specify step size, it has a default of 1. 

@interact(x=(-10,10,0.1))
def h(x):
    return x



## interactive - In addition to interact, IPython provides interactive
# allows to reuse the widgets that are produced or access the data that is bound to the UI controls.

from IPython.display import display

# the following function allows us to two integers with a visual representation
def f(a, b):
    display(a + b)
    return a+b

w = interactive(f, a=10, b=20)
display(w)
