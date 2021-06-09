def max_sequence_ones(n,data):
    count=1
    list=[]
    for i in range (n-1):
        if data[i]==1 and data[i+1]==1 :
            count+=1
        else:
            list+=[count]
            count=1
    print(max(list))

n=int(input())
data=list(map(int,input().split()))
max_sequence_ones(n,data)
'''
i/p:12
    1 1 1 1 2 1 1 1 2 1 1 1
o/p:4
'''
