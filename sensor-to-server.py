import os
import threading
import tailer


def readFileAndSend(f):
    for line in tailer.follow(open(f)):
        #sensor data
        print(line)
        #code to send sensor data to server


#fills array with txt files with sensor data
files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith(".txt")]

ts = []

#creates a thread for each sensor
for file in files:
    taux = threading.Thread(target=readFileAndSend, args=(file,))
    taux.start()
    ts.append(taux)

#current version does not have terminate command
#to exit the process terminate using task manager

