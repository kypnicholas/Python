import pandas as pd
import numpy as np

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# print(__version__)    # Check Plotly version

import cufflinks as cf

cf.go_offline()     # Initialize cufflinks for offline use

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())

# print(df.head())

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})

# print(df2.head())

###########################################################################################
### known incompatibility between Cufflinks and recent versions of Plotly and numpy.    ###
### using Plotly Express (built-in plotting function) as alternative below.             ###
###########################################################################################


## LINE PLOT ##
# Cufflinks implementation
# df.iplot(kind='line')

# Plotly Express implementation
import plotly.express as px
fig = px.line(df)
fig.show()

## SCATTER PLOT ##
# Cufflinks implementation
# df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)

# Plotly Express implementation
fig = px.scatter(df, x='A', y='B')
fig.show()

## BAR PLOT ##
# Cufflinks implementation  
# df2.iplot(kind='bar',x='Category',y='Values')

# Plotly Express implementation
fig = px.bar(df2, x='Category', y='Values')
fig.show()


## 3D SURFACE PLOT ##

df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})

# Cufflinks implementation
# df3.iplot(kind='surface',colorscale='rdylbu')

# Plotly graph Objects implementation
import plotly.graph_objects as go

fig = go.Figure(data=[go.Mesh3d(
    x=df['A'],
    y=df['B'],
    z=df['C'],
    opacity=0.5
)])
fig.show()