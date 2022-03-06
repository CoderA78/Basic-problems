# n= int(input("Enter the number="))
# while n==5:
#     print("You have take number five")
#     break
# for
#2
# while i<=10:
#     i += 1
#     if i==6:
#         continue
#     print(i)

#i=0
#while i<=8:
#    print(i)
#        i+=1
# a=25
# b=a**50
# print(b%24)
# a=int
# b=int(a**100)%17
# c=int(a**7)%17
# m= int(a**6)%17
# print(m)
# print(-223%5)

# bank_balance= int(input())
# entries= int(input())
# for i in range(1,entries+1):
#     operations,numbers=input().split()
#     if operations=='1':
#         bank_balance+= int(numbers)
#         print(bank_balance)
#     elif operations=='2':
#         if bank_balance<int(numbers):
#             print('Insufficient Funds')
#         else:
#             bank_balance-=int(numbers)
#             print(bank_balance)
A=[2,9,8,5,6,2,5,7]
even=[]
odd=[]
for i in A:
    if i%2==0:
        even.append(i)
        print(even)
    else:
        odd.append(i)
print(max(even)-min(odd))







