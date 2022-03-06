a=[2,8,5,9,7,4,56,9,5,7,4,8]
s=int(input())
e=int(input())
sum=0
for i in range(s,e+1):
    sum+=a[i]
print(sum)