#Write a script to enter any word and check it is palindrom or not.

d = input("Enter a word: ")
if d == d[::-1]:
    print(f"{d} is a palindrome.")
else:
    print(f"{d} is not a palindrome.")
