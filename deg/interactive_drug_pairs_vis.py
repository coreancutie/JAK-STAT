#!/usr/bin/env python
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

form_pairs_deg = pd.read_csv('form_pairs_deg.csv')

# print(form_pairs_deg)

dmso_ref_deg = pd.read_csv('dmso_ref_deg.csv')
# easiest way to get drug pairs df
form_pairs_df = form_pairs_deg[['form_1', 'form_2']].drop_duplicates()

# making this for the sake of the dropdown later
form_pairs_dict = {}

# iterate through the formula pairs dataframe to make this easier to handle for dash/plotly 
for col in form_pairs_df.transpose():
    form_1, form_2 = list(form_pairs_df.transpose()[col].values)
    form_pairs_str = f'{form_1}/{form_2}'
    form_pairs_dict[form_pairs_str] = (form_1, form_2)

# print(form_pairs_dict)


# print(form_pairs_df)

pd.set_option('display.max_columns', None)

# TODO: fill out docstring properly
def process_dmso_ref_data():
    '''
    Docstring for process_dmso_ref_data

    returns: pandas dataframe with DMSO reference deg 
    '''
    # form_pairs = get_form_pairs_df()
    paired_names_dmso_df = pd.merge(dmso_ref_deg, form_pairs_df, left_on='group', right_on='form_1')

    # inner join off of drug 2 matching group but ALSO gene names matching and cell type matching
    paired_dmso_ref_deg = pd.merge(paired_names_dmso_df, dmso_ref_deg,
             left_on=['form_2', 'cell_type', 'names'],
             right_on=['group', 'cell_type', 'names'],
             suffixes=('_form_1', '_form_2'))
    return paired_dmso_ref_deg

paired_dmso_ref_deg = process_dmso_ref_data()

filtered_dmso_deg = paired_dmso_ref_deg[paired_dmso_ref_deg['group_form_1'] == 'Afatinib']

# print(filtered_dmso_deg)

# app.layout = [
#     # html.Div(children='Hello World'),
#     dcc.Graph(figure=px.scatter(filtered_dmso_deg, x='logfoldchanges_form_1', y='logfoldchanges_form_2', color = 'cell_type'))
# ]

matching_lfc = filtered_dmso_deg[filtered_dmso_deg['logfoldchanges_form_1'] == filtered_dmso_deg['logfoldchanges_form_2']]

# print(matching_lfc[matching_lfc['logfoldchanges_form_1'] != 0])

groups_form_1 = list(paired_dmso_ref_deg['group_form_1'].unique())


app.layout = html.Div([
    html.H4('Drug pairs analysis'),
    dcc.Dropdown(
        id = "dropdown",
        options = list(form_pairs_dict.keys()),
        value = "Afatinib/Afatinib dimaleate"
    ),
    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_scatter_plot(form_pair_str):
    #TODO: update docstring
    '''
    Docstring for update_scatterplot
    
    :param form_pair_str: Description
    :returns: 
    '''
    form_1, form_2 = form_pairs_dict[form_pair_str]
    # only filtering off of formula 1 since we don't need to filter off of formula 2 as well
    filtered_dmso_deg = paired_dmso_ref_deg[paired_dmso_ref_deg['group_form_1'] == form_1]
    fig = px.scatter(filtered_dmso_deg,
                     x='logfoldchanges_form_1', y='logfoldchanges_form_2', color = 'cell_type',
                     marginal_x="histogram", marginal_y='histogram',
                     labels={
                         'logfoldchanges_form_1': f'{form_1} LFC',
                         'logfoldchanges_form_2': f'{form_2} LFC'
                         }
                     )
    
    return fig

# dcc.Graph(figure=px.histogram(dmso_ref_deg, x='continent', y='lifeExp', histfunc='avg'))

if __name__ == '__main__':
    app.run(debug=True)
