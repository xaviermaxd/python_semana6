temp = int(input("ingrese la tmperatura: "))
if temp <= 10 :
    print("el clima es FRIO")
elif 11 <= temp <= 16 :
    print("el clima es TEMPLADO")
elif 17 <= temp <= 24 :
    print("el clima es CÁLIDO")
else:
    print("el clima es TROPICAL")