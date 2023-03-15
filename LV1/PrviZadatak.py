sati = input("Unesite broj radnih sati: ")
placenost = input("Unesite neto placenost sata: ")

def total_euro(x , y):
    return x * y

print("Placa: ", total_euro(int(sati), float(placenost)), "€")
