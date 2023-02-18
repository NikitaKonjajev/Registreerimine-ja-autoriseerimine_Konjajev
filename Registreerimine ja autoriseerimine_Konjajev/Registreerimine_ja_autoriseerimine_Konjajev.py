from MyModule import *
#Registreerimine ja autoriseerimine

ll=[]
p=[]
while True:
    print("Kas sa reg või aut või välja")
    valik=input("Mida te tahate: ")
    if valik=="reg":
         print("Registreerimine")
         login,psword=kasutajaandmed(ll,p)
         print(f"Teie login ({login}) ja password ({psword})")
    elif valik=="aut":
        print("autoriseerimine")
        logg,pas_=aut(ll,p)
    elif valik=="välja":
        print("Nägemist")
        break
    print(ll,p)