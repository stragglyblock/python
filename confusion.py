a = eval(input("Enter the first side of the triangle : "))
b = eval(input("Enter the second side of the triangle : "))
c = eval(input("Enter the third side of the triangle : "))

if(a==b):
    if(b==a):
        if(a==c):
            if(c==a):
                print("The triangle will be isoscelene")

else:
    print("The triangle will not be right angled ")
    
