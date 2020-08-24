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
#     spack install motion
#
# You can edit this file again by typing:
#
#     spack edit motion
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Motion(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/Motion-Project/motion/archive/release-4.3.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.3.1', sha256='545712b10fc4a0134e994b7d8a3773c1c22f0bf4bd7afea7d7ffff357aca9ea5')
    version('4.3.0', sha256='567c385af81130f7883e4c417c34c0d6dc82ddba47b94478831f973e0f3ef02b')
    version('4.2.2', sha256='c8d40976b41da8eb9f9f7128599403a312fc26b7226bf3787d75f78cb5a6cc6e')
    version('4.2.1', sha256='d97ec6ae766adfd478b6f7f9cc0da5f2fe21faa9366d98664be255714c1cf81d')
    version('4.2',   sha256='6ef8504fc5be00a49c82c4045c0004fbf575d9a5df8687025a9b06923efda2a9')
    version('4.1.1', sha256='2074b935bdfe28f84c2c3233274b06908336778f303bb13530d4299c3f8aa4e2')
    version('4.1',   sha256='277029c80df0d37deefbbea6d15c66a9067d9166fe8f76eb5f90aa6e97aa9741')
    version('4.0.1', sha256='2f67669a09ce0481ecd987028dae1c5cb135dfdc3c254c06ab7c9ca0c6c183f0')
    version('4.0',   sha256='a3c576971d990dae3fb02038a04d020435bf86dfe0cfe23e1ffa0c23b569922e')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('libjpeg-turbo' )

    # FIXME: Add additional dependencies if required.
    # depends_on('foo')
    depends_on('ffmpeg')
    #depends_on("libmicrohttpd")

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
