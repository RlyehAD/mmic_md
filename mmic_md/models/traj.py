""" Populate this file if your translator enables trajectory conversion """

from typing import Dict, Any, Optional
from mmelemental.models.base import ToolkitModel
from mmelemental.models.molecule import Molecule
from mmelemental.models.collect import Trajectory
from mmelemental.util.decorators import require


__all__ = ["The_name_of_the_code_to_translate_mmschema_to/from.Traj"]


class The_name_of_the_code_to_translate_mmschema_to/from.Traj(ToolkitModel):
    """ A model for The name of the code to translate MMSchema to/from. storing a trajectory. """

    @property
    @require("The name of the code to translate MMSchema to/from.")
    def dtype(self):
        """ Returns the fundamental molecule class in The name of the code to translate MMSchema to/from.. """
        import The name of the code to translate MMSchema to/from.

        raise NotImplementedError

    def isvalid(cls, data):
        """ Validates the data object stored in ToolkitModel. """
        raise NotImplementedError

    @classmethod
    @require("The name of the code to translate MMSchema to/from.")
    def from_file(
        cls, filename: str, top_filename: str = None, dtype: str = None, **kwargs: Dict[str, Any]
    ) -> "The_name_of_the_code_to_translate_mmschema_to/from.Traj":
        """
        Constructs an instance of The_name_of_the_code_to_translate_mmschema_to/from.Traj object from file(s).

        Parameters
        ----------
        filename : str, optional
            The trajectory filename to read
        top_filename: str, optional
            The topology filename to read
        dtype: str, optional
            The type of file to interpret. If unset, The name of the code to translate MMSchema to/from. attempts to discover dtype from the file extension.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        Trajectory
            MMSchema Trajectory object.
        """
        import The name of the code to translate MMSchema to/from.

        raise NotImplementedError

    @classmethod
    def from_schema(
        cls, data: Trajectory, version: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> "The_name_of_the_code_to_translate_mmschema_to/from.Traj":
        """
        Constructs a The_name_of_the_code_to_translate_mmschema_to/from.Traj object from an MMSchema Trajectory object.
        Parameters
        ----------
        data: Trajectory
            Data to construct Molecule from.
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructors.
        Returns
        -------
        The_name_of_the_code_to_translate_mmschema_to/from.Traj
            The name of the code to translate MMSchema to/from. trajectory object.
        """
        raise NotImplementedError

    def to_file(self, filename: str, **kwargs):
        """Writes the trajectory to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
        """
        raise NotImplementedError

    def to_schema(self, version: Optional[str] = None, **kwargs) -> Trajectory:
        """Converts the The_name_of_the_code_to_translate_mmschema_to/from.Traj to MMSchema Trajectory.
        Parameters
        ----------
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructor.
        """
        raise NotImplementedError
