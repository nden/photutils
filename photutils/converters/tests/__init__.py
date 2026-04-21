# Licensed under a 3-clause BSD style license - see LICENSE.rst

ASDF_ASTROPY_INSTALLED = True

try:
    import asdf_astropy
except ImportError:
    ASDF_ASTROPY_INSTALLED = False
