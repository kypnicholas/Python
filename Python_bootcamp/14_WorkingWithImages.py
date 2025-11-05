from PIL import Image

pencils = Image.open('c:/Users/nkypri01/Downloads/MyPythonExercises/14_WorkingWithImages/pencils.jpg')

pencils.show()                          # Open the image externally
print(pencils.size)                     # (width, height in pixels)
print(pencils.filename)           
print(pencils.format_description)

## CROP ## 
''' 
The crop() method returns a rectangular sub-section of an image. 
All the coordinates of box (x, y, w, h) are measured from the top left corner of the image. 
'''

# Start at top corner (0,0)
x = 0
y = 0
w = 1950/3          # Grab about 30% in x direction
h = 1300/10         # Grab about 10% in y direction

pencils.crop((x,y,w,h)).show()


## COPY AND PASTE ## 

from PIL import Image

mac = Image.open('c:/Users/nkypri01/Downloads/MyPythonExercises/14_WorkingWithImages/example.jpg')

mac.size
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
# mac.crop((x,y,w,h)).show()

computer = mac.crop((x,y,w,h))

mac.paste(im=computer,box=(0,0))

mac.show()


## RESIZING ## 

new_mac = mac.resize((3000,500))        # create a new instance of the image

new_mac.show()

## ROTATE ## 

new_mac.rotate(90).show()           # specify the amount of degrees to rotate. The original dimensions will be kept and "filled" in with black.
new_mac.rotate(90,expand=True)      # fill the new rotated image to the old dimensions.


## TRANSPARENCY ## 
'''
We can add an alpha value (RGBA stands for RED,Green,Blue, Alpha) where values can go from 0 to 255. 
If Alpha is 0 the image is completely transparent, if it is 255 then its completely opaque.
'''

from PIL import Image

red_color = Image.open('c:/Users/nkypri01/Downloads/MyPythonExercises/14_WorkingWithImages/red_color.jpg')

red_color.putalpha(18)
red_color.show()

## SAVE AS A NEW IMAGE ## 

red_color.save('c:/Users/nkypri01/Downloads/MyPythonExercises/14_WorkingWithImages/light_red.png')
light_red = Image.open('c:/Users/nkypri01/Downloads/MyPythonExercises/14_WorkingWithImages/light_red.png')

light_red.show()