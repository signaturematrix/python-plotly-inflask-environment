from dashflaskapp import dash_app1
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


# Can create data connection and retrieval here. Let if be from CSV file or SQL database or any other source of data 
# This time I do not go into the detail of this

dash_app1.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
            dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])

@dash_app1.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    return 'Output: {}'.format(input_value)