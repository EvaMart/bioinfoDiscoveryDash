from dash import register_page, dcc
import dash_mantine_components as dmc


content = dcc.Markdown('''
# About
👋🏻 Hello! 
                       
This project classifies GitHub repositories into 2 categories: Bioinformatics and Non-Bioinformatics.                  
''')

register_page(__name__)

def layout():
    return dmc.MantineProvider(
        inherit=True,
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[
            content
            ]
    )