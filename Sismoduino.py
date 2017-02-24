import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import serial
# import numpy as np
# import time
import random


# Configurazione grafico
fig, ax = plt.subplots(facecolor='#333333')
line, = ax.plot([], [], lw=2,  color='y')

# Titolo
plt.title('Grafico per il monitoraggio delle magnitudo', color='w')

# Asse X
ax.set_xlim(0, 60)
plt.xlabel('Tempo', color='w')

# Asse y
ax.set_ylim(-12000, 12000)
plt.ylabel('Magnitudo', color='w')

ax.set_facecolor('#333333')
ax.grid()

xdata, ydata = [], []

# Open serial USB
# raw = serial.Serial("/dev/ttyACM0", 9600)


def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)

    return line


def data_gen():
    t = 0

    while True:
        t += 0.2
        ax.set_xlim(t-30, t+30)

        try:
            # val = int(raw.readline())
            val = random.random() * 8000
        except:
            val = 0

        yield t, val


ani = animation.FuncAnimation(fig, run, data_gen, interval=0)
plt.show(block=True)
