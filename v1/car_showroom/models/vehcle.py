# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class vehcle(models.Model):
     _name = "car.vehcle"
     _rec_name ="mv_number"


     mv_number = fields.Char(string="mv_number")
     plate_namber = fields.Char(string="plate_namber")
     variant = fields.Char(string="variant")
     mileage = fields.Char(string="mileage")
     engine_namber = fields.Char(string="engine_namber")
     chasis_namber = fields.Char(string="chasis_namber")
     price = fields.Float()




     state = fields.Selection([
         ('act', "active"),
         ('not_act', "not active"),
         ('stop', "stop"),
         ], default="act")



     model_id = fields.Many2one("car.model")
