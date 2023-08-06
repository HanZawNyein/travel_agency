from odoo import api, fields, models


class TravelCar(models.Model):
    _name = 'travel.car'
    _description = 'TravelCar'

    car_number = fields.Char()
    travel_agency_id = fields.Many2one('travel.agency', required=True)
    partner_id = fields.Many2one('res.partner')
    join_date = fields.Date(default=lambda self: fields.Date.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running')
    ], default='draft')
    avatar = fields.Image()

    def name_get(self):
        return [(rec.id, f"{rec.car_number}({rec.travel_agency_id.name})") for rec in self]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_running(self):
        for rec in self:
            rec.state = 'running'

    def action_change_driver(self):
        return {
            'name': "Change Driver",
            'type': 'ir.actions.act_window',
            'res_model': 'change.driver.wizard',
            'view_mode': 'form',
            'target': 'new'
        }

    def action_change_driver_history(self):
        return {
            'name': f"{self.car_number}'s Driver History",
            'type': 'ir.actions.act_window',
            'res_model': 'travel.driver.history',
            'view_mode': 'tree,form',
            # 'target': 'current'
            "domain": [('travel_car_id', '=', self.id)]
        }
