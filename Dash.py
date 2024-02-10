#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install dash')
get_ipython().system('pip install dash-renderer')
get_ipython().system('pip install dash_html_components')
get_ipython().system('pip install dash_core_components')


# In[22]:


get_ipython().system('pip install dash_bootstrap_components')
import dash
from dash import Dash, dcc, html, Output, Input,callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# In[11]:


app=Dash()


# In[34]:


app.layout=html.Div([
    html.H1('Hello world'),
    html.Div('Dash-first project')
    
])


# In[35]:


if __name__ == '__main__':
    app.run_server(port=4050)


# In[23]:


app = Dash(__name__)
app.layout = html.Div(
    [
        html.Button("Download CSV", id="btn_csv"),
        dcc.Download(id="download-dataframe-csv"),
    ]
)

df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 1, 5, 6], "c": ["x", "x", "y", "y"]})


@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "mydf.csv")


if __name__ == "__main__":
    app.run(debug=True)
    


# In[24]:


from dash import Dash, dcc, html, dash_table, Input, Output, State, callback

import base64
import datetime
import io

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run(debug=True)


# In[27]:


app=Dash(__name__)
app.layout=html.Div([
    dcc.Dropdown(['new york','amsterdam','sydney','san fransisco'],multi=True)
    
    
])

if __name__=='__main__':
    app.run(debug=True)


# In[32]:


app=Dash(__name__)
app.layout=html.Div([
    dcc.Slider(
    id='my slider',
    min=0,
    max=10,
    value=5,    
    marks={i:'{}'.format(i) for i in range (11)}    
    )
    
    
])
if __name__=='__main__':
    app.run(debug=True)


# In[33]:


app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    dcc.Input(id='input', value='Initial Text', type='text'),
    html.Div(id='output')
])

# Define the callback function
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    return 'You have entered: "{}"'.format(input_value)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




