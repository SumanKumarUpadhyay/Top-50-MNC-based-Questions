# largest of three numbers
a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
c = int(input("Enter a third number :"))
if a>b and a>c :
    print("A is largest number")
elif b>a and b>c :
    print("b is largest number")
else:
    print("c is largest number")

print(max(a,b,c))