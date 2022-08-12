import math
a = eval(input("Enter the first no: "))
b = eval(input("Enter the Second no: "))
c = eval(input("Enter the Third no: "))

d = (a+b+c)/2

e = math.sqrt(d*(d-a)*(d-b)*(d-c))
print ("The area of triangle is: ",e)


