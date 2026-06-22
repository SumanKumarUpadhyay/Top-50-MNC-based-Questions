# Armstrong Number
def is_armstrong(num):
    total = 0
    nod = len(str(num))
    original = num
    while num > 0:
        digit = num%10
        total += digit**nod
        num //=10
    return total == original 


num = int(input("Enter a number:"))
if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
