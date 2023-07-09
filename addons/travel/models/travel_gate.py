from odoo import api, fields, models 

class TravelGate(models.Model):
    _name = 'travel.gate'
    _description = 'TravelGate'

    name = fields.Char(required=True)
    township_id = fields.Many2one('travel.township')
    
