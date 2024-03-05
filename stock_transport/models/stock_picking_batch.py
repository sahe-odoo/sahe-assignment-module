from odoo import fields, models,api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock")
    vehicle_id = fields.Many2one("fleet.vehicle.odometer")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category")
    weight = fields.Float(compute="_compute_weight",store=True,precompute=True)
    volume = fields.Float(compute="_compute_volume",store=True,precompute=True)

    @api.depends('weight')
    def _compute_weight(self):
        total = self.picking_ids.move_line_ids
        total_weight=0
        for record in total:
            total_weight+=record.product_id.weight * record.quantity
        self.weight = (total_weight/(self.vehicle_category_id.max_weight if self.vehicle_category_id.max_weight else 1))*100

    @api.depends('volume')
    def _compute_volume(self):
        total = self.picking_ids.move_line_ids
        total_volume=0
        for record in total:
            total_volume+=record.product_id.volume * record.quantity
        self.volume = (total_volume/(self.vehicle_category_id.max_volume if self.vehicle_category_id.max_volume else 1))*100

    def _compute_display_name(self):
        for record in self:
            name = record.name
            if name:
                name = f"{record.name}: {record.weight}kg, {record.volume}m3"
            record.display_name = name
