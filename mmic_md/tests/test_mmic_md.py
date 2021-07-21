"""
Unit and regression test for the mmic_md package.
"""

# Import package, test suite, and other packages as needed
import mmic_md
import pytest
from mmic.components.blueprints import TacticComponent
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

    inputs = mmic_md.MDInput(
        component="mmic_md",
        molecule={"mol": mol},
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
        #freq_write={""},
        long_forces={"method": "PME"},
        short_forces={"method": "Cutoff"},
        cut_off="Verlet",
        t_couple="Berendsen",
        p_couple="no",
        ref_t=300,
    )

    class MDDummyComponent(TacticComponent):
        @classmethod
        def input(cls):
            return mmic_md.MDInput

        @classmethod
        def output(cls):
            return mmic_md.MDOutput

        @classmethod
        def strategy_comp(cls):
            return mmic_md.MDComponent

        @classmethod
        def get_version(cls):
            return None

        def execute(
            self,
            inputs: mmic_md.MDInput,
        ) -> Tuple[bool, mmic_md.MDOutput]:

            return True, mmic_md.MDOutput(proc_input=inputs, molecule=inputs.molecule)

    outputs = MDDummyComponent.compute(inputs)
