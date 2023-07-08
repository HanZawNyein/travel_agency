from odoo import api, fields, models

class TownShip(models.Model):
    _name = 'travel.township'
    _description = 'TownShip'

    name = fields.Char()