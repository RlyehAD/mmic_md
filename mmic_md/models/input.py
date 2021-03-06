from cmselemental.models.procedures import InputProc
from mmelemental.models.base import ProtoModel
from mmelemental.models import Molecule
from mmelemental.models.forcefield import ForceField
from mmelemental.util.units import (
    LENGTH_DIM,
    MASS_DIM,
    TIME_DIM,
    SUBS_DIM,
)
from pydantic import Field, validator
from typing import Optional, Dict, List, Tuple, Any, Union

__all__ = ["InputMD"]


class InputForces(ProtoModel):
    method: str = Field(
        ..., description="The algorithm used to compute the force. e.g. PME"
    )

    cutoff: Optional[float] = Field(None, description="The cut-off distance")

    cutoff_units: Optional[str] = Field(
        "angstrom", description="The unit of cutoff distance",
        dimensionality=LENGTH_DIM,
    )

        
class InputTraj(ProtoModel):
    geometry_freq: Optional[int] = Field(
        None, description="Every number of steps geometry are saved."
    )
    geometry_units: Optional[str] = Field(
        "angstrom",
        description="Units for atomic geometry. Defaults to Angstroms.",
        dimensionality=LENGTH_DIM,
    )
    velocities_freq: Optional[int] = Field(
        None,
        description="Save velocities every 'velocities_freq' steps.",
    )
    velocities_units: Optional[str] = Field(
        "angstrom/fs",
        description="Units for atomic velocities. Defaults to Angstroms/femtoseconds.",
        dimensionality=LENGTH_DIM / TIME_DIM,
    )
    forces_freq: Optional[int] = Field(
        None, description="Every number of steps velocities are saved."
    )
    forces_units: Optional[str] = Field(
        "kJ/(mol*angstrom)",
        description="Units for atomic forces. Defaults to KiloJoules/mol.Angstroms.",
        dimensionality=MASS_DIM * LENGTH_DIM / (SUBS_DIM * TIME_DIM ** 2),
    )
    freq: Optional[int] = Field(
        None,
        description="Every number of steps geometry, velocities, and/or forces are saved.",
    )
        

class InputMD(InputProc):
    """Basic input model for MD run."""
    """
    # System fields
    """
    system: Dict[Molecule, ForceField] = Field(
        ...,
        description="A mapping of Molecule to its corresponding ForceField object(s).",
    )
    cell: Optional[
        Union[
            Tuple[float, float],
            Tuple[float, float, float, float],
            Tuple[float, float, float, float, float, float],
        ]
    ] = Field(
        None,
        description="Cell dimensions in the form: ((xmin, ymin, ...), (xmax, ymax, ...))",
    )
    boundary: Union[
        Tuple[str, str], Tuple[str, str, str, str], Tuple[str, str, str, str, str, str]
    ] = Field(
        ...,
        description="Boundary conditions in all dimensions e.g. (periodic, periodic) imposes periodic boundaries in 1D.",
    )

    # I/O fields
    trajectory: Optional[Dict[str, InputTraj]] = Field(
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
        None, description="The integrator used for MD simulation. e.g. 'md-vv'"
    )

    # Output control
    freq_write: Optional[Dict[str, int]] = Field(
        None,
        description="The args used to set up the frequency to wirite the system properties such as energies and forces. Requires users to specify according to the engine they choose",
    )

    # Bonded interaction
    unconstrained_start: str = Field(
        None,
        description="To determine if constraints are applied to the initial configuration. It's no by default",
    )  # May be deleted
    constraint_method: str = Field(
        None, description="The algorithm used for constranits. e.g. 'SHAKE'"
    )
    constraints: str = Field(
        None, description="The bonds that are constrained"
    )  # May be replaced by bond_const

    # Nonbonded interaction
    short_forces: Optional[InputForces] = Field(
        None, description="Schema model for computing short-range forces."
    )

    long_forces: Optional[InputForces] = Field(
        None, description="Schema model for computing long-range forces."
    )
    # cut_off: str = Field(..., description="Neighbor searching algorithm")

    # Temperature and pressure coupling
    temp_couple: Optional[Dict[str, Any]] = Field(
        None, description="Temperature coupling args"
    )
    press_couple: Optional[Dict[str, Any]] = Field(
        None, description="Pressure coupling args"
    )
