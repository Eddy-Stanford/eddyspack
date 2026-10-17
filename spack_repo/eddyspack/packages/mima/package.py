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
    url = "https://github.com/Eddy-Stanford/MiMA/archive/refs/tags/v2.0.0.tar.gz"
    git = "https://github.com/Eddy-Stanford/MiMA.git"

    maintainers("OneOneFour")
    license("GPL-3.0-only", checked_by="OneOneFour")

    version("develop", branch="main")
    # Uncomment once v2.0.0 is tagged and pushed (fill in its full 40-character commit).
    # Until then, build the v2 branch with: spack install mima@git.v2=2.0.0
    version("2.0.0", sha256="1bb10d8119570282a8bcdf9aa96bf4036667c5a88cb7bc0e5a35f81d09db9d5e")
    version("1.2.5", sha256="8ad711041aff617b32a56237f8cfb8295aa77cd4cf32af0586a371f9ee0818e4")
    version("1.2.4", sha256="d4c3b8ecc47825676493c247f5ebf5d9dd77920ad8b17922fa8fe9f8b989e77f")
    version("1.2.3", sha256="07f3342ff32641ed0cc81373c4f129e85093d9a80a936ee635c76ac743d3bc9a")
    version("1.2.2", sha256="0d815f89ff811550d8c535b94410eac173fb008c43b6e4adffde9e887e4ddf57")
    version("1.2.1", sha256="bbad00d5e936cc614df67c62c5198c49a02cdb188578e99f03a6c632f612b58c")
    version("1.2", sha256="8634e1df1e100689a86a0f39a70b61038d62611d226723f0fa5a36652ee22082")
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
