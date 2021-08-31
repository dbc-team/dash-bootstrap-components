import dash_bootstrap_components as dbc
import dash_html_components as html

badges = html.Span(
    [
        dbc.Badge("Primary", href="#", color="primary", class_name="me-1"),
        dbc.Badge("Secondary", href="#", color="secondary", class_name="me-1"),
        dbc.Badge("Success", href="#", color="success", class_name="me-1"),
        dbc.Badge("Warning", href="#", color="warning", class_name="me-1"),
        dbc.Badge("Danger", href="#", color="danger", class_name="me-1"),
        dbc.Badge("Info", href="#", color="info", class_name="me-1"),
        dbc.Badge("Light", href="#", color="light", text_color="dark", class_name="me-1"),
        dbc.Badge("Dark", href="#", color="dark"),
    ]
)
