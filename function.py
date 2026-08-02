def hello():# this is function definition
    print("Hey Anisha!!, where uh were?")
hello()# this is function call

def mul(number):
    for i in range(1,6):
        cross= print(number*i)
    return cross   
ans = int(input("Enter table number:"))
mul(ans)
#average number
def avg(a,b,c):
    print(a+b+c/3)
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
avg(num1, num2, num3)
# WRITE A FUNCTION OF FACTorial of any number 
#logic 
#  take number n = int(input("Enter any natural number"))
#  mul =1 
# while (i < n+1):
#   mul =mul*i
#   i+=1
# print(mul)
def cal_factorial(a):
    fact =1
    for var in range(1,a+1):
        fact = fact*var
    return fact
n= int(input("Enter your number:"))
print(cal_factorial(n))
