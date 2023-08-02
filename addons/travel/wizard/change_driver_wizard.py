from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ChangeDriverWizard(models.TransientModel):
    _name = 'change.driver.wizard'
    _description = 'Change Driver Wizard'

    partner_id = fields.Many2one('res.partner', required=True)
    join_date = fields.Date(default=lambda self: fields.Date.today())

    def change_driver(self):
        context = self.env.context
        active_model = context.get('active_model')  # travel.car
        active_id = context.get('active_id')  # 1
        travel_card_id = self.env[active_model].browse(active_id)
        if self.partner_id == travel_card_id.partner_id:
            raise UserError(_("Change Driver should not be same."))

        values = {
            "travel_car_id": travel_card_id.id,
            "driver_id": travel_card_id.partner_id.id,
            "join_date": travel_card_id.join_date,
            "fired_date": fields.Date.today()
        }
        self.env['travel.driver.history'].create(values)
        travel_card_id.partner_id = self.partner_id
        travel_card_id.join_date = self.join_date
