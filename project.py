# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Work']


class Work(metaclass=PoolMeta):
    __name__ = 'project.work'
    attachments = fields.One2Many('ir.attachment', 'resource', 'Attachments')
