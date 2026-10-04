# Differs from builtin: adds 1.14.10 to match the Sherlock cairo external; delete once upstream has it.
from spack_repo.builtin.packages.cairo.package import Cairo as BuiltinCairo

from spack.package import *


class Cairo(BuiltinCairo):
    version("1.14.10", sha256="7e87878658f2c9951a14fc64114d4958c0e65ac47530b8ac3078b2ce41b66a09")
