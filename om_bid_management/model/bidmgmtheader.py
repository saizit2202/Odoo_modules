# -*- coding: utf-8 -*-
from contextlib import contextmanager

from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError
from odoo.tools import create_index
from odoo.tools.misc import formatLang

class BidManagementHeader(models.Model):
    _name = "bid.bidmgmtheader"
    _description = "Bid Management Header"

    name = fields.Char(
        string='name',
    )

    bidno = fields.Char(string="bidno", required=True)

