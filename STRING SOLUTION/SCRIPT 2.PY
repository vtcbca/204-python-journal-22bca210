#Write a script to enter any sentence and print those word which is palindrom. Also print total number of palindrom word.

def pali(a):
    b=a.split(" ")
    c=0
    d=[]
    for i in b:
        if(i==i[::-1]):
            c=c+1
            d.append(i)
    if c>0:
        print(f'The number of palindrome word in string is {c} and palindromewords are:{d}.')
    else:
        print("There is no palindrome word in string!")
a=input("enter a string:")
pali(a)
