def movezeros(n,data):
    i=0
    for j in range (n):
        if data[j]!=0:
            data[i],data[j]=data[j],data[i]
            i=i+1
n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)
''''
i/p:6
    1 0 3 0 0 2
o/p:1 3 2 0 0 0
'''
