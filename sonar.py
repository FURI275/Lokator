import numpy as np
import matplotlib.pyplot as plt


class Sonar:
    def __init__(self, fd=80000, fs=21000, ti=0.1, d=0.2, c=1500):
        #self.get_coordinates(signals)
        self.fd = fd
        self.fs = fs
        self.ti = ti
        self.d = d
        self.c = c



    def processing(self, signal_left, signal_right):
        spectrum_left = np.fft.fft(signal_left)
        spectrum_right = np.fft.fft(signal_right)

        n = spectrum_left.size
        spectrum_left[int(n / 2):] = 0
        spectrum_right[int(n / 2):] = 0
        z_left = np.fft.ifft(spectrum_left)
        z_right = np.fft.ifft(spectrum_right)
        sigma = np.sqrt(np.sum(np.abs(z_left) ** 2) / n)  # порог
        detection_level = np.where(z_left >= 4 * sigma)  # привышение порога
        distance = ((detection_level[0][0]) / self.fd) * 1500 / 2  # опредение дистанции

        len = spectrum_left.size
        spectrum_left[int(len/2):] = np.complex(0)
        spectrum_right[int(len / 2):] = np.complex(0)

        phi_left= np.angle(signal_left)
        phi_right = np.angle(signal_right)
        dphi=phi_left-phi_right

        dphi[np.where(dphi>np.pi)]-=2*np.pi
        dphi  [np.where(dphi <- np.pi)] += 2 * np.pi
        dphi_mean=sum (dphi)/dphi.size #среднее занчение
        peleng= np.arcsin(self.c*dphi_mean/(2*np.pi*self.fs*self.d))

        print(distance)
        print(peleng*(180/np.pi))
        print(dphi_mean)

