# -*- coding: utf-8 -*-
'''
    vdirsyncer.storage
    ~~~~~~~~~~~~~~~~~~

    There are storage classes which control the access to one vdir-collection
    and offer basic CRUD-ish methods for modifying those collections. The exact
    interface is described in `vdirsyncer.storage.base`, the `Storage` class
    should be a superclass of all storage classes.

    :copyright: (c) 2014 Markus Unterwaditzer
    :license: MIT, see LICENSE for more details.
'''

from .dav.caldav import CaldavStorage
from .filesystem import FilesystemStorage

storage_names = {
    'caldav': CaldavStorage,
    'filesystem': FilesystemStorage
}
