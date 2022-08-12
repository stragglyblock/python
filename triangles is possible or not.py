a = eval(input("Enter the first side = "))
b = eval(input("Enter the second side = "))
c = eval(input("Enter the third side = "))

if(a+b>c):
    if(b+c>a):
        if(c+a>b):
            print("The triangle is possible")
else:
    print("The triangle is not possible")
