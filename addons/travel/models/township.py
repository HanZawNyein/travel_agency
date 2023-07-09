from odoo import api, fields, models

class TownShip(models.Model):
    _name = 'travel.township'
    _description = 'TownShip'

    name = fields.Char()
    gate_ids = fields.One2many('travel.gate','township_id')