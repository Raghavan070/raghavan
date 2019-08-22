import math
def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0
a,b=map(int,input().split())
var=int(product(a,b))
root = math.sqrt(var)
if int(root + 0.5) ** 2 == var:
    print("yes")
else:
    print("no")
