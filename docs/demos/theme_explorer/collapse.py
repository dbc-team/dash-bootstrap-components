import dash_bootstrap_components as dbc
import dash_html_components as html

from .util import make_subheading

collapse = html.Div(
    [
        make_subheading("Collapse", "collapse"),
        html.Div(
            [
                dbc.Button(
                    "Open collapse", id="collapse-button", class_name="mb-2"
                ),
                dbc.Collapse(
                    dbc.Card(
                        dbc.CardBody("This content is hidden in the collapse")
                    ),
                    id="collapse",
                ),
            ]
        ),
    ],
    class_name="mb-4",
)
