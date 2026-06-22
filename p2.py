# check prime Number or Not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

num = int(input("Enter a Number:"))
if is_prime(num):
    print("Prime Number")
else:
    print("Not a prime Number")