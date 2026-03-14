# r=float(input("enter the annual interest rate: "))
# t=float(input("enter the time period: "))
# p=float(input("enter the principal amount: "))
# n=int(input("enter the number of times interest is compounded in a time period: "))
# A=p*pow(1+r/n,n*t)
# print(f"the compounded value is {A}")
# r=float(input("enter the annual interest rate: "))
# t=float(input("enter the time period: "))
p,r,t=0,0,0
while p <= 0:
    p=float(input("enter the principal amount: "))
    if(p<=0):
        print("principal cant be less than or equal to zero")
while r <= 0:
    r=float(input("enter the rate: "))
    if(r<=0):
        print("rate cant be less than or equal to zero")
while t <= 0:
    t=int(input("enter the time: "))
    if(t<=0):
        print("time cant be less than or equal to zero")
A=p*pow(1+r/100,t)
print(f"the compounded value is ${A:.2f}")

