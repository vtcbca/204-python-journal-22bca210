#WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
#strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.

def strsymmetric(s):
    a=len(s)//2
    d1=s[0:a]
    d2=s[a:]
    if d1==d2:
        print(f"\"{s}\"  Is Symmetircal  String")
    else:
        print(f"\"{s}\"  Is Not Symmetircal String")
def inputs():
       s=input("Enter String:")        
       strsymmetric(s)
inputs()
