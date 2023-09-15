# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class type(models.Model):
     _name = "car.type"
     name = fields.Char(string="Name")


     state = fields.Selection([
         ('act', "active"),
         ('not_act', "not active"),
         ('stop', "stop"),
         ], default="act")