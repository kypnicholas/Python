import plotly.io as pio
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import pandas as pd

## Create a USA geographical plot with sample data ##

# Sample data (dictionary) for choropleth map
data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['Arizona','California','New York'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})

# Define the layout for the map 
layout = dict(geo = {'scope':'usa'})

# Create the figure and display it. Pass the 'data' object and the 'layout' object to the 'Figure' function
choromap = go.Figure(data = [data],layout=layout)
choromap.update_layout(title_text = 'US Choropleth Map Example',geo_scope='usa') # limit map scope to USA
# choromap.show()



## Create a USA geographical plot with built-in dataset ##

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
# print(df.head())

data = dict(type='choropleth',
            locations=df['code'],   
            locationmode='USA-states',
            colorscale='Reds',
            text=df['state'],
            z=df['total exports'],
            colorbar={'title':'Millions USD'}
              )

layout = dict(geo={'scope':'usa'})

choromap2 = go.Figure(data=[data],layout=layout)
choromap2.update_layout(title_text = '2011 US Agriculture Exports by State',geo_scope='usa')
# choromap2.show()



## Create a world geographical plot with built-in dataset ##
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
# print(df.head())

data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      ) 

layout = dict(
    geo={
        'scope': 'usa',
        'projection': {'type': 'mercator'}           # Different projection types available. They affect the appearance of the map.
        ## 'projection': {'type': 'orthographic'}
    }
)

choromap3 = go.Figure(data=[data],layout=layout)
choromap3.update_layout(title_text = '2014 World GDP by Country',geo_scope='world')
choromap3.show()    