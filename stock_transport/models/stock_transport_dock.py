from odoo import fields, models,api

class StockTransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "Stock transport Dock"

    name=fields.Char()
