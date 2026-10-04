# Differs from builtin: adds 1.12.0-1.14.0, g2c-link/test patches, pins bacio@2.4.1; delete once upstream has them.
from spack_repo.builtin.packages.ufs_utils.package import UfsUtils as BuiltinUfsUtils

from spack.package import *


class UfsUtils(BuiltinUfsUtils):
    version(
        "1.14.0",
        tag="ufs_utils_1_14_0",
        commit="ae64734226402fcb438ce4feed5a43829b47342e",
        submodules=True,
    )
    version(
        "1.13.0",
        tag="ufs_utils_1_13_0",
        commit="cadff2ba1a4ec048700b7d7bdf4602ad87186545",
        submodules=True,
    )
    version(
        "1.12.3",
        tag="ufs_utils_1_12_3",
        commit="9040c825eed77da843879176800009438575325e",
        submodules=True,
    )
    version(
        "1.12.0",
        tag="ufs_utils_1_12_0",
        commit="5585ebb30f30a3f25284fa2d9890dcc361d454b2",
        submodules=True,
    )

    depends_on("bacio@2.4.1")

    patch("g2c_dep_1_11_0.patch", when="@1.11.0")
    patch("broken_test_1_12_3.patch", when="@1.12.3")
    patch("g2c_dep_1_12_0.patch", when="@1.12.3")
    patch("g2c_dep_1_12_0.patch", when="@1.12.0")
    patch("g2c_dep_1_14_0.patch", when="@1.14.0")
