# check leap year or not 
def check_leap(year):
    if year%400==0:
        print("leap year")
    elif year%100==0:
        print("Not leap year")
    elif year%4==0:
        print("leap year")
    else:
        print("Not a leap year")

year = int(input("Enter a year : "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("Not a leap year")