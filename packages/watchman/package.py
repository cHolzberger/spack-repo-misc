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
#     spack install watchman
#
# You can edit this file again by typing:
#
#     spack edit watchman
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Watchman(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/facebook/watchman/archive/v2020.06.15.00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('2020.06.29.00', sha256='13a95bf56cea60b703e717bea2adba9dbb4a8f229e2e84f4896fe42d7df51230')
    version('2020.06.15.00', sha256='e1633e0f54d62742a0da96d40aaeb12caa8dada5c3c849b061ae643c8b5b8e76')
    version('2020.06.08.00', sha256='d9f28dbe1cb9bf60ea3702c3030e5b75c463b62bb22e71989f594675945e27b8')
    version('2020.06.01.00', sha256='6a8151d369428d69b285983206882d9e0c0cb5713b74c39d25bd987274772303')
    version('2020.05.25.00', sha256='271009a9c5d39c33a87c9cde8fc8b4b8018b3030f1a7afb92c61c48e3481400f')
    version('2020.05.18.00', sha256='fd0a5bad223e791eb37f59c5bb1dad3fd7dc94383c9f206d0dd74ba9e784edeb')
    version('2020.05.11.00', sha256='701b8d2dbf50d397ffabc86b814c2592e53ca54df7f831cedb4fa3d88c345708')
    version('4.9.0-rc1',     sha256='3ecfe4a98da790fabcaca553d2f02b6ad9c28a9b0948c03fa5247e9138ed29ec')
    version('4.9.0',         sha256='1f6402dc70b1d056fffc3748f2fdcecff730d8843bb6936de395b3443ce05322')
    version('4.8.0-rc1',     sha256='fc921cbe39606b604d81285897317985a17de4d7b4b56ec0a5922db893955c1b')
    version('4.7.0',         sha256='77c7174c59d6be5e17382e414db4907a298ca187747c7fcb2ceb44da3962c6bf')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('boost')
    depends_on('glog')
    depends_on('fmt')
    depends_on('folly@2020.06.15.00')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
