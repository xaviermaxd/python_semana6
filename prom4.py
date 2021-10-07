angu = int(input("ingrese el angulo: "))
if angu == 0 :
    print("el angulo es nulo")
elif 0 < angu < 90:
    print("el angulo es agudo")
elif angu == 90 :
    print("el angulo es recto")
elif 90 < angu < 180 :
    print("el angulo es obtuso")
elif angu == 180 :
    print("el angulo es llano")
elif 180 < angu < 360 :
    print("el angulo es obtuso")
elif angu == 360 :
    print("el angulo es completo")
else:
    print("error")