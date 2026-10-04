# Differs from builtin: adds 5.9.1 to match the Sherlock qt external; delete once upstream has it.
from spack_repo.builtin.packages.qt.package import Qt as BuiltinQt

from spack.package import *


class Qt(BuiltinQt):
    version("5.9.1", sha256="7b41a37d4fe5e120cdb7114862c0153f86c07abbec8db71500443d2ce0c89795")
