# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Attachment']


class Attachment(metaclass=PoolMeta):
    __name__ = 'ir.attachment'
    allow_galatea = fields.Boolean('Allow Galatea', select=True)
    galatea_session = fields.Boolean('Galatea Session',
        help='Allow attachment to login users')
    galatea_party = fields.Boolean('Galatea Party',
        help='Allow attachment to party (login user)')
