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
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    total_amount = fields.Monetary(currency_field="currency_id", compute="_compute_total_amount")
    per_seat = fields.Monetary(related="transportation_route_id.per_seat")

    @api.depends('partner_ids')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = len(rec.partner_ids) * rec.per_seat
