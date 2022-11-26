import import numpy as np
import matplotlib.pyplot as plt
import water

water = water.Water(fs=20000,ti=1)
class Submarine:
    def __init__(self, x, y, phi, V, time):
        self.update(time)
        self.get_position