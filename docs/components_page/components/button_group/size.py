import dash_bootstrap_components as dbc
import dash_html_components as html

button_groups = html.Div(
    [
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="lg",
            class_name="mr-1",
        ),
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="md",
            class_name="mr-1",
        ),
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="sm",
        ),
    ]
)
