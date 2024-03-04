from odoo import fields, models,api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock")
    vehicle_id = fields.Many2one("fleet.vehicle.odometer")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category")
    weight = fields.Float(compute="_compute_weight")
    volume = fields.Float(compute="_compute_volume")
    total_volume = fields.Float(compute="_compute_total_volume")

    @api.depends('picking_ids')
    def _compute_weight(self):
        total = self.picking_ids.move_line_ids
        total_weight=0
        for record in total:
            total_weight+=record.product_id.weight * record.quantity
        self.weight = (total_weight/self.vehicle_category_id.max_weight)*100

    @api.depends('picking_ids')
    def _compute_volume(self):
        total = self.picking_ids.move_line_ids
        total_volume=0
        for record in total:
            total_volume+=record.product_id.volume * record.quantity
        self.volume = (total_volume/self.vehicle_category_id.max_volume)*100
