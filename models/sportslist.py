from odoo import models,fields,api

class Gameslist(models.Model):
    _name = 'gamelist.gamelist'
    _description = 'List of Sports'

    name=fields.Char("Game Name")
    fees = fields.Integer("Fees")
    total_member_count =fields.Integer("Total Member")

