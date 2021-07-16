"""
MINT
The Generic component for running MD simulations using MMIC
"""

# Add imports here
# from .mmic_md import *
from . import models, components
from .models import *
from .components import *

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions

"""
# The molecule file extensions supported by
# the reader and writers in mmic_md
molread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

molwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# The trajectory file extensions supported by
# the reader and writers in mmic_md
trajread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

trajwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# The force field file extensions supported by
# the readers and writers in mmic_md
ffread_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

ffwrite_ext_maps = {
    ".ext1": "ext1",
    ".ext2": "ext2",
    ".ext3": "ext3",
    ".ext4": "ext4",
    ".ext5": "ext5",
}

# Name to model map for MMElemental
_classes_map = {
    "Molecule": models.The_name_of_the_code_to_translate_mmschema_to/from.Mol,
    "Trajectory": models.The_name_of_the_code_to_translate_mmschema_to/from.Traj,
    "ForceField": models.The_name_of_the_code_to_translate_mmschema_to/from.FF,
}
"""
