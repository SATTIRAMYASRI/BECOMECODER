def reverse(data,l,h):
    while(l<h):
        data[l],data[h]=data[h],data[l]
        l+=1
        h-=1
def rotatelist(n,data,r):
    r=r%n
    reverse(data,0,r-1)
    reverse(data,r,n-1)
    reverse(data,0,n-1)
n=int(input())
data=list(map(int,input().split()))
r=int(input())
rotatelist(n,data,r)
print(*data)

'''
i/p:6
    1 2 3 4 5 6
    100
o/p:5 6 1 2 3 4
===================================
i/p:6
    1 2 3 4 5 6
    2
o/p:3 4 5 6 1 2
'''
