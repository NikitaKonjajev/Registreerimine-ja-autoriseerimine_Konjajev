from random import *
def kasutajaandmed(ll:list,p:list):
    print("Kas sa tahad oma andmet või random")
    a=input("Mida te soovite: ")
    if a=="oma":
        login=input("Kirjutage teie nimi: ")      
        psword=input("Kirjutage teie salasõna max 12 värtused: ")
        n=len(psword)
        while n<12:
            psword=input("Teie salasõna on lühike. Palun kirjuta veel: ")
            n=len(psword)
    elif a=="random":
        login=input("Kirjutage teie nimi: ")
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        #print(str4)
        ls = list(str4)
        #print(ls)
        shuffle(ls)
        #print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([choice(ls) for x in range(12)])
    ll.append(login)
    p.append(psword)
    return login,psword
 
def aut(ll:list,p:list):
    print("Kirjutage teie login j salasõna")
    logg=input("Login: ")
    pas_=input("Salasõna: ")
    if logg in ll and pas_ in p:
        print("Tere tulemast!")
    else:
        print("Ebaõiged andmed")
    return logg, pas_