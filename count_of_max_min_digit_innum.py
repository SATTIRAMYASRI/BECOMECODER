n=input()
max,min,max_count,min_count=0,9,1,1
for i in range (1,len(n)+1):
    if (n[i]>max):
        max=num[i]
        print(max)
    if (n[i]<min):
        min=n[i]
        print(min)
for i in range (1,len(n)+1):
    if (max==n[i]):
        max_count+=1
    if (min==n[i]):
        min_count+=1
print(min_count,max_count)

        

