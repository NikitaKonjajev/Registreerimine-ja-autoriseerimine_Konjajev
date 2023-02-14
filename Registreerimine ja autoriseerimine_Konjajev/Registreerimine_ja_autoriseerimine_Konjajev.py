from MyModule import *
#Registreerimine ja autoriseerimine

ll=["user1","user2","user3"]
p=["123","1234","321"]
while True:
    print("Kas sa reg või aut või välja")
    valik=input("Mida te tahate: ")
    if valik=="reg":
         print("Registreerimine")
         login,psword=kasutajaandmed()
         print(f"Teie login ({login}) ja password ({psword})")
    elif valik=="aut":
        print("autoriseerimine") 
        log,pas=aut(ll,p)
    elif valik=="välja":
        print("Nägemist")
        break
        