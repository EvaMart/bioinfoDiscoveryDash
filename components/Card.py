import dash_mantine_components as dmc


def card(title, number):
    card = dmc.Card(
        children=[
            dmc.Text(title, size="sm"),
            dmc.Space(h=10),
            dmc.Text(number, weight=500, size="xl"),
        ],
        
        shadow=False,
        withBorder = True
    )
    return card
