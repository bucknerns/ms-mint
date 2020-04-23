import platform

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_table import DataTable

import numpy as np

from multiprocessing import cpu_count
from ms_mint import __version__

from .button_style import button_style

n_cpus = cpu_count()

slider_style = {'marginBottom': '3em'}
info_style =   {'margin-top': 10, 'margin-bottom': 10, 'margin-left': 10,
                'display': 'inline-block', 'float': 'right', 'color': 'grey'}


ISSUE_TEXT = f'''
%0A%0A%0A%0A%0A%0A%0A%0A%0A
MINT: {__version__}%0A
OS: {platform.platform()}%0A
'''

Layout = html.Div(
    [   
     
        html.H1('MINT', style={'margin-top': '10%'}),
        html.P(f'v{__version__}', style={'text-align': 'right', 'color': 'grey'}),
        html.Div(id='storage', style={'display': 'none'}),
        
        # Status
        html.Div(id='n_peaklist_selected', children=0, style={'display': 'none'}),
        html.Div(id='n_files_selected', children=0, style={'display': 'none'}),

        # Buttons
        html.Button('Select peaklist file(s)', id='B_peaklists', style=button_style()),
        html.Button('Add MS-file(s)', id='B_add_files', style=button_style()),
        html.Button('Load', id='B_load', style=button_style('neutral')),
        html.Button('Reset', id='B_reset', style=button_style('warn')),
        
        html.A(href=f'https://github.com/soerendip/ms-mint/issues/new?body={ISSUE_TEXT}', 
               children=[html.Button('Help / Issues', id='B_help', style=button_style('help', float="right"))],
               target="_blank"),

        html.Br(),
        
        dcc.Checklist(id='files-check', 
                      options=[{ 'label': 'Add files from directory', 'value': 'by-dir' }], 
                      value=['by-dir'], style={'display': 'inline-block'}),
        html.Br(),
        
        html.Div(id='files-text', children='', style=info_style),
        
        html.Div(id='peaklist-text', children='', style=info_style),
        
        html.Div(id='cpu-text', children='', style=info_style),
        
        html.Br(),

        html.P("Select number of cores:", style={'display': 'inline-block', 'margin-top': 30}),
        
        html.Div(dcc.Slider( id='n_cpus', 
                            min=1, max=n_cpus,
                            step=1, value=n_cpus,
                            marks={i: f'{i} cpus' for i in [1, n_cpus]}),
                style=slider_style),
        
        html.Button('Run', id='B_run'),
        
        html.A(html.Button('Export', id='B_export'), href="export"),
        
        # Progress bar
        dcc.Interval(id="progress-interval", n_intervals=0, interval=1000, disabled=False),
        dbc.Progress(id="progress-bar", value=0),
        html.Div(id='progress', children=[], style=info_style),
        
        html.Br(),
        
        html.H2("Table View", style={'margin-top': 100}),
        
        dcc.Dropdown(id='table-value-select', value='full',
                     options=[ 
                              {'label': 'Full Table', 'value': 'full'},
                              {'label': 'Peak Area', 'value': 'peak_area'},
                              {'label': 'Retention time of maximum', 'value': 'peak_rt_of_max'},
                              {'label': 'Peak Max', 'value': 'peak_max'},
                              {'label': 'Peak Min', 'value': 'peak_min'},
                              {'label': 'Peak Median', 'value': 'peak_median'},
                              {'label': 'Peak Mean', 'value': 'peak_mean'},
                              {'label': 'First minus last intensity', 'value': 'peak_delta_int'}
                     ]),
        
        html.Div(id='run-out', 
                 style={'min-height':  0, 'margin-top': 10},
                 children=[DataTable(id='table', data=np.array([]))]),
        
        dcc.Input(id="label-regex", type='text', placeholder="Label Selector"),
        
        html.Button('Reload', id='B_reload'),

                                
        html.H2("Heatmap"),
        
        html.Button('Heatmap', id='B_heatmap', style=button_style()),
        
        dcc.Checklist(id='checklist', 
                options=[{ 'label': 'Normalized by biomarker', 'value': 'normed'},
                        { 'label': 'Cluster', 'value': 'clustered'},
                        { 'label': 'Dendrogram', 'value': 'dendrogram'},
                        { 'label': 'Transposed', 'value': 'transposed'},
                        { 'label': 'Correlation', 'value': 'corr'} ], 
                value=['normed'], style={'display': 'inline-block'}),
        html.P(id='heatmap-message'),
        
        dcc.Graph(id='heatmap', figure={}),
        
        html.Div(id='analysis', children=[
        
                html.H2("Peak Shapes"),
                
                dcc.Dropdown(id='peakshapes-selection',
                        options=[],
                        value=[],
                        multi=True
                        ), 
                
                html.Button('Peak Shapes', id='B_shapes', style=button_style()),
                
                dcc.Checklist(id='check_peakShapes', 
                        options=[{'label': 'Show Legend', 'value': 'legend'},
                                {'label': 'Horizontal legend', 'value': 'legend_horizontal'}],
                        value=['legend'], style={'display': 'inline-block'}),
                
                html.Div(dcc.Slider(id='n_cols', min=1, max=5, step=1, value=2,
                                marks={i: f'{i} columns' for i in range(1, 6)}),
                        style=slider_style),
                
                dcc.Graph(id='peakShape', figure={}),
                
                html.H2("Peak Shapes 3D"),
                
                html.Button('Peak Shapes 3D', id='B_shapes3d', style=button_style()),
                
                dcc.Checklist(id='check_peakShapes3d', 
                        options=[{'label': 'Show Legend', 'value': 'legend'},
                                {'label': 'Horizontal legend', 'value': 'legend_horizontal'}], 
                        value=['legend'], style={'display': 'inline-block'}),
                
                dcc.Dropdown(id='peak-select', options=[]),
                
                dcc.Graph(id='peakShape3d', figure={}, style={'height': 800}),
        ], style={'display': 'none'})
], style={'max-width': '80%', 'margin': 'auto', 'margin-bottom': '10%'})
