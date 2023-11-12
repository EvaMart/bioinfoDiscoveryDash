from dash import register_page, dcc
import dash_mantine_components as dmc


from components.table import table_grid
from charts.readmesCountLineChart import readmes_count_line_chart
from charts.confidence_distribution import confidence_distribution
from charts.cards import cards

plots = dmc.Grid(
    children=[
        dmc.Col(dcc.Graph(figure=readmes_count_line_chart), span=6),
        dmc.Col(dcc.Graph(figure=confidence_distribution), span=6),
        ]
    )


register_page(__name__, path="/")

def layout():
    return dmc.MantineProvider(
        inherit=True,
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[
            dmc.Space(h=20),
            dmc.Title('Mining stats',order=3, weight=500),
            cards,
            dmc.Space(h=10),
            dmc.Title('READMEs predictions',order=3, weight=500, mb=20),
            plots,
            dmc.Space(h=20),
            dmc.Title('Bioformatics READMEs',order=3, weight=500, mb=40),
            table_grid
            ]
    )