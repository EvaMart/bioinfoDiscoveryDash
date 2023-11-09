from dash import register_page, dcc
import dash_mantine_components as dmc
from dash import html
import plotly.express as px


from components.Card import card

# five cards to show number of successful retrievals 
header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Element Position"),
                html.Th("Element Name"),
                html.Th("Symbol"),
                html.Th("Atomic Mass"),
            ]
        )
    )
]


row1 = html.Tr([html.Td("6"), html.Td("Carbon"), html.Td("C"), html.Td("12.011")])
row2 = html.Tr([html.Td("7"), html.Td("Nitrogen"), html.Td("N"), html.Td("14.007")])
row3 = html.Tr([html.Td("39"), html.Td("Yttrium"), html.Td("Y"), html.Td("88.906")])
row4 = html.Tr([html.Td("56"), html.Td("Barium"), html.Td("Ba"), html.Td("137.33")])
row5 = html.Tr([html.Td("58"), html.Td("Cerium"), html.Td("Ce"), html.Td("140.12")])

body = [html.Tbody([row1, row2, row3, row4, row5, row1, row2, row3])]

table = dmc.Table(header + body)


df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", width=600, height=400, template="plotly_white" )



cards = dmc.SimpleGrid(
    cols=5,
    children=[
        card('Repos searched', 2343),
        card('Repos accessed', 1000),
        card('Readmes', 876),
        card('Bioinformatics readmes', 20),
        card('Non-bioinformatics readmes', 856)
    ],
    m=15
)

bioinformatics = dmc.SimpleGrid(
    cols=2,
    children=[
        dcc.Graph(figure=fig),
        table
    ],
    m=15
)

register_page(__name__, path="/")

def layout():
    return dmc.MantineProvider(
        inherit=True,
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[
            dmc.Space(h=20),
            dmc.Title('Repositories',order=1),
            cards,
            dmc.Space(h=20),
            dmc.Title('Bioinformatics Repositories',order=2),
            bioinformatics,
            dmc.Title('Non-Bioinformatics Repositories',order=2),
            bioinformatics
            ]
    )