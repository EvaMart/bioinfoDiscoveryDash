import dash_mantine_components as dmc
from dash_iconify import DashIconify

title = dmc.Text(
            "Bioinformatics Reposiories Classifier",
            style={"fontSize": 22},
            size="md",
            weight=700,
        )


Btn1 =  dmc.Button(
        children=[DashIconify(icon="ci:hamburger-lg", width=24, height=24,color="#c2c7d0")],
        variant="subtle", 
        p=1,
        ml=10,
        id='sidebar-button'
    )

left_stuff = dmc.Group(
    position="left",
    children=[
        Btn1,
        title
    ]
)

links = dmc.Anchor(
    dmc.Button(DashIconify(icon="bi:github", width=20), variant="subtle", m=20, color="gray"),
    href="https://github.com",
    target="_blank"
    )


header = dmc.Header(
        dmc.Group(
            children=[
                left_stuff,
                links
            ],
            position="apart",
        ),
        height=70, 
        fixed=True, 
        style={"zIndex": 1000}
)
