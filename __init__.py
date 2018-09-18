# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import attachment
from . import galatea
from . import configuration
from . import static_file
from . import party
from . import sale
from . import invoice
from . import project


def register():
    Pool.register(
        attachment.Attachment,
        configuration.Configuration,
        galatea.GalateaWebSite,
        galatea.GalateaWebsiteCountry,
        galatea.GalateaWebsiteLang,
        galatea.GalateaWebsiteCurrency,
        galatea.GalateaUser,
        galatea.GalateaUserWebSite,
        galatea.GalateaRemoveCacheStart,
        galatea.GalateaSendPasswordStart,
        galatea.GalateaSendPasswordResult,
        static_file.GalateaStaticFolder,
        static_file.GalateaStaticFile,
        party.Party,
        module='galatea', type_='model')
    Pool.register(
        sale.Sale,
        depends=['sale'],
        module='galatea', type_='model')
    Pool.register(
        invoice.Invoice,
        depends=['account_invoice'],
        module='galatea', type_='model')
    Pool.register(
        project.Work,
        depends=['project'],
        module='galatea', type_='model')
    Pool.register(
        galatea.GalateaRemoveCache,
        galatea.GalateaSendPassword,
        module='galatea', type_='wizard')
