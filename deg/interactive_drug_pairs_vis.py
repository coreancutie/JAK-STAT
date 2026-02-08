#!/usr/bin/env python

# Import packages:
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_bio

pd.set_option('display.max_columns', None)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load in the data:
form_pairs_deg = pd.read_csv('./deg_final_files/head-to-head_wilcoxon_deg_results.csv') # Drug vs. drug: formulation-specific effects
form_pairs_deg['snp'] = None

# print(form_pairs_deg)

dmso_ref_deg = pd.read_csv('./deg_final_files/wilcoxon_deg_results.csv') # Drug vs. DMSO: drug vs. "healthy state" reference

# Creating drug-pair dropdown:
form_pairs_df = form_pairs_deg[['form_1', 'form_2']].drop_duplicates() # easiest way to get drug pairs df
# making this for the sake of the dropdown later
form_pairs_dict = {}

# iterate through the formula pairs dataframe to make this easier to handle for dash/plotly 
for col in form_pairs_df.transpose():
    form_1, form_2 = list(form_pairs_df.transpose()[col].values)
    form_pairs_str = f'{form_1}/{form_2}'
    form_pairs_dict[form_pairs_str] = (form_1, form_2)

# TODO: fill out docstring properly
def process_dmso_ref_data():
    '''
    Docstring for process_dmso_ref_data

    returns: pandas dataframe with DMSO reference deg results
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

cell_types = list(dmso_ref_deg['cell_type'].unique())

app.layout = html.Div(
    className = 'p-2',
    children = [
        html.H4('Formula pairs analysis'),
        dbc.Row([
            dbc.Col(
                width = 4,
                children = [
                    dcc.Dropdown(
                        id = "dropdown",
                        options = list(form_pairs_dict.keys()),
                        value = list(form_pairs_dict.keys())[0]
                    )
                ]
            ),
            dbc.Col(
                width = 4,
                children = [
                    dcc.Dropdown(
                        id = "dropdown_cell_type",
                        options = cell_types,
                        value = cell_types[0]
                    )
                ]
            )
        ]),
        dbc.Row([
            dbc.Col(
                width = 4,
                children = [dcc.Graph(id="scatter")]
            ),
            dbc.Col(
                width = 4,
                children = [dcc.Graph(id="volcano")]
            )
        ])
    ]
)

# todo: add callback for hover where it shows that data point across graphs

@app.callback(
    [Output("scatter", "figure"),
     Output("volcano", "figure")],
    Input("dropdown", "value"),
    Input("dropdown_cell_type", "value")
)
def update_figures(form_pair_str, cell_type_str):
    form_1, form_2 = form_pairs_dict[form_pair_str]
    # only filtering off of formula 1 since we don't need to filter off of formula 2 as well
    filtered_dmso_deg = paired_dmso_ref_deg[paired_dmso_ref_deg['group_form_1'] == form_1]
    filtered_dmso_deg = filtered_dmso_deg[filtered_dmso_deg['cell_type'] == cell_type_str]

    # scatter plot updates
    scatter_fig = px.scatter(
        filtered_dmso_deg,
        x='logfoldchanges_form_1', 
        y='logfoldchanges_form_2', 
        color = 'cell_type',

        marginal_x="histogram", 
        marginal_y='histogram',
        
        labels = {
            'logfoldchanges_form_1': f'{form_1} LFC',
            'logfoldchanges_form_2': f'{form_2} LFC'
        }
    )

    # 
    filtered_pairs_deg = form_pairs_deg[form_pairs_deg['form_1'] == form_1]
    filtered_pairs_deg = filtered_pairs_deg[filtered_pairs_deg['cell_type'] == cell_type_str]
    # Reset the index to default integers because there were errors when there were genes of interest
    filtered_pairs_deg.reset_index(inplace=True)

    #TODO: fix the snp attribute
    volcano_fig = dash_bio.VolcanoPlot(
        dataframe = filtered_pairs_deg,
        effect_size = 'logfoldchanges',
        p = 'pvals_adj',
        snp = 'snp',
        gene = 'names'
    )

    return scatter_fig, volcano_fig

# dcc.Graph(figure=px.histogram(dmso_ref_deg, x='continent', y='lifeExp', histfunc='avg'))

# todo: for future -- if doing ssGSEA across formulations can add a volcano plot showing the pathways next to 
# the existing plots

if __name__ == '__main__':
    app.run(debug=True)


