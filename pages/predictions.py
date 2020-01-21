# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
import numpy as np
from joblib import load
from dash.dependencies import Input, Output

# Imports from this application
from app import app

rf = load('assets/rf.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Adjust the features to predict a heart disease.

            """
        ),
        dcc.Markdown('#### Maximum heart rate achieved'),
        dcc.Slider(
            id='max_heart_rate_achieved',
            min=70,
            max=210,
            step=10,
            value=100,
            className='mb-5',
            tooltip={'always_visible': True, 'placement': 'bottom'}
        ),
        dcc.Markdown('#### Thallium stress test type 2'),
        dcc.Dropdown(
            id='thal_2',
            options = [
                {'label': 'positive', 'value': 1},
                {'label': 'negative', 'value': 0},
            ],
            value = 0,
            className = 'mb-5'
        ),
        dcc.Markdown('#### Sex'),
        dcc.Dropdown(
            id='sex',
            options = [
                {'label': 'male', 'value': 1},
                {'label': 'female', 'value': 0},
            ],
            value = 0,
            className = 'mb-5'
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Have a heart disease?', className='mb-5'),
        html.Div(id='prediction-content', className='lead')

    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('max_heart_rate_achieved', 'value'),
    Input('thal_2', 'value'),
    Input('sex', 'value')
    ],
)
def predict(max_heart_rate_achieved, thal_2, sex):
    df = pd.DataFrame(
        columns=['max_heart_rate_achieved', 'thal_2', 'sex'], 
        data=[[max_heart_rate_achieved, thal_2, sex]]
    )
    y_pred = rf.predict(df)[0]

    if y_pred == 0:
        return html.Img(src='/assets/red-heart.jpg', className='img-fluid')
    else:
        return html.Img(src='/assets/black-heart.jpg', className='img-fluid')

