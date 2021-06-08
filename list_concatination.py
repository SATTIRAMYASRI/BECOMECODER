n=int(input())
list=[]
required_list=[]
for i in range (1,n+1):
    value=input()
    list=list+[value]
#for i in range (3):
#    required_list=required_list+[list[i]]
#for i in range (3,0,-1):
#    required_list=required_list+[list[n-i]]
#print(required_list)
required_list=list[0:3]+list[n-3:]
print(required_list)
