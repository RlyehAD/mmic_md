MINT
==============================

# Molecular Dynamics Component

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/RlyehAD/mmic_md/workflows/CI/badge.svg)](https://github.com/RlyehAD/mmic_md/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/RlyehAD/mmic_md/branch/master/graph/badge.svg)](https://codecov.io/gh/RlyehAD/mmic_md/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/RlyehAD/mmic_md.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/RlyehAD/mmic_md/context:python)

This is part of the [MolSSI](http://molssi.org) Molecular Mechanics Interoperable Components ([MMIC](https://github.com/MolSSI/mmic)) project. This package provides a strategy component for running Molecular Dynamics simulations for systems composed by molecules and their forcefields.

## Preparing Input
```python
# Import moleucule and forcefield models
from mmelemental.models import Molecule, ForceField

# Import MD component
import mmic_md

# Construct molecule and forcefield objects
mol = Molecule.from_file(path_to_file)
ff = ForceField.from_file(path_to_file)

# Construct input data model from molecule and forcefield objects
inp = mmic_md.InputMD(
    schema_name=SCHEMA_NAME,
    schema_version=SCHEMA_VERSION,
    system={mol: ff},
    boundary=(
        "periodic",
        "periodic",
        "periodic",
        "periodic",
        "periodic",
        "periodic",
    ),
    max_steps=TOTAL_STEP_NUMBER,
    step_size=STEP_SIZE,
    method="md",
    long_forces={"method": METHOD_FOR_LONGRANGE_INTERACTION},
    short_forces={"method": METHOD_FOR_SHORT_INTERACTION},
    temp_couple={"method": T_COUPLE_METHOD, "ref_t": REFERENCE_T},
    press_couple={"method": P_COUPLE_METHOD},
)	
```

Examples for the Parameters:
*METHOD_FOR_LONGRANGE_INTERACTION*  "PME"
*METHOD_FOR_SHORT_INTERACTION*  "cut-off"
*T_COUPLE_METHOD*  "Berendsen"
*P_COUPLE_METHOD*  "Parrinello-Rahman"

## Runing MD Simulation
```python
# Import strategy compoent for runing MD simulation
from mmic_md.components import MDComponent

# Run MD Simulation
outp = MDComponent.compute(inp)
```

## Extracting Output
```python
# Extract the potential energy 
pot_energy = outp.observables["pot_energy"]
...
```


### Copyright

Copyright (c) 2021, Xu Guo


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 0.0.
