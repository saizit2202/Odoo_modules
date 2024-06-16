# -*- coding: utf-8 -*-
from contextlib import contextmanager

from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError
from odoo.tools import create_index
from odoo.tools.misc import formatLang

class SalesOrder(models.Model):
    _name = "sales.salesorder"
    _description = "Sales Order"

    name = fields.Char(
        string='name',
    )

