def second_max(data):
    max_no=max(data)
    for i in data:
        if i==max_no:
            data.remove(i)
    print(max(data))
n=int(input())
data=list(map(int,input().split()))
second_max(data)
'''
i/p:4
    1 2 3 4
o/p:3
==================
i/p:6
    1 2 3 2 3
o/P:2
==================
FAILED TEST CASE
i/p:6
    1 2 3 2 3 3
o/p:3
'''
