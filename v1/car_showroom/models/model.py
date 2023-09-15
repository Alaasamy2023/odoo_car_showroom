# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class model(models.Model):
     _name = "car.model"
     name = fields.Char(string="Name")
     engine_type = fields.Char(string="engine_type")
     transmission_type = fields.Char(string="transmission_type")
     technology = fields.Char(string="technology")


     state = fields.Selection([
         ('act', "active"),
         ('not_act', "not active"),
         ('stop', "stop"),
         ], default="act")



     brand_id = fields.Many2one("car.brand")
     type_id = fields.Many2one("car.type")

