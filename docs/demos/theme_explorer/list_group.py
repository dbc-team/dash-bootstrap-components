import dash_bootstrap_components as dbc
import dash_html_components as html

from .util import make_subheading

list_group = html.Div(
    [
        make_subheading("ListGroup", "list_group"),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Item 1", color="primary", action=True),
                dbc.ListGroupItem("Item 2"),
                dbc.ListGroupItem("Item 3"),
                dbc.ListGroupItem(
                    [
                        html.H5("Item 4 heading"),
                        html.P("Item 4 text"),
                    ]
                ),
            ]
        ),
    ],
    class_name="mb-4",
)
