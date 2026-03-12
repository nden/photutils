# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
Tests for the photutils PSF converters.
"""
import asdf
from astropy import units as u

from photutils.psf import (
    AiryDiskPSF,
    CircularGaussianPRF,
    CircularGaussianPSF,
    CircularGaussianSigmaPRF,
)

psfs = {
    'AiryDiskPSF': [
        AiryDiskPSF(flux=1 * u.Jy, x_0=0 * u.arcsec, y_0=0 * u.arcsec,
                    radius=1 * u.arcsec, bbox_factor=2),
        AiryDiskPSF(flux=2 * u.Jy, x_0=1 * u.arcsec, y_0=1 * u.arcsec,
                    radius=2 * u.arcsec, bbox_factor=3),
    ],
    'CircularGaussianPRF': [
        CircularGaussianPRF(flux=1 * u.Jy, x_0=0 * u.arcsec, y_0=0 * u.arcsec,
                            fwhm=1 * u.arcsec, bbox_factor=2),
        CircularGaussianPRF(flux=2 * u.Jy, x_0=1 * u.arcsec, y_0=1 * u.arcsec,
                            fwhm=2 * u.arcsec, bbox_factor=3),
    ],
    'CircularGaussianPSF': [
        CircularGaussianPSF(flux=1 * u.Jy, x_0=0 * u.arcsec, y_0=0 * u.arcsec,
                            fwhm=1 * u.arcsec, bbox_factor=2),
        CircularGaussianPSF(flux=2 * u.Jy, x_0=1 * u.arcsec, y_0=1 * u.arcsec,
                            fwhm=2 * u.arcsec, bbox_factor=3),
    ],
    'CircularGaussianSigmaPRF': [
        CircularGaussianSigmaPRF(flux=1 * u.Jy, x_0=0 * u.arcsec, y_0=0 * u.arcsec,
                            sigma=1 * u.arcsec, bbox_factor=2),
        CircularGaussianSigmaPRF(flux=2 * u.Jy, x_0=1 * u.arcsec, y_0=1 * u.arcsec,
                            sigma=2 * u.arcsec, bbox_factor=3),
    ],
}


parameters = {
    'AiryDiskPSF': ['flux', 'x_0', 'y_0', 'radius', 'bbox_factor'],
    'CircularGaussianPRF': ['flux', 'x_0', 'y_0', 'fwhm', 'bbox_factor'],
    'CircularGaussianPSF': ['flux', 'x_0', 'y_0', 'fwhm', 'bbox_factor'],
    'CircularGaussianSigmaPRF': ['flux', 'x_0', 'y_0', 'sigma', 'bbox_factor'],
}


def test_psf_converters(tmp_path):
    """
    Test that the PSF converters can round-trip a PSF object.
    """
    for psf, instances in psfs.items():
        for instance in instances:
            with asdf.AsdfFile() as af:
                af['psf'] = instance
                af.write_to(tmp_path / 'psf.asdf')

            with asdf.open(tmp_path / 'psf.asdf') as af:
                psf2 = af['psf']

            for parameter in parameters[psf]:
                assert getattr(instance, parameter) == getattr(psf2, parameter)
