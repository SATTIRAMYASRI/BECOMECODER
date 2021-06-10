def leaders(n,data):
    leaders_list=""
    for i in range (n-1):
        max_value=max(data[i+1:])
        if data[i]>max_value:
            leaders_list+=str(data[i])+" "
    print(leaders_list+str(data[-1]))
n=int(input())
data=list(map(int,input().split()))
leaders(n,data)

"""
i/p:6
    10 7 8 6 4 5
o/p:10 8 6 5
"""


