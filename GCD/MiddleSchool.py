def prime_factor(num):
    factor=[]
    i=2
    while i<=num:
        if num%i==0:
            factor.append(i)
            num=num//i
        else:
            i+=1
    return factor

def gcd_prime(num1,num2):
    factor1=prime_factor(num1)
    factor2=prime_factor(num2)
    common=[]
    for f in factor1:
        if f in factor2:
            common.append(f)
            factor2.remove(f)
    gcd=1
    for i in common:
        gcd*=i
    return gcd

num1,num2=map(int,input("Enter two numbers: ").split())
gcd=gcd_prime(num1,num2)
print("GCD of",num1,"and",num2,"is:",gcd)