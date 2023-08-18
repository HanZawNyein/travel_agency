from odoo import api, fields, models


class TravelBooking(models.Model):
    _name = 'travel.booking'
    _description = 'TravelBooking'

    partner_ids = fields.Many2many('res.partner', required=True)
    transportation_route_id = fields.Many2one('transportation.route', domain="[('state','=','confirm')]")
    travel_agency_id = fields.Many2one('travel.agency', related="transportation_route_id.travel_agency_id")
    travel_car_id = fields.Many2one('travel.car', related="transportation_route_id.travel_car_id")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')
    ], default='draft')
