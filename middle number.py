a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if (a<b) and (b<c):
    print("The middle nimber is",b)
elif (a>b) and (a<c):
        print("The middle nimber is",a)
elif (c>a) and (c<b):
            print("The middle nimber is",c)
    
