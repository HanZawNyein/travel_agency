from odoo import api, fields, models


class TownShip(models.Model):
    _name = 'travel.township'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TownShip'

    name = fields.Char(tracking=True)
    gate_ids = fields.One2many('travel.gate', 'township_id')
