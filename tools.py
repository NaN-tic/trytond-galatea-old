# This file is part galatea module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from PIL import Image
import logging
import os

try:
    import slug
except ImportError:
    logger = logging.getLogger(__name__)
    logger.error('Unable to import slug. Install slug package.')

IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']


def slugify(value):
    """Convert value to slug: az09 and replace spaces by -"""
    if not slug:
        name = ''
    else:
        if isinstance(value, unicode):
            name = slug.slug(value)
        else:
            name = slug.slug(unicode(value, 'UTF-8'))
    return name


def seo_lenght(string):
    '''Get first 155 characters from string'''
    if len(string) > 155:
        return '%s...' % (string[:152])
    return string


def slugify_file(value):
    """Convert attachment name to slug: az09 and replace spaces by -"""
    if not slug:
        return value
    fname = value.lower().split('.')
    fn = fname[0]
    if isinstance(fn, unicode):
        name = slug.slug(fn)
    else:
        name = slug.slug(unicode(fn, 'UTF-8'))

    if len(fname) > 1:
        return '%s.%s' % (name, fname[1])
    else:
        return name


def thumbly(directory, filename, data, size=300, crop=False):
    '''Create thumbnail image
    :param directory: directory name
    :param filename: file name
    :param data: data image
    :param size: size to thumb
    :param crop: crop thumb image
    '''
    if not os.path.isdir(directory):
        os.makedirs(directory, 0o775)
    os.umask(0o022)
    with open(filename, 'wb') as file_p:
        file_p.write(data)

    # square and thumbnail thumb image
    thumb_size = size, size
    try:
        im = Image.open(filename)
    except:
        if os.path.exists(filename):
            os.remove(filename)
        return False

    if crop:
        width, height = im.size
        if width > height:
            delta = width - height
            left = int(delta / 2)
            upper = 0
            right = height + left
            lower = height
        else:
            delta = height - width
            left = 0
            upper = int(delta / 2)
            right = width
            lower = width + upper
        im = im.crop((left, upper, right, lower))
    im.thumbnail(thumb_size, Image.ANTIALIAS)
    im.save(filename)
    return True
