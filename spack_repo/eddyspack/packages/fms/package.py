# Differs from builtin: adds 2026.02 (the FMS MiMA v2 downloads itself), which needs cmake 3.22; delete once upstream has it.
from spack_repo.builtin.packages.fms.package import Fms as BuiltinFms

from spack.package import *


class Fms(BuiltinFms):
    version("2026.02", sha256="65db44c961089c5e004dd8774cc4cfee75373c4684590d1146c8ff971f8480b7")

    depends_on("cmake@3.22:", type="build", when="@2026.02:")
