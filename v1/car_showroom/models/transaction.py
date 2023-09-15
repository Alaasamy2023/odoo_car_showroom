# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class transaction(models.Model):
     _name = "car.transaction"



     agent_name = fields.Char(string="agent_name")
     f_name = fields.Char(string="f_name")
     l_name = fields.Char(string="l_name")
     m_name = fields.Char(string="m_name")
     sex = fields.Char(string="sex")
     dob = fields.Date()
     contact = fields.Char(string="contact")
     email = fields.Char(string="email")
     address = fields.Char(string="address")

     # state = fields.Selection([
     #     ('act', "active"),
     #     ('not_act', "not active"),
     #     ('stop', "stop"),
     #     ], default="act")



     vehcle_id = fields.Many2one("car.vehcle")
