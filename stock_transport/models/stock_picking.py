from odoo import fields, models,api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    total_volume = fields.Float(compute="_compute_total_volume")

    @api.depends('total_volume')
    def _compute_total_volume(self):
        total = self.move_line_ids
        for record in total:
            self.total_volume=record.product_id.volume * record.quantity
