# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .attachment import *
from .galatea import *
from .configuration import *
from .static_file import *
from .party import *
from .sale import *
from .invoice import *
from .project import *

def register():
    Pool.register(
        Attachment,
        Configuration,
        GalateaWebSite,
        GalateaWebsiteCountry,
        GalateaWebsiteCurrency,
        GalateaUser,
        GalateaUserWebSite,
        GalateaRemoveCacheStart,
        GalateaSendPasswordStart,
        GalateaSendPasswordResult,
        GalateaStaticFolder,
        GalateaStaticFile,
        Party,
        Sale,
        Invoice,
        Work,
        module='galatea', type_='model')
    Pool.register(
        GalateaRemoveCache,
        GalateaSendPassword,
        module='galatea', type_='wizard')
