from odoo import fields, models,api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    total_volume = fields.Float(compute="_compute_total_volume")

    @api.depends('move_line_ids')
    def _compute_total_volume(self):
        for res in self:
            total = res.move_line_ids
            initial_volume=0
            for record in total:
                initial_volume+=record.product_id.volume * record.quantity
            res.total_volume=initial_volume
