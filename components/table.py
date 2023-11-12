
from dash import html, callback, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc, callback_context

from components.seeBtn import generate_btn

from charts.utils import connectMongo 

collection, logCollection = connectMongo()

# get all repos with prediction == bioinformatics
bioinformaticsRepos = list(collection.find({"prediction": "bioinformatics"}))

header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Repository"),
                html.Th("Conf"),
            ]
        )
    )
]


def link(name):
    l = dmc.Anchor(name,
                href="https://github.com",
                target="_blank")
    return l

rows = []
for repo in bioinformaticsRepos :
    row1 = html.Tr([html.Td([link(repo['name']), generate_btn(repo['name'])]), html.Td(repo['confidence']) ])
    rows.append(row1)


body = [html.Tbody(rows)]

table = dmc.Table(header + body)


## ------ card --------------------------------


def generate_title(name):
   return dmc.Text(f"README Preview of {name}", weight=500)

card = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Group(
                children=[
                    dmc.Text(f"README Preview of", weight=500),
                    dmc.Text(link(bioinformaticsRepos[0]['name']), weight=500,  id='card_title')
                ],
                position="left",
                spacing=5
            ),
            withBorder=True,
            inheritPadding=True,
            py="xs",
        ),
        dmc.CardSection(
            children=[dcc.Markdown(children=[bioinformaticsRepos[0]['readme']], id='markdown' )],
            style={"height": 450, "overflow": "scroll", "fontSize": 12}, 
            p="md",
        )
    ],
    withBorder=True,
    shadow="xs",
    radius="md",
    ml=20,
    id="card",
)

@callback(
    [
        Output('markdown', 'children', allow_duplicate=True),
        Output('card_title', 'children', allow_duplicate=True),
    ],
    [Input(f"btn_{repo['name']}", 'n_clicks') for repo in bioinformaticsRepos],
    prevent_initial_call=True
)
def update_mkd(*args):
    print(args)
    trigger = callback_context.triggered[0] 
    print("You clicked button {}".format(trigger["prop_id"].split("_")[1].split(".")[0]))
    # search for that repo in repos
    repo = next((item for item in bioinformaticsRepos if item["name"] == trigger["prop_id"].split("_")[1].split(".")[0]), None)
    return [repo['readme']], [link(repo['name'])]



table_grid = dmc.Grid(
    children=[
        dmc.Col(table, span=4),
        dmc.Space(w=30),
        dmc.Col(card, span=7),
        ]
    )

