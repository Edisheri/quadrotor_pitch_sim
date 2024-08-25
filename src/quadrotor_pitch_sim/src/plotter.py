import matplotlib.pyplot as plt
import numpy as np  # Добавьте эту строку

def plot_results(t, theta, omega):
    plt.figure()

    plt.subplot(3, 1, 1)
    plt.plot(t, theta, label='Angular Position (Theta)')
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, omega, label='Angular Velocity (Omega)', color='green')
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t[:-1], np.diff(omega)/np.diff(t), label='Angular Acceleration (Alpha)', color='red')
    plt.legend()
    plt.grid()

    plt.xlabel('Time (s)')
    plt.show()
