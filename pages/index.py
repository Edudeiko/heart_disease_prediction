# Imports from 3rd party libraries
import dash
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Heart Disease Prediction

            Keep yourself healthy :) 

            Using the features provided you can predict a possible heart disease.
            
            Some of the feature explanation for ease read:
            
            sex — (1 = male; 0 = female),
            
            target — have heart disease or not (1=yes, 0=no)
            """
        ),
        dcc.Link(dbc.Button('Have a heart disease?', color='primary'), href='/predictions')
    ],
    md=4,
)

hd = pd.read_csv('assets/hd_renamed.csv')
fig = px.scatter(hd, x='max_heart_rate_achieved', y='age', color='target', marginal_x='histogram')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])