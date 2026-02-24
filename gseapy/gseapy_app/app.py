#!/usr/bin/env python

# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
import dash_bio

pd.set_option('display.max_columns', None)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data
gseapy_hallmark = pd.read_csv('../gseapy_final_files/il6_jak-stat_paired-form_gseapy_hallmark.csv')

def pivot_csv(input_filename, output_filename, index_col, columns_col, values_col):
    """
    Reads a CSV file, pivots it, and saves the result to a new CSV file.

    Parameters:
    input_filename (str): The path to the input CSV file.
    output_filename (str): The path to save the output pivoted CSV file.
    index_col (str): The column to use as the new index.
    columns_col (str): The column to use to create new columns.
    values_col (str): The column to use for populating values in the pivoted table.
    """

    # Read the input CSV file
    df = pd.read_csv(input_filename)

    # Pivot the DataFrame
    pivoted_df = df.pivot(index=index_col, columns=columns_col, values=values_col)

    # Save the pivoted DataFrame to a new CSV file
    pivoted_df.to_csv(f'./gseapy_app/{output_filename}')

    return pivoted_df

# pivoted_gseapy_hallmark = pivot_csv('../gseapy_final_files/il6_jak-stat_paired-form_gseapy_hallmark.csv', 'pivoted_gseapy_hallmark.csv', 'Term', 'drug', 'NES')

# Initialize the app
# app = Dash()

# App layout. Requires Dash 2.17.0 or later
# app.layout = [
#     html.Div(children='My First App with Data'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{"field": i} for i in df.columns]
#     )
# ]

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)