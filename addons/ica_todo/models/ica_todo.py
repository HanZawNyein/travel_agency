from odoo import api, fields, models


class IcaTodo(models.Model):
    _name = 'ica.todo'
    _description = 'IcaTodo'

    name = fields.Char()
    completed = fields.Boolean(default=False)
