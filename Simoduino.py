import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time

Lim = 40

fig, ax = plt.subplots(facecolor = '#333333')
line, = ax.plot([], [], lw=2,  color = 'y')

plt.title('Grafico per il monitoraggio delle magnitudo', color = 'w')

ax.set_facecolor('#333333')

ax.set_ylim(-12000, 12000)
plt.ylabel('Magnitudo', color = 'w')

ax.set_xlim(0, 60)
plt.xlabel('Tempo', color = 'w')

ax.grid()

xdata, ydata = [0]*100, [0]*100
raw = serial.Serial("/dev/ttyACM0",9600)

def update(data):
    line.set_ydata(data)
    return line,

def run(data):
    t,y = data
    del xdata[0]
    del ydata[0]
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

def data_gen():
    t = 0
    while True:
        t += 0.1
        ax.set_xbound(0, Lim)
        try:
            dat = int(raw.readline())
        except:
            dat = 0
        yield t, dat

ani = animation.FuncAnimation(fig, run, data_gen, interval=0)
#plt.pause(0.001)
plt.show(block=True)
