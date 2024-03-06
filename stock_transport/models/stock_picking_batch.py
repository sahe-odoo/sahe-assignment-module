from odoo import fields, models,api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock")
    vehicle_id = fields.Many2one("fleet.vehicle.odometer")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category")
    weight = fields.Float(compute="_compute_weight",store=True)
    volume = fields.Float(compute="_compute_volume",store=True)
    transfers = fields.Integer(compute="_compute_transfers",store=True)
    lines = fields.Integer(compute="_compute_lines",store=True)

    @api.depends('picking_ids.move_line_ids')
    def _compute_lines(self):
        self.lines = len(self.picking_ids.move_line_ids)

    @api.depends('picking_ids.move_line_ids')
    def _compute_transfers(self):
        self.transfers = len(self.picking_ids.move_line_ids.picking_id)

    @api.depends('picking_ids.move_line_ids.product_id.weight','picking_ids.move_line_ids','vehicle_category_id.max_weight')
    def _compute_weight(self):
        for res in self:
            total = res.picking_ids.move_line_ids
            total_weight=0
            for record in total:
                total_weight+=record.product_id.weight * record.quantity
            res.weight = (total_weight/(res.vehicle_category_id.max_weight if res.vehicle_category_id.max_weight else 1))*100

    @api.depends('picking_ids.move_line_ids.product_id.volume','picking_ids.move_line_ids','vehicle_category_id.max_volume')
    def _compute_volume(self):
        for res in self:
            total = res.picking_ids.move_line_ids
            total_volume=0
            for record in total:
                total_volume+=record.product_id.volume * record.quantity
            res.volume = (total_volume/(res.vehicle_category_id.max_volume if res.vehicle_category_id.max_volume else 1))*100

    def _compute_display_name(self):
        for record in self:
            name = record.name
            if name:
                name = f"{record.name}: {record.weight if record.weight else 0}kg, {record.volume if record.volume else 0}m\u00b3"
            record.display_name = name
