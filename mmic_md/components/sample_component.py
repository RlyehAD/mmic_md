"""
Components in mmic_md.
"""

from typing import List, Tuple, Optional

# Import the generic i.e. starting component from MMIC
from mmic.components.blueprints.generic_component import GenericComponent

from ..models.input import MDInput
from ..models.output import MDOutput


__all__ = ["MDComponent"]


class MDComponent(GenericComponent):
	""" A sample component that reads in a Molecule and returns a ForceField object. """

	@classmethod
	def input(cls):
		return MDInput

	@classmethod
	def output(cls):
		return MDOutput


	@property
	def supported_comps(self) -> Set[str]:
		"""Returns the supported components e.g. set(['mmic_mda',...]).
		Returns
		-------
		Set[str]
		"""
		return set(["mmic_md_openmm","mmic_md_gmx"])
