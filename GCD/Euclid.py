def GCD(m,n):
     m, n= abs(m), abs(n)
     while(n!=0):
          m,n=n,m%n
     return m

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
result= GCD(num1,num2)
print("The GCD of", num1, "and", num2, "is", result)