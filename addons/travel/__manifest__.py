{
    "name": "Travelling",
    "depends": ["mail"],
    "data": [
        # security
        "security/ir.model.access.csv",

        # data
        "data/sequence.xml",

        # views
        "views/township.xml",
        "views/travel_gate.xml",
        "views/travel_agency.xml",

        # menus
        'views/menus.xml'
    ]
}
