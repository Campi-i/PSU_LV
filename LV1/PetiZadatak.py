import os
import sys

dhand = open(os.path.join(sys.path[0], "song.txt"), "r")

rijeci = {}

for line in dhand:

    r = line.split(" ")

    for a in r: 
    
        nova = a.rstrip('\n')

        bez_zareza = nova.replace(",", "")
        
        if bez_zareza.lower() in rijeci:
            rijeci[bez_zareza.lower()] += 1
        else:
            rijeci[bez_zareza.lower()] = 1

print(rijeci)

print("Rijeci koje se samo jednom pojavljuju: ")

for x in rijeci:
    if(rijeci.get(x) == 1):
        print(x)