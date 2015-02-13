# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton

__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    'Galatea Configuration'
    __name__ = 'galatea.configuration'
