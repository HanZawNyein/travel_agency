from odoo import api, fields, models, _
from odoo.exceptions import UserError


class TravelAgency(models.Model):
    _name = 'travel.agency'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TravelAgency'

    name = fields.Char(tracking=True)
    reference = fields.Char(tracking=True, default=lambda self: _("New"), copy=False)
    license_number = fields.Char(tracking=True)
    travel_car_ids = fields.One2many('travel.car', 'travel_agency_id')
    logo = fields.Image()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('license_number_unique', 'unique(license_number)', 'License Number be unique !')
    ]

    @api.constrains('name')
    def _check_name(self):
        if self.name in self.search([('id', '!=', self.id)]).mapped('name'):
            raise UserError(_("Agency Name is already exists."))

    @api.model
    def create(self, values):
        if values.get('reference', _('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('travel.agency') or _('New')
        # Add code here
        return super(TravelAgency, self).create(values)
