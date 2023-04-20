#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF

def evenlenstr(k):
    c=0
    for i in range(5):
       n=input("Enter String : ")
       k.append(n)
    print(k)
    for j in k:
       if len(j)%2==0:
          c+=1
          print(j)
    print(f"Total String With Even Length : {c}")
k=[]
evenlenstr(k)
