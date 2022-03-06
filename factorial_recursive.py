# def factorial(n):
#     fac=1
#     for i in range(n):
#         fac= fac * (i+1)
#     return fac
# number= int(input("Enter the number = "))
# print("The factorial is = ", factorial(number))
# def factorial_recursive(n):
#   #  if n==1:
#        #return 1
#         if n==1:
#         return n +factorial_recursive (n+m)
# number = int(input("Enter the number = "))
# print("The factorial is = ", factorial_recursive(number))

# Python 3 program to find
# factorial of given number
# def factorial(n):
#     # single line to find factorial
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1);
# num = int(input(print("Enter the number: ")));
# print("Factorial of", num, "is", factorial(num))
# N = int(input())
# count = 0
# while (N > 0):
#     count = count + 1
#     N = N // 10
#     print(count)
# A=[1,8,9,58,52,89,152]
# # for i in A:
import math
number = int(input())
if number > 1:
    for i in range(2, int(math.sqrt(number))):
        if (number % i) == 0:
            print("NO")
            break
        else:
            print("YES")
else:
    print("NO")








