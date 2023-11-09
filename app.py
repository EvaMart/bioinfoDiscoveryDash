from dash import Dash, page_container
import dash_mantine_components as dmc

from components.Header import header

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
        ]
    )


navbar = dmc.Navbar(
    p="md",
    fixed=True,
    width={"base": 250},
    hidden = True,    
    children=[
        dmc.NavLink(
            label="Repositories",
            href="/",
        ),
        dmc.NavLink(
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
        navbar,
        dmc.Space(h=70),
        dmc.Grid(
            children=[
                dmc.Col(navbar, span=2),
                dmc.Col(dmc.Container(page_container, size='xl'), span=10),
            ],
            gutter="xl",
        )
    ]
)



if __name__ == '__main__':
    app.run(debug=True)