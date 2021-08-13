using DashBootstrapComponents, DashHtmlComponents

buttons = html_div([
    dbc_button("Regular", color="primary", class_name="mr-1"),
    dbc_button("Active", color="primary", active=true, class_name="mr-1"),
    dbc_button("Disabled", color="primary", disabled=true),
]);
