# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class invo_desc_without_internal_ref(models.Model):
#     _name = 'invo_desc_without_internal_ref.invo_desc_without_internal_ref'
#     _description = 'invo_desc_without_internal_ref.invo_desc_without_internal_ref'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
