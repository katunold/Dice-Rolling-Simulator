"""
Module for dice simulation
"""
from random import randint


class Simulator:
    value = None

    def dice_roller(self):
        self.value = randint(1, 6)
        return self.value
