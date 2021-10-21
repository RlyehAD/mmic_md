"""
Components in mmic_md.
"""

from typing import List, Tuple, Optional

# Import the generic i.e. starting component from MMIC
from mmic.components.blueprints.generic_component import GenericComponent
from mmic.components.blueprints import StrategyComponent
from cmselemental.util.decorators import classproperty

from ..models.input import MDInput
from ..models.output import MDOutput


__all__ = ["MDComponent"]


class MDComponent(StrategyComponent):
	""" A sample component that reads in a Molecule and returns a ForceField object. """

	@classproperty
	def input(cls):
		return MDInput

	@@classproperty
	def output(cls):
		return MDOutput

    @classproperty
    def version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        return ""

	@classproperty
	def tactic_comps(self) -> Set[str]:
		"""Returns the supported components e.g. set(['mmic_mda',...]).
		Returns
		-------
		Set[str]
		"""
		return set(["mmic_md_openmm","mmic_md_gmx"])
