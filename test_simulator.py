"""
Tests module
"""
from unittest import TestCase
from dice_simulator import Simulator


class Tests(TestCase):
    """
    Tests class to handle methods for testing program functionality
    """

    def test_dice_roller(self):
        self.assertTrue(isinstance(Simulator().dice_roller(), int))
        self.assertTrue(Simulator().dice_roller() in range(1, 7))
