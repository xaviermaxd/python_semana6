ope = input("ingrese la operacion: ")
a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
if ope == 'S':
    print("la suma es: ",a+b)
elif ope == 'R':
    print("la resta es: ",a-b)
elif ope == 'M':
    print("la multiplicacion es: ",a*b)
elif ope == 'D' and b != 0 :
    print("la division es: ",a/b)
else:
    print("error")
