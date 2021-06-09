def move_zeros(n,data):
    for i in range(n):
        if data[i]==0:
            data.append(0)
            data.remove(0)
n=int(input())
data=list(map(int,input().split()))
move_zeros(n,data)
print(*data)
'''
i/p:6
    1 0 2 0 3 0
o/p:1 2 3 0 0 0
==========
i/p:7
    1 0 0 4 0 5 0
o/p:1 4 5 0 0 0 0
'''
