from odoo import api, fields, models, _
from odoo.exceptions import UserError


class TransportationRoute(models.Model):
    _name = 'transportation.route'
    _description = 'TransportationRoute'

    travel_agency_id = fields.Many2one('travel.agency', required=True)
    logo = fields.Image(related="travel_agency_id.logo")
    travel_car_id = fields.Many2one('travel.car')
    seat = fields.Integer(related="travel_car_id.seat")
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    per_seat = fields.Monetary()
    avatar = fields.Image(related='travel_car_id.avatar')
    driver_id = fields.Many2one('res.partner', related="travel_car_id.partner_id")
    start_datetime = fields.Datetime()
    start_township = fields.Many2one('travel.township')
    start_gate = fields.Many2one('travel.gate')
    arrived_datetime = fields.Datetime()
    arrived_township = fields.Many2one('travel.township')
    arrived_gate = fields.Many2one('travel.gate')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('running', 'Running'),
        ('arrived', 'Arrived'),
    ], default='draft')
    transportation_route_line_ids = fields.One2many('transportation.route.line', 'transportation_route_id')

    def name_get(self):
        return [(rec.id, f"{rec.travel_car_id.car_number}({rec.start_datetime}-{rec.arrived_datetime})") for rec in
                self]

    @api.constrains('start_datetime', 'arrived_datetime')
    def _check_start_arrived_datetime(self):
        if self.start_datetime >= self.arrived_datetime:
            raise UserError(_("Start Datetime Should be greater than arrived datetime!"))

    @api.onchange('travel_agency_id')
    def _onchange_travel_agency_id(self):
        if self.travel_agency_id:
            self.travel_car_id = False

    @api.onchange('start_township')
    def _onchange_start_township(self):
        if self.start_township:
            self.start_gate = False

    @api.onchange('arrived_township')
    def _onchange_arrived_township(self):
        if self.arrived_township:
            self.arrived_gate = False

    def action_confirm(self):
        self.state = "confirm"

    def action_running(self):
        self.state = "running"


class TransportationRouteLine(models.Model):
    _name = 'transportation.route.line'
    _description = 'TransportationRoute Line'

    transportation_route_id = fields.Many2one('transportation.route')
    partner_ids = fields.Many2many('res.partner', 'transportation_route_line_rel', 'partner_id',
                                   'transportation_route_line_id')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    amount = fields.Monetary(related="transportation_route_id.per_seat")
    seat_number = fields.Integer()
    travel_booking_id = fields.Many2one('travel.booking')

    @api.constrains('seat_number')
    def _check_start_arrived_datetime(self):
        for rec in self:
            seat_numbers = set(range(1, rec.transportation_route_id.seat + 1))
            all_seat_number: list = set(rec.transportation_route_id.transportation_route_line_ids.filtered(
                lambda x: x.id != rec.id).mapped('seat_number'))
            results = seat_numbers - all_seat_number
            if rec.seat_number not in results:
                raise UserError(_("Seat Booking is already exists!"))
