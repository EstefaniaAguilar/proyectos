# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:41:37 2017

@author: 22B
"""



print ("\ncodificador")

cadena = "\nlas palabras se las lleva el viento"
cadena2 = cadena
print ("Mensaje: ",cadena)
##equiva= [["t","0"],["w","2"],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

cadena = cadena.replace("t","0")
cadena = cadena.replace("r","1")
cadena = cadena.replace("w","2")
cadena = cadena.replace("a","3")
cadena = cadena.replace("g","4")
cadena = cadena.replace("m","5")
cadena = cadena.replace("y","6")
cadena = cadena.replace("f","7")
cadena = cadena.replace("p","8")
cadena = cadena.replace("d","9")
cadena = cadena.replace("x","10")
cadena = cadena.replace("b","11")
cadena = cadena.replace("n","12")
cadena = cadena.replace("j","13")
cadena = cadena.replace("z","14")
cadena = cadena.replace("s","15")
cadena = cadena.replace("q","16")
cadena = cadena.replace("v","17")
cadena = cadena.replace("h","18")
cadena = cadena.replace("l","19")
cadena = cadena.replace("c","20")
cadena = cadena.replace("k","21")
cadena = cadena.replace("e","22")


cadena2 = cadena2.replace("0","t")
cadena2 = cadena2.replace("1","r")
cadena2 = cadena2.replace("2","w")
cadena2 = cadena2.replace("3","a")
cadena2 = cadena2.replace("4","g")
cadena2 = cadena2.replace("5","m")
cadena2 = cadena2.replace("6","y")
cadena2 = cadena2.replace("7","f")
cadena2 = cadena2.replace("8","p")
cadena2 = cadena2.replace("9","d")
cadena2 = cadena2.replace("10","x")
cadena2 = cadena2.replace("11","b")
cadena2 = cadena2.replace("12","n")
cadena2 = cadena2.replace("13","j")
cadena2 = cadena2.replace("14","z")
cadena2 = cadena2.replace("15","s")
cadena2 = cadena2.replace("16","q")
cadena2 = cadena2.replace("17","v")
cadena2 = cadena2.replace("18","h")
cadena2 = cadena2.replace("19","l")
cadena2 = cadena2.replace("20","c")
cadena2 = cadena2.replace("21","k")
cadena2 = cadena2.replace("22","e")
    

print (cadena)  
print (cadena2)
def crear():
    archivo = open ('ejercicio3.txt','w')
    archivo.close()
    
def grabar():
    archivo = open ('ejercicio3.txt','a')
    archivo.write('\nmensaje a codificar es:')
    archivo.write('\n')
    archivo.write(cadena2)
    archivo.write('\n')
    archivo.write(cadena)
    archivo.write('\n')
    archivo.write(cadena2)
    

print (crear())  
print (grabar())
    