""" Populate this file if your translator enables force field conversion """

from typing import Dict, Any, Optional
from mmelemental.models.base import ToolkitModel
from mmelemental.models.forcefield import ForceField
from mmelemental.util.decorators import require


__all__ = ["The_name_of_the_code_to_translate_mmschema_to/from.FF"]


class The_name_of_the_code_to_translate_mmschema_to/from.FF(ToolkitModel):
    """ A model for The name of the code to translate MMSchema to/from. storing forcefield parameters. """

    @property
    @require("The name of the code to translate MMSchema to/from.")
    def dtype(self):
        """ Returns the fundamental forcefield class in The name of the code to translate MMSchema to/from.. """
        import The name of the code to translate MMSchema to/from.

        raise NotImplementedError

    def isvalid(cls, data):
        """ Validates the data object stored in ToolkitModel. """
        raise NotImplementedError

    @classmethod
    @require("The name of the code to translate MMSchema to/from.")
    def from_file(
        cls, filename: str, dtype: str = None, **kwargs: Dict[str, Any]
    ) -> "The_name_of_the_code_to_translate_mmschema_to/from.FF":
        """
        Constructs an instance of The_name_of_the_code_to_translate_mmschema_to/from.FF object from file(s).

        Parameters
        ----------
        filename : str, optional
            The forcefield filename to read
        dtype: str, optional
            The type of file to interpret. If unset, The name of the code to translate MMSchema to/from. attempts to discover dtype from the file extension.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        ForceField
            MMSchema ForceField object.
        """
        import The name of the code to translate MMSchema to/from.

        raise NotImplementedError

    @classmethod
    def from_schema(
        cls, data: ForceField, version: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> "The_name_of_the_code_to_translate_mmschema_to/from.FF":
        """
        Constructs a The_name_of_the_code_to_translate_mmschema_to/from.FF object from an MMSchema ForceField object.
        Parameters
        ----------
        data: ForceField
            Data to construct ForceField from.
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructors.
        Returns
        -------
        The_name_of_the_code_to_translate_mmschema_to/from.FF
            The name of the code to translate MMSchema to/from. forcefield object.
        """
        raise NotImplementedError

    def to_file(self, filename: str, **kwargs):
        """Writes the forcefield to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
        """
        raise NotImplementedError

    def to_schema(self, version: Optional[str] = None, **kwargs) -> ForceField:
        """Converts the The_name_of_the_code_to_translate_mmschema_to/from.FF to MMSchema ForceField.
        Parameters
        ----------
        version: str, optional
            Schema version e.g. 1.0.1
        **kwargs
            Additional kwargs to pass to the constructor.
        """
        raise NotImplementedError
