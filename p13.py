# count vowels and consonents in string 
string = input(str("Enter a string : "))
vowel = 0
consonent = 0

vow = "aeiouAEIOU"
for char in string :
    if char in vow:
        vowel +=1
    else :
        consonent +=1
print("Number of vowels is : " , vowel)
print("Number of consonets is : ", consonent)