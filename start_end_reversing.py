num=input()
start_end_reverse=""
for i in range (len(num)):
    if (i==0):
        start_end_reverse=start_end_reverse+num[len(num)-1]
    elif(i==(len(num)-1)):
        start_end_reverse=start_end_reverse+num[0]    
    else:
        start_end_reverse=start_end_reverse+num[i]
print(start_end_reverse)
        
        
