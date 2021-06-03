def sumofdigits(n,data):
    list=[]
    for number in data:
        sum=0
        for i in range (len(str(number))):
            sum=sum+number%10
            number=number//10
        list+=[sum]
    print(list)
        
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
