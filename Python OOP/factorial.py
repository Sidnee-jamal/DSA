n=int(input("Enter a number: "))
def factorial(n:int)->int:
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) 
result=factorial(n)
print(f"The factorial of {n} is {result}")

#fibonacci
# def fibonacci(n:int)->int:
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("Enter a number: "))
# result=fibonacci(n)
# print(f"The fibonacci of {n} is {result}")
