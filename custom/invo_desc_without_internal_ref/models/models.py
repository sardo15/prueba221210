-*- coding: utf-8 -*-

from odoo import models, fields, api
    
    _inherit = 'account.move.line'
    
    def _get_computed_name(self):
        self.ensure_one()

        if not self.product_id:
            return ''

        if self.partner_id.lang:
            product = self.product_id.with_context(lang=self.partner_id.lang)
        else:
            product = self.product_id

        values = []
        if product.partner_ref:
            values.append(product.partner_ref)
        if self.journal_id.type == 'sale':
            if product.description_sale:
                values.append(product.description_sale)
        elif self.journal_id.type == 'purchase':
            if product.description_purchase:
                values.append(product.description_purchase)
        
        val = '\n'.join(values)
        ref = "["+product.default_code+"] "
        return val.replace(ref,"",1)

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
