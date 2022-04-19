# Copyright 2022 Camptocamp (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class FleetVehicleConfiguration(models.Model):
    _inherit = "fleet.vehicle.configuration"

    product_ids = fields.Many2many(
        "product.template",
        domain=[("detailed_type", "=", "event")],
        string="Event products",
        help="Event products for the max seat counter",
    )
