# -*- coding: utf-8 -*-
"""
Marz Workbench for FreeCAD 0.19+.
https://github.com/mnesarco/MarzWorkbench
"""

__author__       = "Frank D. Martinez. M."
__copyright__    = "Copyright 2020, Frank D. Martinez. M."
__license__      = "GPLv3"
__maintainer__   = "https://github.com/mnesarco"


import hashlib

import marz_math as xmath
from marz_linexy import lineIntersection, linexy
from marz_vxy import vxy
from marz_neck_profile_list import getNeckProfile

class BodyData(object):
    """
    Body reference constructions
    """

    #! Using __slots__ to make this class Immutable.
    #! Immutability is required here because instances of 
    #! this object will be cached as a hash calculated on creation,
    #! so two instances created with same data will hit the same
    #! cache entry.
    __slots__ = ['neckd', 'length', 'width', 'backThickness', 'topOffset',
        'topThickness', 'neckPocketDepth', 'neckAngle', 'neckPocketLength', '_ihash']

    def __init__(self, inst, neckd):

        # Set immutable values
        super().__setattr__('length', inst.body.length)
        super().__setattr__('width', inst.body.width)
        super().__setattr__('backThickness', inst.body.backThickness)
        super().__setattr__('topThickness', inst.body.topThickness)
        super().__setattr__('neckPocketDepth', inst.body.neckPocketDepth)
        super().__setattr__('neckPocketLength', inst.body.neckPocketLength)
        super().__setattr__('neckAngle', inst.neck.angle)
        super().__setattr__('topOffset', inst.neck.topOffset)
        super().__setattr__('neckd', neckd)
        
        # Calculate immutable hash
        keys = ":".join([repr(v) for v in [
            inst.body.length, 
            inst.body.width, 
            inst.body.backThickness, 
            inst.body.topThickness, 
            inst.body.neckPocketDepth, 
            inst.body.neckPocketLength,
            inst.neck.angle,
            neckd
        ]])
        super().__setattr__('_ihash', hashlib.md5(keys.encode()).hexdigest())

    def __setattr__(self, name, value):
        raise AttributeError(f"{self.__class__.__name__}.{name} is not writable.")

    #! IMPORTANT: Used for caching
    #! Must represent the complete state of the instance
    def __repr__(self):
        return self._ihash

    def totalThickness(self):
        return self.topThickness + self.backThickness

    def totalThicknessWithOffset(self):
        return self.totalThickness() + self.topOffset