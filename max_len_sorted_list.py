def max_sorted_len(data):
    count=1
    list=[]
    for i in range(n-1):
        if data[i]<data[i+1]:
            count+=1
        if data[i]>data[i+1]:
            list+=[count]
            count=1
    print(max(list+[count]))
            
    
n=int(input())
data=list(map(int,input().split()))
max_sorted_len(data)
'''
8
1 2 3 1 2 3 4 6 --->3 5
5 6 7 8 9 2 3 4---> 5 3
i/p:12
    4 6 3 5 7 9 7 4 2 1 2 3
o/p:4
'''
