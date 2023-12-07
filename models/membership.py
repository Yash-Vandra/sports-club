from odoo import models,fields,api

class Sportsmembership(models.Model):
    _name = 'sports.sports'
    _description = 'Sports club'

    firstname = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    age = fields.Integer("Age")
    email = fields.Char("Email Id")
    mobile = fields.Integer("Mobile Number")
    fees = fields.Float("Fees")

    total_games_available_id= fields.Many2one('gamelist.gamelist',string='Select Game')


    @api.onchange('total_games_available_id')
    def onchange_total_games_available_id(self):
        if self.total_games_available_id:
            self.update({'fees':self.total_games_available_id.fees})