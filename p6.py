# check pallindrome number
def is_pallindrome(num):
    start = 0
    end = len(num) - 1
    while start < end:
        if num[start] != num[end]:
            return False
        start +=1
        end -=1
    return True

num = [1,2,3,2,1]
if is_pallindrome(num):
    print("Pallindrome Number")
else:
    print("Not a Pallindrome Number")

