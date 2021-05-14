n=input()
rev_of_middle_no=""
for i in range (len(n)):
    if (i==0):
        rev_of_middle_no=rev_of_middle_no+n[0]
    elif (i==(len(n)-1)):
        rev_of_middle_no=rev_of_middle_no+n[-1]
    else:
        rev_of_middle_no=rev_of_middle_no+n[(len(n)-1)-i]
print(rev_of_middle_no)
        
    
