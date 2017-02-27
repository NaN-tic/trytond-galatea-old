# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Attachment']


class Attachment:
    __name__ = 'ir.attachment'
    __metaclass__ = PoolMeta
    allow_galatea = fields.Boolean('Allow Galatea', select=True)
