# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

hd_r = pd.read_csv('assets/hd_renamed.csv')
hd_r_thal_2_yes = hd_r[hd_r['thal_2'] == 1]
hd_r_cp_0_yes = hd_r[hd_r['chest_pain_0'] == 1]
hd_r_thal_3_yes = hd_r[hd_r['thal_3'] == 1]

# fig = px.scatter(hd_r, x='cholestoral', y='thal_2', color='target', marginal_x='histogram')
fig2 = px.scatter(hd_r_thal_2_yes, x='age', y='sex', color='target', marginal_x='histogram')
fig3 = px.scatter(hd_r_cp_0_yes, x='age', y='sex', color='target', marginal_x='histogram')
fig4 = px.scatter(hd_r_thal_3_yes, x='age', y='sex', color='target', marginal_x='histogram')

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups
            in the United States. One person dies every 37 seconds in the United States from cardiovascular disease.
            About 647,000 Americans die from heart disease each year—that's 1 in every 4 deaths.
            https://www.cdc.gov/heartdisease/facts.htm
            
            In my project I used features importance to find out which of them are more important in predicting
            a heart disease
            """
        ), 
        html.Img(src='assets/ThalliumStressTest.jpg', className='img-fluid'),
        dcc.Markdown(
            
            '''
            From the feature importance and Eli5 permutation importance for RandomForestClassifier 
            you can see that some of the features are more correlated to the target than the others.
            
            '''),
        html.Img(src='assets/feature_importance.png', className='img-fluid'),
        html.Img(src='assets/permutation_importance.png', className='img-fluid'),
        dcc.Markdown(
            '''
            Positive results on Thallium stress test type 2 has a big impact on prediction the patients
            who have a heart disease. On the other hand Chest Pain type 0 and Thallium stress test type 3 have a more 
            positive correlation with those patients who doesn't have a heart disease.
            
            '''),
        dcc.Markdown('#### Thallium stress test type 2 positive'),
        dcc.Graph(figure=fig2),
        dcc.Markdown(
            '''
            You can interact with the plot to see the impact on those who have Thallium stress test type 2, Chest pain type 0
            or Thallium stress test type 3 in correlation to the target. 1 = got a disease, 0 = doesn't have a disease.
            
            '''),
        dcc.Markdown('#### Chest Pain type 0 positive'),
        dcc.Graph(figure=fig3),
        dcc.Markdown('#### Thallium stress test type 3 positive'),
        dcc.Graph(figure=fig4),

    ],
)

layout = dbc.Row([column1])