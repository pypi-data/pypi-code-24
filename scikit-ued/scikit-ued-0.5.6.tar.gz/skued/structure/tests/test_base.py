# -*- coding: utf-8 -*-
import pickle
import unittest
from copy import deepcopy
import collections.abc as abc

import numpy as np

from .. import Atom, AtomicStructure

class TestAtomicStructure(unittest.TestCase):

    def setUp(self):
        self.substructure = AtomicStructure(atoms = [Atom('U', [0,0,0])])
        self.structure = AtomicStructure(atoms = [Atom('Ag', [0,0,0]), 
                                                  Atom('Ag', [1,1,1])],
                                         substructures = [self.substructure])
    
    def test_iteration(self):
        """ Test iteration of AtomicStructure yields from orphan atoms and substructure atoms alike """
        elements = [atm.element for atm in self.structure]
        self.assertTrue(len(elements), 3)
    
    def test_length(self):
        """ Test the __len__ methods """
        self.assertTrue(len(self.structure), 3)
    
    def test_containership_substructures(self):
        """ Test that containership works on substructure and atoms separately """
        self.assertIn(self.substructure, self.structure)
        self.assertNotIn(self.structure, self.substructure)
    
    def test_containership_atoms(self):
        """ Test that atom containership testing is working, even in substructures """
        atm = next(iter(self.substructure))
        self.assertIn(atm, self.structure)
    
    def test_equality(self):
        """ Test that AtomicStructure is equal to itself but not others """
        self.assertEqual(self.structure, self.structure)
        self.assertEqual(self.structure, deepcopy(self.structure))
        self.assertNotEqual(self.structure, self.substructure)

    def test_array(self):
        """ Test AtomicStructure.__array__ """
        arr = np.array(self.structure)
        self.assertSequenceEqual(arr.shape, (len(self.structure), 4))

    def test_picklable(self):
        """ Test that Crystal instances can be pickled, and that the unpickled instance
        is identical to the source """
        pickled = pickle.dumps(self.structure)
        unpickled = pickle.loads(pickled)
        self.assertEqual(self.structure, unpickled)
    
    def test_abstract_base_classes(self):
        """ Test that AtomicStructure fits with collections.abc module """
        for abstract_base_class in (abc.Hashable, abc.Iterable, abc.Sized):
            self.assertIsInstance(self.structure, abstract_base_class)

if __name__ == '__main__':
    unittest.main()