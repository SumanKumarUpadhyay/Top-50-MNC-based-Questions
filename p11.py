# lcm of two number 
def findlcm(a,b):
    if a>b:
        max = a
    else :
        max = b
    while True:
        if max%a==0 and max%b==0:
            return max
            break
        max +=1

a = int(input("enter a number :"))
b = int(input("Enter second number :"))
print(findlcm(a,b))
    