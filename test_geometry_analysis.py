"""
Tests for geometry analysis functions.
"""

import geometry_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    
    assert observed == expected
    
    
# Write a test for the bond_check function. Test that the value 1.0 is evaluated as True

def test_bond_check():
    bond_distance = 1.0
    expected = True
    observed = ga.bond_check(bond_distance)
    
    assert expected == observed
    
def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    
    assert expected == observed
    
def test_bond_check_1p6():
    bond_distance = 1.6
    expected = False
    observed = ga.bond_check(bond_distance)
    
    assert expected == observed
    
    
    
