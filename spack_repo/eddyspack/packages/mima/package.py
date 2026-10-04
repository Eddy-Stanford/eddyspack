# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install mima
#
# You can edit this file again by typing:
#
#     spack edit mima
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mima(CMakePackage):
    """
    Model of an idealized Moist Atmosphere (MiMA)
    MiMA is an intermediate-complexity General Circulation Model with interactive water vapor and full radiation
   
    """

    homepage = "https://mjucker.github.io/MiMA/"
    url = "https://github.com/Eddy-Stanford/MiMA.git"
    git = "https://github.com/Eddy-Stanford/MiMA.git"

    maintainers("OneOneFour")

    license("GPL-3.0-only", checked_by="OneOneFour")

    version("develop",branch="master")    
    version("1.2.5", tag='v1.2.5', commit='8a4da0da877b699203a8532b39f8f937958b76e7')
    version("1.2.4", tag='v1.2.4', commit='bf454f4dd5ef778ad3ee12bf78a3a5792f2767ad')
    version("1.2.3", tag='v1.2.3', commit='08538c26eb91b6f28db6e2d7c231fee963e43129')
    version("1.2.2", tag='v1.2.2', commit='ca884bec3f66410c8896a1ffc09321f4440caa93')
    version("1.2.1", tag='v1.2.1', commit='631b12c4560620bd2b3c1026c4eac36c26d51ebf')
    version("1.2",tag='v1.2',commit='9c79934187fcfdaa55b671acf515a8d1a655a6b2')
    version("1.1",tag='v1.1',commit='27739db42059ad7a6646dbd4a1df1805798e7218')
    version("1.0",tag='v1.0',commit='6b40f7569aed7d4bbd134b8e9cb53214570a1ddc')

    depends_on("fortran", type="build")
    depends_on("c",type="build")
    depends_on("mpi")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("python")
    
    variant("combine",default=False,description="Build mppnccombine?")

    def cmake_args(self):
        return [self.define_from_variant("BUILD_COMBINE","combine")]
