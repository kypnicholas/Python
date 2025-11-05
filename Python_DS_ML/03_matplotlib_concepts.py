
# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
# It provides an object-oriented API for embedding plots into applications that use general-purpose GUI toolkits, such as Tkinter, wxPython, Qt, or GTK.

# Import the `matplotlib.pyplot` module under the name `plt` (the tidy way):
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

print(x)
print(y)


## You can create Matplot libplots in TWO ways: FUNCTIONAL and OBJECT-ORIENTED.

## 1. FUNCTIONAL way: 
plt.plot(x, y, 'r')                     # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
#plt.show()                              # Show the plot when using an IDE. Not needed in Jupyter Notebook.

# Creating Multiplots on Same Canvas

# plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x, y, 'r--')       # 'r--' is the color red with dashed lines
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-');      # 'g*-' is the color green with star markers and solid lines
#plt.show()                              


## 2. OBJECT-ORIENTED way:

## METHOD A: PLT.FIGURE() 
fig = plt.figure()                              # Create a figure object. Empty canvas.
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])       # INDICATE DISTANCE FROM THE LEFT AND BOTTOM OF THE FIGURE AND THE WIDTH AND HEIGH.(L,B,W,H)(range 0 to 1)

# Plot on that set of axes
axes.plot(x, y, 'b')
axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
#plt.show()                              

# Creating Multiplots on Same Canvas. Multiple figures on the same canvas.
fig = plt.figure()                              
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])      # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])      # inserted axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');

plt.show()



## METHOD B: PLT.SUBPLOT()
## SUBPLOTS:  Create a grid of subplots in a single figure. 
# The subplots() function is an AXIS MANAGER on top of the figure() function.
# It takes three arguments: the number of rows, the number of columns, and the index of the subplot you want to create.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Creating Multiplots on Same Canvas. 2 subplots in a single figure. 
## You can adjust the figure size by passing the figsize argument to the subplots() function.
## You can also adjust the dpi (dots per inch) of the figure by passing the dpi argument to the figure() function.

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=70)      # Create an EMPTY 1x2 grid of subplots

# Axes is an array of Axes objects so you can ITERATE over it.
for ax in axes:
    ax.plot(x, y, 'b')          # Plot on the axes object. 'b' is the color blue.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

plt.show()
# plt.tight_layout() # Adjust the spacing between subplots to prevent overlap

# If you want to popultate the subplots with different data, you can do it like this:
fig, axes = plt.subplots(nrows=1, ncols=2)  

axes[0].plot(x, y, 'b')          # Plot on the first axes object. 'b' is the color blue.
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('plot A')

axes[1].plot(y, x, 'r')          # Plot on the second axes object. 'r' is the color red.
axes[1].set_xlabel('y')
axes[1].set_ylabel('x')
axes[1].set_title('plot B')
plt.show()



# SAVE FIGURE: Save the figure to a file. You can save the figure in different formats such as PNG, PDF, SVG, etc.

fig.savefig('my_figure.png', dpi=300)  # Save the figure to a file in the CURRENT WORKING DIR. The dpi argument specifies the resolution of the image.


# Adding a LEGEND: You can add a legend to the plot to identify different lines or markers in the plot.
fig, ax = plt.subplots()

ax.plot(x, x**2, label="x**2", color='blue', linestyle='--',linewidth=0.75)             # linestyle='--' means dashed line
ax.plot(x, x**3, label="x**3", color='red',linewidth=1.75,marker='+')                   # marker indicates where the data points are located.
ax.legend(loc=1)            # loc=1 means upper right corner. You can also use loc='upper right' or loc='best' to let matplotlib choose the best location.

plt.show()




## PLOT RANGE: You can set the range of the x and y axes using the xlim() and ylim() functions.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0,0, 1, 1])
ax.plot(x, y, ls='--')

# Set the x and y axis limits
ax.set_xlim(0, 1)          # Set the x axis limits to 0 and 1
ax.set_ylim(0, 1)          # Set the y axis limits to 0 and 1
plt.show()


## SPECIAL PLOT TYPES: Matplotlib has many special plot types such as scatter plots, bar plots, histograms, etc.

plt.scatter(x,y)    # Scatter plot
plt.show()


from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)  # Histogram
plt.show()