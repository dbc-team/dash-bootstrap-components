import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

fade = html.Div(
    [
        dbc.Button(
            "Toggle fade",
            id="fade-transition-button",
            class_name="mb-3",
            n_clicks=0,
        ),
        dbc.Fade(
            dbc.Card(
                dbc.CardBody(
                    html.P(
                        "This content fades in and out", class_name="card-text"
                    )
                )
            ),
            id="fade-transition",
            is_in=True,
            style={"transition": "opacity 2000ms ease"},
            timeout=2000,
        ),
    ]
)


@app.callback(
    Output("fade-transition", "is_in"),
    [Input("fade-transition-button", "n_clicks")],
    [State("fade-transition", "is_in")],
)
def toggle_fade(n, is_in):
    if not n:
        # Button has never been clicked
        return True
    return not is_in
