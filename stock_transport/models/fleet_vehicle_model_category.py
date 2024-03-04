from odoo import fields, models,api

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float('Max Weight(Kg)')
    max_volume = fields.Float('Max Volume(m3)')

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if name:
                name = f"{record.name}({record.max_weight}kg, {record.max_volume}m3)"
            record.display_name = name
