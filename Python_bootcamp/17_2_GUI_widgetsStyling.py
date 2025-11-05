

import ipywidgets as widgets

b1 = widgets.Button(description='Ordinary Button', button_style='')

b2 = widgets.Button(description='Danger Button', button_style='danger')

display(b1,b2)

b3 = widgets.Button(description='Custom color')
b3.style.button_color = 'lightgreen'

display(b1,b2,b3)