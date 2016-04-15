print "--------Ejercicio3--------"
print ""
print "-----orden ascendente------"

num1=input("ingrese primer numero ")
num2=input("ingrese segundo numero ")
num3=input("ingrese tercer numero ")

if (num1<num2<num3):
	print ("%s >> %s >> %s") % (num1,num2,num3)
elif (num1<num3<num2):
	print ("%s >> %s >> %s") % (num1,num3,num2)
elif (num2<num1<num3):
	print ("%s >> %s >> %s") % (num2,num1,num3)
elif (num2<num3<num1):
	print ("%s >> %s >> %s") % (num2,num3,num1)
elif (num3<num1<num2):
	print ("%s >> %s >> %s") % (num3,num1,num2)
else:
	print ("%s >> %s >> %s") % (num3,num2,num1)




