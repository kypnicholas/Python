
## The Button is not used to represent a data type. 
# Instead the button widget is used to handle mouse clicks. 
# The on_click method of the Button can be used to register a function to be called when the button is clicked.

import ipywidgets as widgets

# on_click
from IPython.display import display
button = widgets.Button(description="Click Me!")
display(button)

def on_button_clicked(b):
    print("Button clicked.")

button.on_click(on_button_clicked)

# on_submit // The on_submit event fires when the user hits enter.
text = widgets.Text()
display(text)

def handle_submit(sender):
    print(text.value)

text.on_submit(handle_submit)





import traitlets
# Create Caption
caption = widgets.Label(value = 'The values of slider1 and slider2 are synchronized')

# Create IntSliders
slider1 = widgets.IntSlider(description='Slider 1')
slider2 =  widgets.IntSlider(description='Slider 2')

# Use trailets to link
l = traitlets.link((slider1, 'value'), (slider2, 'value'))
display(caption, slider1, slider2)



# Create Caption
caption = widgets.Label(value='Changes in source values are reflected in target1')

# Create Sliders
source = widgets.IntSlider(description='Source')
target1 = widgets.IntSlider(description='Target 1')

# Use dlink
dl = traitlets.dlink((source, 'value'), (target1, 'value'))
display(caption, source, target1)

l.unlink()
dl.unlink()
