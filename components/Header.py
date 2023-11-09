import dash_mantine_components as dmc
from dash_iconify import DashIconify

title = dmc.Text(
            "Bioinformatics Reposiories Classifier",
            variant="gradient",
            gradient={"from": "#764BA2", "to": " #667EEA", "deg": 45},
            style={"fontSize": 22},
            size="xl",
            weight=500,
            mt=20,
            ml=20,
        )

links = dmc.Anchor(
    dmc.Button(DashIconify(icon="bi:github", width=20), variant="subtle", m=20, color="gray"),
    href="https://github.com",
    target="_blank"
    )


header = dmc.Header(
    children=[
        dmc.Grid(
            children=[
                dmc.Col(title, span=11),
                dmc.Col(links, span=1),
                ]
            )
        ], 
    height=70, fixed=True, style={"zIndex": 1000}
)
