while True:
    
    try: 
        br = float(input("Unesite broj u intervalu [0.0, 1.0]"))

        if(br >= 0.0 and br <= 1.0):
            break

        else :
            print("Broj nije u zadanom intervalu")

    except: 
        print("Uneseni podatak nije broj")


if br >= 0.9:
    print("Ocjena A")

elif br >= 0.8:
    print("Ocjena B")

elif br >= 0.7:
    print("Ocjena C")

elif br >= 0.6:
    print("Ocjena D")

else :
    print("Ocjena F")
