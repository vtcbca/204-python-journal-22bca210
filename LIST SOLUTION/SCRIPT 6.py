#WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().

def createList():
    p=[]
    n=int(input("How many number you want to enter:"))
    for i in range(n):
        s=int(input("Enter a number:"))
        p.append(s)
    return(p)

def evenodd(p):
    codd=0
    ceven=0
    print("\n\n")
    for i in p:
        if i%2==0:
            print(i)
            ceven=ceven+1
    print("Total even number is:{}\n\n".format(ceven))
    for i in p:
        if i%2!=0:
            print(i)
            codd=codd+1
    print("Total odd number is:{}\n\n".format(codd))
    
p=createList()
evenodd(p)
