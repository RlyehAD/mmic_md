"""
Unit and regression test for the mmic_md package.
"""

# Import package, test suite, and other packages as needed
import mmic_md
import pytest
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
        mol = json.load(fp)

    with open(ff_file, "r") as fp:
        ff = json.load(fp)

    inputs = mmic_md.InputMD(
        molecule={"mol": mol},
        schema_name="test",
        schema_version=1.0,
        forcefield={"mol": ff},
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

            return True, mmic_md.OutputMD(proc_input=inputs, molecule=inputs.molecule, schema_name=inputs.schema_name, schema_version=inputs.schema_version, success=True)

    outputs = MDDummyComponent.compute(inputs)
