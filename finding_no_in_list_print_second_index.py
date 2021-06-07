
n=int(input())
data=list(map(int,input().split()))
no=int(input())
no_count=0
no_index=[]
for i in range (n):
        if no==data[i]:
          no_count+=1
          no_index+=[i]
if no_count>=2:
    print("True")
    print(no_index[1])
else:
    print("False")
#i/p:18
#   1 6 2 3 4 3 2 1 4 5 4 3 2 4 5 1 2 3 
#   3
#0/p:True
#   5         
    
    
