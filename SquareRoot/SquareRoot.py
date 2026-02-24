def squareroot(num):
    a=1
    while a*a< num:
        a+=1
    return a

n=int(input("Enter a number: "))
print("Square root of",n,"is:",squareroot(n))