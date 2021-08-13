using DashBootstrapComponents, DashHtmlComponents

badges = html_span([
    dbc_badge("Primary", color="primary", class_name="mr-1"),
    dbc_badge("Secondary", color="secondary", class_name="mr-1"),
    dbc_badge("Success", color="success", class_name="mr-1"),
    dbc_badge("Warning", color="warning", class_name="mr-1"),
    dbc_badge("Danger", color="danger", class_name="mr-1"),
    dbc_badge("Info", color="info", class_name="mr-1"),
    dbc_badge("Light", color="light", class_name="mr-1"),
    dbc_badge("Dark", color="dark"),
]);
