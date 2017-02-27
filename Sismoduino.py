import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colour import Color
import serial
import json
import numpy as np
import time
from TwitterAPI import TwitterAPI
import datetime

# Configurazione Twitter
try:
    with open('credentials.json') as data_file:
        data = (json.load(data_file))["twitter"]
    api = TwitterAPI(data["key"], data["key_secret"], data["token"], data["token_secret"])
    print("Twitter configurato correttamente")
except:
    print("Si è verificato un errore nella configurazione di twitter")

last_tweet = None

# Configurazione grafico
fig, ax = plt.subplots(facecolor='#191919')
line, = ax.plot([], [], lw=2, color='green')

# Configurazioni colori
c1 = Color('green')
c2 = Color('red')
c_int = list(c1.range_to(c2, 10022))

# Titolo
#plt.title('Grafico per il monitoraggio delle magnitudo', color='w')

# Settaggi asse X
ax.set_xlim(0, 60)
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_alpha(0.1)
ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
for t in ax.xaxis.get_ticklines():
    t.set_color('white')
    t.set_alpha(0.3)

# Settaggi asse y
ax.set_ylim(-12000, 12000)
#plt.ylabel('Magnitudo', color='w')
ax.spines['left'].set_color('white')
ax.spines['right'].set_alpha(0.1)
ax.tick_params(axis='y', colors='white')
for t in ax.yaxis.get_ticklines():
    t.set_color('white')
    t.set_alpha(0.3)

# Colore sfondo e griglia
ax.set_facecolor('#191919')
ax.grid(alpha=0.3)

# Dati iniziali settati a zero
xdata, ydata = [0]*100, [0]*100

# Dichirazione porta seriale per Arduino
raw = serial.Serial("/dev/ttyACM0", 9600)

def tweet(data):
    msg = "Ho appena registrato una magnitudo massima di {0} con #sismoduino".format(data/1000)
    try:
        global last_tweet
        last_tweet = datetime.datetime.now()
        r = api.request('statuses/update', {'status': msg})
    except:
        pass

def update(data):
    line.set_ydata(data)

    return line,

def run(data):
    t, y = data
    del xdata[0]
    del ydata[0]
    xdata.append(t)
    ydata.append(y)

    line.set_data(xdata, ydata)

    # Modifiche valori lungo l'asse Y, la lettera 'M' sta per Magnitudo
    labels_axisy = [item.get_text() for item in ax.get_yticklabels()]
    labels_axisy[1] = '-10M'
    labels_axisy[2] = '-5M'
    labels_axisy[3] = '0M'
    labels_axisy[4] = '5M'
    labels_axisy[5] = '10M'
    ax.set_yticklabels(labels_axisy)

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
    Mag_Max = 0
    while True:
        t += 0.2
        Lim += 0.2
        ax.set_xbound(Lim-20, Lim+20)
        try:
            dat = int(raw.readline())
            # Ottengo la magnitudo massima in una sessione di monitoraggio
            if abs(dat) >= Mag_Max:
                Mag_Max = dat
                Mag_Max = abs(Mag_Max)
                now = datetime.datetime.now()
                plt.tight_layout()
                plt.savefig('PlotSavedImages/MAG_MAX_SISMODUINO.png',
                    bbox_inches='tight',
                    pad_inches=0.1)
                if last_tweet is None or ((now-last_tweet).seconds)/60 >= 5:
                    tweet(Mag_Max)

                print(Mag_Max/1000)
                # PROVE PER LA STAMPA DEL VALORE MASSIMO SUL GRAFICO
                # ISSUE: LAG ESAGERATO CHE PORTA A UN DELAY ASSURDO
                # DEL GRAFICO STESSO, CAN WE IMPROVE THIS FUNCTION?
                # plt.text(0.9, 0.9, Mag_Max,
                #     horizontalalignment='center',
                #     verticalalignment='center',
                #     transform=ax.transAxes,
                #     fontsize=22,
                #     bbox=dict(facecolor='black', alpha=0.5))

        except:
            dat = 0
        yield t, dat

ani = animation.FuncAnimation(fig, run, data_gen, interval=0)
plt.show(block=True)
