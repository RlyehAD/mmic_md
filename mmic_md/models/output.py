from cmselemental.models.procedures import ProcOutput
from .input import MDInput
from mmelemental.models import Molecule, Ensemble, Trajectory
from pydantic import Field
from typing import Optional, Dict, List

__all__ = ["MDOutput"]


class MDOutput(ProcOutput):
    proc_input: MDInput = Field(
        ..., description="Input schema used to run optimization"
    )
    molecule: Dict[str, Molecule] = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``Molecule`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    ensemble: Optional[Dict[str, Ensemble]] = Field(
        None,
        description="Ensemble output for a series of microstates of molecules. "
        "See the :class:``Ensemble`` class.",
    )
    trajectory: Optional[Dict[str, Trajectory]] = Field(
        None,
        description="Trajectory output representing a series of snapshots of the system at "
        "different timesteps. See the :class:``Trajectory`` class.",
    )
