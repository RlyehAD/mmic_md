from cmselemental.models.procedures import OutputProc
from .input import InputMD
from mmelemental.models import Molecule
from mmelemental.models.collect import Ensemble, Trajectory
from pydantic import Field
from typing import Optional, Dict, List, Union

__all__ = ["OutputMD"]


class OutputMD(OutputProc):
    proc_input: InputMD = Field(
        ..., description="Input schema used to run MD simulation"
    )
    molecule: Union[Molecule, List[Molecule]] = Field(
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
