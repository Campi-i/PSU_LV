lstEmpty = []
suma = 0

while True:

    try:
        
        br = input("Unesite broj koji zelite dodati u listu (napisite Done ako zelite izaci):  ")

        if(br == 'Done'):
            break

        lstEmpty.append(int(br))
        suma += int(br)
        lstEmpty.sort()
    except:
        print("Unijeli ste tip podatka koji nije broj")



print("Korisnik je unio ", len(lstEmpty), " elemenata")

print("Min element liste: ", min(lstEmpty))

print("Max element liste ", max(lstEmpty))

print("Srednja vrijednost liste ", (suma / len(lstEmpty)))

print("Sortirana lista: ", lstEmpty)