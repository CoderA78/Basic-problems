A=[-3,0,2,6,2,5,7,9,7,5,8,9,6,5,8,7]
LM=[]
LM.append(A[0])
for i in range(1,len(A)):
    LM.append(max(LM[i-1],A[i]))
print(LM)