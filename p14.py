# reverse a sting
def reverse_string(s):
    return s[::-1]

s = input("enter a string:")
print(reverse_string(s))

# 2nd method
def reverse_string(s):
    left = 0
    right = len(s) - 1
    while left <right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    return s 

s = input("enter a string:")
print(reverse_string(s))