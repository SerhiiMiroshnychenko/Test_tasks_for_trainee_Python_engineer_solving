from odoo import fields, models

class DemoDemo(models.Model):
    _name = 'demo.demo'
    _description = 'Demo Object'

    name = fields.Char(string='Name')
