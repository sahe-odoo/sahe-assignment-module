from odoo import fields, models,api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    total_volume = fields.Float(compute="_compute_total_volume")

    @api.depends('move_line_ids')
    def _compute_total_volume(self):
        total = self.move_line_ids
        for record in total:
            record.total_volume = total.quantity * total.parent_id.volume
