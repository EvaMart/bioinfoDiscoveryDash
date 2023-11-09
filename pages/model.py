from dash import register_page, dcc
import dash_mantine_components as dmc


content = dcc.Markdown('''
# Model
👋🏻 Hello!                       
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