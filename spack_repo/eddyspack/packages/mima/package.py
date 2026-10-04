# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mima(CMakePackage):
    """
    Model of an idealized Moist Atmosphere (MiMA)
    MiMA is an intermediate-complexity General Circulation Model with interactive water vapor and full radiation

    """

    homepage = "https://eddy-stanford.github.io/MiMA/"
    git = "https://github.com/Eddy-Stanford/MiMA.git"

    maintainers("OneOneFour")
    license("GPL-3.0-only", checked_by="OneOneFour")

    version("develop", branch="main")
    # Uncomment once v2.0.0 is tagged and pushed (fill in its full 40-character commit).
    # Until then, build the v2 branch with: spack install mima@git.v2=2.0.0
    # version("2.0.0", tag="v2.0.0", commit="<full commit of v2.0.0>")
    version("1.2.5", tag="v1.2.5", commit="8a4da0da877b699203a8532b39f8f937958b76e7")
    version("1.2.4", tag="v1.2.4", commit="bf454f4dd5ef778ad3ee12bf78a3a5792f2767ad")
    version("1.2.3", tag="v1.2.3", commit="08538c26eb91b6f28db6e2d7c231fee963e43129")
    version("1.2.2", tag="v1.2.2", commit="ca884bec3f66410c8896a1ffc09321f4440caa93")
    version("1.2.1", tag="v1.2.1", commit="631b12c4560620bd2b3c1026c4eac36c26d51ebf")
    version("1.2", tag="v1.2", commit="9c79934187fcfdaa55b671acf515a8d1a655a6b2")
    version("1.1", tag="v1.1", commit="27739db42059ad7a6646dbd4a1df1805798e7218")
    version("1.0", tag="v1.0", commit="6b40f7569aed7d4bbd134b8e9cb53214570a1ddc")

    variant(
        "combine", default=False, description="Build mppnccombine?", when="@1.2.1:1.2.5"
    )
    variant("openmp", default=True, description="Build with OpenMP", when="@2:")

    # v1.0 and v1.1 predate the CMake build (they use mkmf)
    conflicts("@:1.1", msg="MiMA v1.0 and v1.1 predate the CMake build; use v1.2 or newer")

    depends_on("fortran", type="build")
    depends_on("c", type="build")
    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@2:")

    depends_on("mpi")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("python", when="@:1.2.5")

    # v2 builds against an external FMS. FMS 2026.01 crashes when writing restarts
    # on more than one PE. MiMA needs 8-byte reals (precision=mixed or 64) and
    # the GFDL constants.
    depends_on("fms@2026.01.01: precision=mixed constants=GFDL", when="@2:")
    # Match FMS's OpenMP to MiMA's, as MiMA does when it builds FMS itself
    depends_on("fms+openmp", when="@2: +openmp")
    depends_on("fms~openmp", when="@2: ~openmp")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@1.2.1:1.2.5"):
            args.append(self.define_from_variant("BUILD_COMBINE", "combine"))
        if self.spec.satisfies("@1.2.1:"):
            # INSTALL_EXEC overrides CMAKE_INSTALL_PREFIX with the source tree; keep it off
            args.append(self.define("INSTALL_EXEC", False))
        if self.spec.satisfies("@2:"):
            args.append(self.define_from_variant("MIMA_OPENMP", "openmp"))
            args.append(self.define("FMS_ROOT", self.spec["fms"].prefix))
            # Fail rather than download FMS if Spack's FMS is not accepted
            args.append(self.define("FETCHCONTENT_FULLY_DISCONNECTED", True))
        return args
