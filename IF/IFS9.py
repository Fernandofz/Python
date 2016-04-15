import math
print ("---------- C9 ------------")
print ("")
op=input("por favor escriba triangulo o circulo para calcular el area: ")
if (op=="triangulo"):
    print("Area del triangulo = (BasexAltura)/2")
    base=input("Ingrese la base: ")
    altura=input("Ingrese la altura: ")
    area=((float(base)*float(altura))/2)
    print(("El area del triangulo es = %.2f")%(area))
elif (op=="circulo"):
    print("Area del circulo = Pi x R^2")
    Radio=input("por favor ingrese el radio del circulo: ")
    area=math.pi*(float(Radio)**2)
    print(("El area del triangulo es = %.2f") % (area))
else:
    print("error no ingreso un dato correcto")
print ("")
print ("---------- FIN ------------")
