from mmelemental.models.proc.base import ProcInput
from mmelemental.models import Molecule, ForceField, ForcesInput, TrajInput
from pydantic import Field, validator
from typing import Optional, Dict, List, Tuple

__all__ = ["MDInput"]


class MDInput(ProcInput):
    """Basic input model for MD run."""

    # System fields
    molecule: Dict[str, Molecule] = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``Molecule`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    forcefield: Dict[str, ForceField] = Field(
        ...,
        description='Forcefield object(s) or name(s) for every Molecule defined in "mol".',
    )
    cell: Optional[Tuple[Tuple[float], Tuple[float]]] = Field(
        None,
        description="Cell dimensions in the form: ((xmin, ymin, ...), (xmax, ymax, ...))",
    )
    boundary: List[str] = Field(
        None,
        description="Boundary conditions in all dimensions e.g. (periodic, periodic, periodic) imposes periodic boundaries in 3D.",
    )

    # I/O fields
    trajectory: Optional[Dict[str, TrajInput]] = Field(
        None,
        description="Trajectories to write for quantity 'key' every 'value' steps. e.g. {'geometry_freq': 10, 'velocities_freq': 100, 'forces_freq': 50} "
        "produces 3 trajectory objects storing positions every 10 steps, velocities, every 100 steps, and forces every 50 steps.",
    )

    # Global fields
    max_steps: int = Field(
        None, description="Max number of optimization steps to perform."
    )
    step_size: float = Field(None, description="Step size for constant step marching.")
    step_size_units: Optional[str] = Field(
        None,
        description="Step size unit. Any unit supported by pint is allowed. If not defined, it's set to fs",
    )

    # Algorithmic fields
    method: str = Field(
        None,
        description="The integrator used for MD simulation. e.g. 'md-vv'",
    )

    # Output control
    F_xout: float = Field(
        Optional,
        description="The frequency for the simulation to write a frame of coordinates",
    )
    F_vout: float = Field(
        Optional,
        description="The frequency for the simulation to write the velocities",
    )
    F_eout: float = Field(
        Optional,
        description="The frequency for the simulation to write the energies",
    )
    F_fout: float = Field(
        Optional,
        description="The frequency for the simulation to write the forces",
    )
    # A F for log file output?
    F_stdout: float = Field(
        Optional,
        description="The frequecy for writing an standard output including info of T, P, E, and so on",
    )
    F_unit: str = Field(
        Optional,
        description="The unit for the frequencies to write coordinates, velocities, and energies",
    )  # May be deleted

    # Bonded interaction
    unconstrained_start: str = Field(
        None,
        description="To determine if constraints are applied to the initial configuration. It's no by default",
    )  # May be deleted
    constraint_method: str = Field(
        None,
        description="The algorithm used for constranits. e.g. 'SHAKE'",
    )
    constraints: str = Field(
        None,
        description="The bonds that are constrained",
    )  # May be replaced by bond_const

    # Nonbonded interaction
    short_forces: ForcesInput = Field(
        ..., description="Algorithms for computing short-range forces."
    )  

    long_forces: ForcesInput = Field(
        ..., description="Algorithms for computing long-range forces."
    )
    cut_off: str = Field(..., description="Neighbor searching algorithm")

    # Temperature and pressure coupling
    t_couple: str = Field(None, description="Temperature coupling algorithm")
    p_couple: str = Field(None, description="Pressure coupling algorithm")
    ref_t: float = Field(None, description="The reference temperature")
    ref_p: float = Field(None, description="The reference pressure")
