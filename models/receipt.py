from odoo import models, fields, api


class Receipt(models.Model):
    _name = 'receipt.receipt'
    _description = 'Member Receipt'

    name = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    age = fields.Integer("Age")
    email = fields.Char("Email Id")
    memberid = fields.Many2one('sports.sports', string="Member Id")
    mobile = fields.Char("Mobile Number")
    fees = fields.Float("Fees")
    month = fields.Integer("Month")

    total_games_available_id = fields.Many2one('gamelist.gamelist', string='Select Game', )
    counting_member = fields.Integer(related='total_games_available_id.total_member_count', string="Total Member",
                                     store=True)

    total_amount = fields.Integer(string="Total Amount")

    @api.onchange('memberid')
    def onchange_memberid(self):
        if self.memberid:
            self.update({'name': self.memberid.name,
                         'lastname': self.memberid.lastname,
                         'age': self.memberid.age,
                         'email': self.memberid.email,
                         'mobile': self.memberid.mobile,
                         'fees': self.memberid.fees,
                         'month': self.memberid.month,
                         'total_games_available_id': self.memberid.total_games_available_id,
                         'total_amount': self.memberid.fees * self.memberid.month
                         })
