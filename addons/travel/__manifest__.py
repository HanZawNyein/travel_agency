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
        "views/travel_car.xml",

        # menus
        'views/menus.xml',

        # wizard
        "wizard/change_driver_wizard.xml",
    ]
}
