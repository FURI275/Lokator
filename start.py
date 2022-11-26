import numpy as np
import matplotlib.pyplot as plt
import water
import sonar


submarine = 0
objects = []
water = water.Water(submarine, objects)
(time, signal_left, signal_right) = water.get_signal(400, 30)
#plt.plot(time, signal_left)
#plt.show()
distance = sonar.Sonar().processing(signal_left, signal_right)