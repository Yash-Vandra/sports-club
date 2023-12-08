from odoo import models,fields,api

class Sportsmembership(models.Model):
    _name = 'sports.sports'
    _description = 'Sports club'

    name = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    age = fields.Integer("Age")
    email = fields.Char("Email Id")
    memberid = fields.Char("Member Id")
    mobile = fields.Char("Mobile Number")
    fees = fields.Integer("Fees")
    month = fields.Integer("Month")

    total_games_available_id= fields.Many2one('gamelist.gamelist',string='Select Game')

    counting_member=fields.Integer(related='total_games_available_id.total_member_count',string="Total Member",store=True)
    total_amount=fields.Integer(string="total amount")

    @api.onchange('total_games_available_id')
    def onchange_total_games_available_id(self):
        if self.total_games_available_id:
            self.update({'fees':self.total_games_available_id.fees})
            # print(self.total_amount)

    def headerbutton(self):
        print("header button clicked........")

    def applycoupon(self):
        print("apply coupon clicked........")
