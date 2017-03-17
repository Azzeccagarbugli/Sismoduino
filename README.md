![Alt text](Sismoduino.jpg?raw=true "Title")
# Sismoduino

Sismoduino è uno strumento realizzato per monitorare l'intensa attività sismica che dal 2016 sta colpendo in modo significativo il territorio italiano.

## Idea e Scopo

L'anno appena trascorso, il 2016, è stato secondo l'Istituto Nazionale di Geologia Italiana l'anno con il maggior numero di scosse registarte. Si parla di cifre davvero terrificanti, circa 53.000, il triplo rispetto al 2015.
La distruzione di intere città e la morte di centinaia di persone sono la conseguenza dello sciame sismico originato il 24 Agosto 2016 alle ore 3:36, quando delle piccole realtà come quelle di Amatrice e Accuomoli sono state rase al suolo in pochi secondi. Da quel momento il centro Italia è stato ogni giorno oggetto di scosse di lieve intensità che ci hanno fatto capire la nostra impotenza di fronte a eventi di tale entità.
In base a questa esperienza ho pensato di costrurire un piccolo Sismografo basato su un microcontrollore noto come Arduino e un accellerometro triassale comprendente un giroscopio, ovvero l'MPU6050, che fosse in grado di rilevare oscillazioni sismiche e monitorarle continuamente, e inoltre, costruire un database grazie ai dati raccolti accesibile da chiunque.
In questo modo è nato Sismoduino.

## Struttura di Sismoduino

La componente informatica ed elettroica è fondamentale in questo progetto. Infatti l'intera struttura si basa su Arduino, un microcontrollore capace di elaborare grandi moli di dati in pochi secondi, moli di dati che vengono ricevute dall'accellerometro MPU6050 che grazie alla formula matematica che descrive l'andamento della magnitudo riesce a convertire le oscillazioni del terreno in valori scalari misurati lungo la scala Richter.

## Installazione

Per provare Sismoduino occorre installare in primo luogo le dipendenze dello script:

`sudo pip install -r requirements.txt`

e in seguito, lanciare lo script stesso in iPython:

`ipython --matplotlib=qt5 Sismoduino.py`

## Ringraziamenti

@Radeox
@lorenzofar
@YelFlash
@sd3ntato
