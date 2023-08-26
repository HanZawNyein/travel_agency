{
    "name": "ICA Todo",
    "author": "Han Zaw Nyein",
    "depends": ["web"],
    "data": [
        "security/ir.model.access.csv",

        "views/ica_todo.xml"
    ],
    "license": "LGPL-3",
    'assets': {
        'web.assets_backend': [
            "ica_todo/static/src/todo/ica_todo.js",
            "ica_todo/static/src/todo/ica_todo.xml"
        ]
    }
}
