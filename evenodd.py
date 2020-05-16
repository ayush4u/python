a=int(input("enter the starting number:"))
b=int(input("enter the ending number:"))
for x in range(a,b):
    if x%2==0:
        print("{} is even".format(x))
    else:
        print("{} is odd".format(x))
