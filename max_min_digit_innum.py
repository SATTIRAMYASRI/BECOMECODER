n=input()
min=9
max=0
for i in range (1,len(n)+1):
    if (i>max):
        max=i
    if (i<min):
        min=i
print(min,max)
