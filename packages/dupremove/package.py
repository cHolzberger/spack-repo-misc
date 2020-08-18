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
#     spack install dupremove
#
# You can edit this file again by typing:
#
#     spack edit dupremove
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Dupremove(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/markfasheh/duperemove/archive/v0.11.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.11.1',     sha256='75c3c91baf7e5195acad62eab73a7afc3d0b88cbfccefac3e3412eba06a42ac8')
    version('0.11.beta4', sha256='fdccc29670c39e36751217263bef0f7d0803c3773b0bbb61fcd651370798b6c0')
    version('0.11.beta3', sha256='d9a1d484193a42ca2362fefc9b82b6e40a7e302750a0ec5ccf3c4367d006df0d')
    version('0.11.beta2', sha256='aea377e09cd87ae6c9b6b73601a959d9462ce4961de2512ae3001262be2f67e9')
    version('0.11.beta1', sha256='f3862cd277df733fd00ccaec22dad25fee5c36e20ebf77082acf466f8d869fbd')
    version('0.11',       sha256='854735ae5e47527afbe5e07712753b498fd93966615c6d645189632f08ac5566')
    version('0.10.beta4', sha256='98482640e5de63069d70e4f1d27613554b62e5246fb27e842ebd7c1ce1af570b')
    version('0.10.beta3', sha256='000555d6a640e97449ff5b84c93471c54fd44f929c08e85186e5565eb976fb69')
    version('0.10',       sha256='1ef855c4d0a85efc8757edcac5ea7189d896d2f2abad0e572c47f6568cf050aa')
    version('0.09.5',     sha256='8c8c781ab53435dfcc114d2a500525c72428fdbafc14ead10de115d77b447b69')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    patch("gcc10.patch")
    #def edit(self, spec, prefix):
        

