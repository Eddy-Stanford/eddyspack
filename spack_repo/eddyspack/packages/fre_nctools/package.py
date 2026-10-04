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
#     spack install fre-nctools
#
# You can edit this file again by typing:
#
#     spack edit fre-nctools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class FreNctools(AutotoolsPackage):
    """
    FRE_NCTOOLS package
    FRE-NCtools is a collection of tools for creating grids and mosaics commonly used in climate and weather models, the remapping of data among grids, and the creation and manipulation of netCDF files. These tools were largely written by members of the GFDL Modeling Systems Group primarily for use in the Flexible Modeling System (FMS) Runtime Environment (FRE) supporting the work of the Geophysical Fluid Dynamics Laboratory (GFDL).
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-GFDL/FRE-NCtools"
    git = "https://github.com/NOAA-GFDL/FRE-NCtools.git"
    url = "https://github.com/NOAA-GFDL/FRE-NCtools/archive/refs/tags/2024.05.02.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("OneOneFour")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("LGPL-3.0-only", checked_by="OneOneFour")

    version("2026.01", sha256="c19f2383072a22e2c80a517932c7dba7a1982cf5631d40dd08b05dc1d882e7fd")
    version("2024.05.02", sha256="013d0dc63027bc4273544a3690a894e0903d5dfc1e62c8830bc8531105995e8a")
    version("2024.05.01", sha256="bb8effba374b68dde892c1dc16611119181ad4f77cf2e64c18f28141315893c7")
    version("2024.05", sha256="61cec52aa03e066b64bed794ef9dc3eb28654c3d1b872aef1b69ce99ef7a9c65")
    version("2024.04", sha256="e27346d7ade1b67af163bb7f327a47a288d5e475fe797323bd7cee3a46385de0")
    version("2024.03", sha256="2835199359c7d1dba6e70c8656f34cfc1ccae3a6a258b5359321024d03def861")
    version("2024.02", sha256="90d52abc1b467d635dd648185b0046efcc6d58a232143b0ccaf9a0bff23d2f5d")
    version("2024.01", sha256="98068a7b16687092af161998351bc16d7117d05098857c34b9fc89d708aa9837")
    version("2023.01.02", sha256="16f75086ed36bfcee00d366c4504c20d97a436223f5250137c35a7c661b1f3f6")
    version("2023.01.01", sha256="7a5eb6fcea996a03287bddeabeedcea2f3fa65f0633d281bd3ab295227b85968")
    version("2023.01", sha256="930119b72e20e72e08cc37ab1422d780a8aba24b2ed84682af9db0c311c449b3")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("nco") 
    depends_on("python@3")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")

        
    variant("mpi",default=False,description="Compile version of tools with MPI Support")
    depends_on("mpi",when="+mpi")
  
    variant("gpu",default=False,description="Build OpenACC version of NC Tools for GPU offloading")
    depends_on("nvhpc",when="+gpu")

    patch("fixdocs_2024_05.patch",when="@2024.05:") 

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        args += self.with_or_without("mpi")
        args += self.enable_or_disable("gpu")
        return args
