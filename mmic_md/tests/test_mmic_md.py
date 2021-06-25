"""
Unit and regression test for the mmic_md package.
"""

# Import package, test suite, and other packages as needed
import mmic_md
import pytest
import sys

def test_mmic_md_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_md" in sys.modules
