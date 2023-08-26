from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    transportation_route_line_ids = fields.Many2many('transportation.route.line', 'transportation_route_line_rel',
                                                     'transportation_route_line_id', 'partner_id')
