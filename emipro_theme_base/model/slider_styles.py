# -*- coding: utf-8 -*-
"""
    This model is used to create a slider styles fields
"""
from odoo import api, fields, models, _

class SliderStyles(models.Model):

    _name = "slider.styles"
    _description = "Slider Styles"

    display_name = fields.Char(string='Name', required=True)
    style_template_key = fields.Char(string='Key', required=True)
    slider_type = fields.Selection([
        ('product', 'Product'),
        ('category', 'Product Category'),
        ('brand', 'Product Brand'),
    ], string="Slider Type",
        required=True, default='product', readonly=False)
    slider_style = fields.Selection([
        ('slider', 'Slider'),
        ('grid', 'grid'),
        ('list', 'List'),
    ], string="Slider Style",
        required=True, default='slider', readonly=False)

    def _cron_slider_styles_data_remove(self):
        res = self.sudo().search(['|', ('display_name', '=', False), ('style_template_key', '=', False)])
        res.sudo().unlink()
        res = self.env['slider.filter'].sudo().search(['|', ('display_name', '=', False), ('filter_domain', '=', False)])
        res.sudo().unlink()
        cron = self.env.ref('emipro_theme_base.cron_slider_styles_data_remove')
        cron.sudo().unlink()
