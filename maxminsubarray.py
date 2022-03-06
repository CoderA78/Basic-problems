A=[-6,5,-6,5,6,9,5,2,4,10]
ans= None
N=len(A)
Amin=min(A)
Amax=max(A)
for i in range(0,N):
    if A[i]==Amin:
        for j in range(i,N):
            if A[j]==Amax:
                ans=min(ans,j-i+1)
                #break
    elif A[i]==Amax:
        for j in range(i,N):
            if A[j]==Amin:
                ans=min(ans,j-i+1)
print(ans)



