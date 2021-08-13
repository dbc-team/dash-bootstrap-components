import dash_bootstrap_components as dbc
import dash_html_components as html

from .util import make_subheading

popover = html.Div(
    [
        make_subheading("Popover", "popover"),
        dbc.Button(
            "Click to toggle popover", id="popover-target", color="danger"
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Popover header"),
                dbc.PopoverBody("Popover body"),
            ],
            id="popover",
            is_open=False,
            target="popover-target",
        ),
    ],
    class_name="mb-4",
)
