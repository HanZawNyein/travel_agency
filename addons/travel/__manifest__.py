{
    "name": "Travelling",
    "depends": ["base", "mail", "contacts"],
    "data": [
        # security
        "security/ir.model.access.csv",

        # data
        "data/sequence.xml",

        # views
        "views/travel_driver_history.xml",
        "views/township.xml",
        "views/travel_gate.xml",
        "views/travel_agency.xml",
        "views/travel_car.xml",
        "views/transportation_route.xml",
        "views/travel_booking.xml",
        "views/res_partner.xml",

        # menus
        'views/menus.xml',

        # wizard
        "wizard/change_driver_wizard.xml",
    ]
}
