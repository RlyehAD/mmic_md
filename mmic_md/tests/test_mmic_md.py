"""
Unit and regression test for the mmic_md package.
"""

# Import package, test suite, and other packages as needed
import mmic_md
import pytest
from mmelemental.models import Molecule, ForceField
from mmic.components.blueprints import TacticComponent
from cmselemental.util.decorators import classproperty
import mm_data
from typing import Tuple
import sys
import json


mol_file = mm_data.mols["water-mol.json"]
ff_file = mm_data.ffs["water-ff.json"]


def test_mmic_md_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_md" in sys.modules


def test_mmic_md_models():
    with open(mol_file, "r") as fp:
        mol_data = json.load(fp)
        mol = Molecule(**mol_data) 

    with open(ff_file, "r") as fp:
        ff_data = json.load(fp)
        ff = ForceField(**ff_data)

    inputs = mmic_md.InputMD(
        schema_name="test",
        schema_version=1.0,
        system={mol: ff},
        boundary=(
            "periodic",
            "periodic",
            "periodic",
            "periodic",
            "periodic",
            "periodic",
        ),
        max_steps=20,
        step_size=0.01,
        method="md",
        long_forces={"method": "PME"},
        short_forces={"method": "Cutoff"},
       	temp_couple={"method": "Berendsen", "ref_t": 300},
        press_couple={"method": "no"},
    )

    class MDDummyComponent(TacticComponent):
        @classproperty
        def input(cls):
            return mmic_md.InputMD

        @classproperty
        def output(cls):
            return mmic_md.OutputMD

        @classmethod
        def strategy_comps(cls):
            return mmic_md.MDComponent

        @classproperty
        def version(cls):
            return None

        def execute(
            self,
            inputs: mmic_md.InputMD,
        ) -> Tuple[bool, mmic_md.OutputMD]:

            return (
                True, 
                mmic_md.OutputMD(proc_input=inputs, 
                molecule=mol, 
                schema_name=inputs.schema_name, 
                schema_version=inputs.schema_version, 
                success=True,
                ),
            )

    outputs = MDDummyComponent.compute(inputs)
