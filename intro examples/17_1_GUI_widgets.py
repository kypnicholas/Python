
## Widgets are eventful python objects that have a representation in the browser, often as a control like a slider, textbox, etc.
# You can also use widgets to synchronize stateful and stateless information between Python and JavaScript.

import ipywidgets as widgets

from IPython.display import display
w = widgets.IntSlider()
display(w)

w.value                     # value of the slider 

w.close()

# Link two similar widgets together

a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))     # if you dont specify this line, the values of the widgets will be different.

# mylink.unlink()                                       # you can also unlink the two widgets



## For a complete list of the GUI widgets available to you, you can list the registered widget types. Widget is the base class.

import ipywidgets as widgets

# Show all available widgets!
for item in widgets.Widget.widget_types.items():
    print(item[0][2][:-5])