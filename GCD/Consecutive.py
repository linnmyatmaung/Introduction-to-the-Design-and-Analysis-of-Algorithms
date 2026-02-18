def gcd(m,n):
    t=min(m,n)
    while t>0:
        if m%t==0 and n%t==0:
            return t
        t-=1

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
result=gcd(num1,num2)
print("The GCD of", num1, "and", num2, "is", result)