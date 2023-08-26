from odoo import api, fields, models, _
from odoo.exceptions import UserError


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
    travel_booking_line_ids = fields.One2many('travel.booking.line', 'travel_booking_id')

    @api.depends('partner_ids')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = len(rec.partner_ids) * rec.per_seat

    @api.model
    def create(self, values):
        # Add code here
        if values.get('transportation_route_id'):
            transportation_route_id = self.transportation_route_id.browse(values.get('transportation_route_id'))
            already_seats = set(transportation_route_id.transportation_route_line_ids.mapped('seat_number'))
            all_seats = set(range(1, transportation_route_id.seat + 1))
            available_seats = all_seats - already_seats
            if available_seats:
                values["travel_booking_line_ids"] = [
                    (0, 0, {"travel_booking_id": self.id, "seat_number": seat})
                    for seat in available_seats
                ]
        return super(TravelBooking, self).create(values)

    def action_confirm(self):
        booking = self.travel_booking_line_ids.filtered(lambda booking_line_id: booking_line_id.booking)
        if not len(self.partner_ids) == len(booking):
            raise UserError(_("Matching Failed."))
        self.state = "confirm"
        self.travel_booking_line_ids.filtered(
            lambda booking_line_id: booking_line_id.booking == False).unlink()
        self.transportation_route_id.transportation_route_line_ids = [
            (0, 0, {
                "transportation_route_id": self.transportation_route_id.id,
                "partner_ids": self.partner_ids.ids,
                "travel_booking_id": self.id,
                "seat_number": seat,
            }) for seat in self.travel_booking_line_ids.mapped('seat_number')
        ]


class TravelBookingLine(models.Model):
    _name = 'travel.booking.line'
    _description = 'TravelBookingLine'

    travel_booking_id = fields.Many2one('travel.booking')
    seat_number = fields.Integer()
    booking = fields.Boolean(default=False)
