import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colour import Color
import serial
import numpy as np
import time

# Configurazione grafico
fig, ax = plt.subplots(facecolor='#333333')
line, = ax.plot([], [], lw=2,  color='green')

# Configurazioni colori
c1 = Color('green')
c2 = Color('red')
c_int = list(c1.range_to(c2, 10022))

# Titolo
plt.title('Grafico per il monitoraggio delle magnitudo', color='w')

# Settaggi asse X
ax.set_xlim(0, 60)
plt.xlabel('Tempo', color='w')
ax.spines['bottom'].set_color('white')
for t in ax.xaxis.get_ticklines():
    t.set_color('white')
    t.set_alpha(0.3)

# Settaggi asse y
ax.set_ylim(-12000, 12000)
plt.ylabel('Magnitudo', color='w')
ax.spines['left'].set_color('white')
for t in ax.yaxis.get_ticklines():
    t.set_color('white')
    t.set_alpha(0.3)

# Colore sfondo e griglia
ax.set_facecolor('#333333')
ax.grid(alpha=0.3)

# Dati iniziali settati a zero
xdata, ydata = [0]*100, [0]*100

# Dichirazione porta seriale per Arduino
raw = serial.Serial("/dev/ttyACM0", 9600)


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

    # Gradiente di colorazione in base al valore della magnitudo
    if abs(y) >= 10022:
        try:
            line.set_color(color=c_int[10021].rgb)
        except:
            pass
    else:
        try:
            line.set_color(color=c_int[abs(y)].rgb)
        except:
            pass

    return line,

def data_gen():
    t = 0
    Lim = 0
    while True:
        t += 0.2
        Lim += 0.2
        ax.set_xbound(Lim-20, Lim+20)
        try:
            dat = int(raw.readline())
        except:
            dat = 0
        yield t, dat

ani = animation.FuncAnimation(fig, run, data_gen, interval=0)
plt.show(block=True)
