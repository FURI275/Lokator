import numpy as np
import matplotlib.pyplot as plt



class Water:
    def __init__(self, submarine, objects, fd=80000, fs=21000, ti=0.1, Tc=2, d=0.2):
        self.submarine = submarine
        self.objects = objects
        self.fd = fd
        self.fs = fs
        self.ti = ti
        self.Tc = Tc
        self.d = d

    def get_signal(self, r, phi):
#        [xs, ys] = self.submarine.get_coord()
       # r = 1000
        time = np.arange(0, self.Tc, 1/self.fd)
        signal_left = np.random.randn(time.size)/10
        signal_right = np.random.randn(time.size)/10
        delay = r/1500*2
        dt = self.d/1500*np.sin(phi/180.0*np.pi)
        for i in range(time.size):
            if time[i] > delay and time[i] < delay + self.ti:
                signal_left[i] += np.sin(2*np.pi*self.fs*time[i])
                signal_right[i] += np.sin(2 * np.pi * self.fs * (time[i]-dt))
        plt.plot(time, signal_left, time, signal_right)
        plt.show()
        print(2 * np.pi * self.fs * dt*180/np.pi)
        return ((time, signal_left, signal_right))