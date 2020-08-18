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
#     spack install folly
#
# You can edit this file again by typing:
#
#     spack edit folly
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Folly(CMakePackage):
    """Folly (acronymed loosely after Facebook Open Source Library) is a
    library of C++11 components designed with practicality and efficiency
    in mind.

    Folly contains a variety of core library components used extensively at
    Facebook. In particular, it's often a dependency of Facebook's other open
    source C++ efforts and place where those projects can share code.
    """

    homepage = "https://github.com/facebook/folly"
    url      = "https://github.com/facebook/folly/archive/v2020.06.15.00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('2020.06.29.00', sha256='d057c33ace39373635b908580be90307e23b0d3b3185c37006952151b551e4b9')
    version('2020.06.01.00', sha256='75b2f24790eb213cc96979b916bdafa4d5b4e8a7a1461f8c87cc53828ae19896')
    version('2020.05.25.00', sha256='bceb726307fd63f31dc4e3ae89f0c461bae5aa75d08f7115ef0a2cb7ac40d519')
    version('2020.05.18.00', sha256='b52bc43fbac951d73f35dfaef304a81d7e41f9aecec1c83440a809677e16fe86')
    version('2020.05.11.00', sha256='8c2f4927546220ad141c6807915293ea5c1b120d5e36d13ea380ddda96b1d05e')
    version('2020.05.04.00', sha256='8c3b373e8423dbecd465bfac0d3a6b2954ba2c20ee3e8babb2c05c5e331b8440')
    version('2020.04.27.00', sha256='212a9f680b16f7c742cddf7f51b180c592cb8df75d4037e737f85e1335c0ebcc')
    version('2020.04.20.00', sha256='9a50986b0a71c2d8cdf6285a6ab67839ddde698fb23512f929b5601b221a0e86')
    version('2020.04.13.00', sha256='369d17a6603c1dc53db006bd5d613461b76db089bd90a85a713565c263497082')

    depends_on('libtool', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('cmake', type='build')

    # TODO: folly requires gcc 4.9+ and a version of boost compiled with
    # TODO: C++14 support (but there's no neat way to check that these
    # TODO: constraints are met right now)
    depends_on('boost cxxstd=11 +context')
    
    # these are needed but cmake can't link to them in spacks prefix... 
    #    depends_on('glog')
    #    depends_on('gflag')
    depends_on('libelf')
    depends_on('libsodium')
    depends_on('double-conversion')
    depends_on('libevent')
    patch("atomic.patch")
    def cmake_args(self):
        # CMAKE prefix is needed because of LIBATOMIC
        return ['--debug-trycompile', '-DCMAKE_LIBRARY_PATH:PATH=/usr/lib64', '-DCMAKE_PREFIX_PATH=/usr']
    
