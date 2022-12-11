# -*- coding: utf-8 -*-
# from odoo import http


# class InvoDescWithoutInternalRef(http.Controller):
#     @http.route('/invo_desc_without_internal_ref/invo_desc_without_internal_ref', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invo_desc_without_internal_ref/invo_desc_without_internal_ref/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invo_desc_without_internal_ref.listing', {
#             'root': '/invo_desc_without_internal_ref/invo_desc_without_internal_ref',
#             'objects': http.request.env['invo_desc_without_internal_ref.invo_desc_without_internal_ref'].search([]),
#         })

#     @http.route('/invo_desc_without_internal_ref/invo_desc_without_internal_ref/objects/<model("invo_desc_without_internal_ref.invo_desc_without_internal_ref"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invo_desc_without_internal_ref.object', {
#             'object': obj
#         })
