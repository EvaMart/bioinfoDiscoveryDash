from dash import html, callback, Input, Output
from dash_iconify import DashIconify
import dash_mantine_components as dmc


def generate_btn(i):
    see = dmc.Button(DashIconify(icon="mdi:eye"), size="sm", variant="subtle" , color="gray", id=f'btn_{i}')
    
    return see
