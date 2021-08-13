import dash_bootstrap_components as dbc

form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Email", class_name="mr-2"),
                dbc.Input(type="email", placeholder="Enter email"),
            ],
            class_name="mr-3",
        ),
        dbc.FormGroup(
            [
                dbc.Label("Password", class_name="mr-2"),
                dbc.Input(type="password", placeholder="Enter password"),
            ],
            class_name="mr-3",
        ),
        dbc.Button("Submit", color="primary"),
    ],
    inline=True,
)
