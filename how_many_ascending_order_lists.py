def ascending_order_no(data):
    c=1
    for i in range(n-1):
        if data[i]<data[i+1]:
            pass
        if data[i]>data[i+1]:
            c=c+1
    print(c)
    
n=int(input())
data=list(map(int,input().split()))
ascending_order_no(data)
'''
i/p:12
    4 6 3 5 7 9 7 4 2 1 2 3
    (explanation:4 6, 3 5 7 9, 7 ,4 ,2 ,1 2 3)
o/p:6

i/p:6
    7 6 8 7 9 2
    (explanation:7, 6 8, 7 9 ,2)
o/p:4
'''
