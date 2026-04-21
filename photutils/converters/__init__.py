# Licensed under a 3-clause BSD style license - see LICENSE.rst

ASDF_ASTROPY_INSTALLED = True

try:
    import asdf_astropy  # noqa: F401 -- needed to register the converters
    from .functional_models import AiryDiskPSFConverter
    from .apertures import CircularApertureConverter
except ImportError:
    ASDF_ASTROPY_INSTALLED = False

__all__ = [
    'AiryDiskPSFConverter',
    'CircularApertureConverter',
]
