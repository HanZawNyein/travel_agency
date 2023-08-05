from odoo import api, fields, models


class TransportationRoute(models.Model):
    _name = 'transportation.route'
    _description = 'TransportationRoute'

    travel_agency_id = fields.Many2one('travel.agency', required=True)
    travel_car_id = fields.Many2one('travel.car')
    avatar = fields.Image(related='travel_car_id.avatar')
    driver_id = fields.Many2one('res.partner', related="travel_car_id.partner_id")
    start_datetime = fields.Datetime()
    start_township = fields.Many2one('travel.township')
    start_gate = fields.Many2one('travel.gate')
    arrived_datetime = fields.Datetime()
    arrived_township = fields.Many2one('travel.township')
    arrived_gate = fields.Many2one('travel.gate')
