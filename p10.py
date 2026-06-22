# gcd of two numbers
def findgcd(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            gcd = i
    return gcd 

a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
print("The gcd of two number is : " , findgcd(a,b))