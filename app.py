from dash import Dash, page_container, callback, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dotenv import load_dotenv

from components.Header import header

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
        ]
    )

def get_icon(icon):
    return DashIconify(icon=icon, height=16)


navbar = dmc.Navbar(
        p="md",
        id='sidebar',
        fixed=True,
        width={"base": 70},
        children=[
            dmc.NavLink(
                icon=get_icon(icon="bx:stats"),
                label="Repositories",
                href="/",
            ),
            dmc.NavLink(
                icon=get_icon(icon="mdi:about-circle-outline"),
                label="About",
                href="/about",
            ),
        ],
    )



app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        header,
        dmc.Space(h=70),
        dmc.Group(
            children=[
                navbar,
                dmc.Space(w=80),
                dmc.Container(children=[page_container],  size="90%"),
            ],
            position="apart"
        ),
        dmc.Space(h=70)
    ]
)

@callback(
    Output("sidebar", "width"),          #what we wanted to change
    Input("sidebar-button", "n_clicks"), #width will change when btn is triggered
    State('sidebar','width'),            #store inital width
    prevent_initial_call=True,
    )
def sidebar(opened, width):
    if opened:
        if width['base'] == 200:         #if initial width is 300 then return 70
            return {"base": 70}
        else:
            return {'base':200}
        
if __name__ == '__main__':
    # Load env variables
    load_dotenv()

    app.run(debug=True)