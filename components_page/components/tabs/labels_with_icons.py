import dash_bootstrap_components as dbc
from dash import html

tabs = dbc.Tabs(
    [
        dbc.Tab(
            html.Div("This is the content of tab 1", className="p-4"),
            label="Tab 1",
        ),
        dbc.Tab(
            html.Div("This is the content of tab 2", className="p-4"),
            label="Tab 2",
        ),
    ],
    id="labelled-tabs",
)
