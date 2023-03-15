import os
import sys

d1 = input("Unesite prvu datoteku:  ")
d2 = input("Unesite drugu datoteku:  ")

def spam(d):

    dhand = open(os.path.join(sys.path[0], d), "r")

    suma = 0.0
    brojac = 0

    for line in dhand:
        if line.startswith("X-DSPAM-Confidence:"):
            brojac += 1

            podijeljeniString = line.partition("X-DSPAM-Confidence: ")[2]

            suma += float(podijeljeniString[:-2])


    print("Ime datoteke:", d)
    print("Average X-DSPAM-Confidence:", (suma/brojac))

spam(d1)
spam(d2)

    