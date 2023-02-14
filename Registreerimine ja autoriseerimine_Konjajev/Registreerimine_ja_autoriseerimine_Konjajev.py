from MyModule import *
#Registreerimine ja autoriseerimine

login=[]
password=[]
while True:
    print("Kas sa reg või log või välja")
    valik=input("Mida te tahate: ")
    if valik=="reg":
         print("Registreerimine")
         login,password=kasutajaandmed()
         print("Teie login ja password",login,password)
    elif valik=="aut":
        pass 
    elif valik=="välja":
        print("Nägemist")
        break
        