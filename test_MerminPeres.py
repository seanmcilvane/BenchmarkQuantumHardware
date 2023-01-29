import pytest
from MerminPeres import *
import numpy as np

def test_classical_simulation_mermin_peres():
    
    final_counts = classical_simulation_mermin_peres()
    assert final_counts['0000'] == 9*1024
 
