# Copyright 2022 Camptocamp (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class FleetVehicleConfiguration(models.Model):
    _inherit = "fleet.vehicle.configuration"

    specific_product_id = fields.Many2one(
        "product.template",
        domain=[("detailed_type", "=", "event")],
        string="Specific Event product",
        help="Event products for the specific max seat counter",
    )
    specific_max_seats = fields.Integer(default=0)
