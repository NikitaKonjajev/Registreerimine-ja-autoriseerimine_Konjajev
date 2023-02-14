from random import *
def kasutajaandmed():
    print("Kas sa tahad oma andmet või random")
    a=input("Mida te soovite: ")
    if a=="oma":
        login=input("Kirjutage teie nimi: ")
        password=input("Kirjutage teie salasõna: ")
    elif a=="random":
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        print(str4)
        ls = list(str4)
        print(ls)
        shuffle(ls)
        print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([choice(ls) for x in range(12)])
        # Пароль готов
        print(psword)
    return login,password
