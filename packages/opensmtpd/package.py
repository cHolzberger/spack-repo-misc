# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install opensmtpd
#
# You can edit this file again by typing:
#
#     spack edit opensmtpd
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Opensmtpd(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/OpenSMTPD/OpenSMTPD/releases/download/6.7.1p1/opensmtpd-6.7.1p1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('6.7.1p1', sha256='7478e918b41e734a39ad082df55cb2607f0933a506fab2c3dd3554a95cdf08ca')
    version('6.7.0p1', sha256='c13f5dd7b9cb9421eabb62068537d90b0441cdb3ca2e5c1e753d7aee01b90bb9')
    version('6.6.4p1', sha256='e2f9962a6b99b3cc1572b63a10db648fdca4ad2b58079b680b4202cc7c82d7cf')
    version('6.6.3p1', sha256='9ef7c0eb7ffc5c84dca7651cec69bd7b180014cd5227f6dbc7a303eaa9d41eb7')
    version('6.6.2p1', sha256='63b811aca56861108bb72f16fcbbf32f1af71e77b8996a9a5654b6a18915df9a')
    version('6.6.1p1', sha256='eb1bedbfb23d9f08f509d92d8efcaf51d56fb2f44492f40ec059d41124a2f1d9')
    version('6.6.1',   sha256='1d0e2bf5371ab172304969dc19a9c23af1b0f60392d5e7252134fe1967cc9040')

    # FIXME: Add dependencies if required.
    depends_on('libevent')
    depends_on('libtool')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
