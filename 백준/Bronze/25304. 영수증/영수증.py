x=int(input())
n=int(input())
sum=0

for i in range(1,n+1):
    price,cnt=map(int,input().split())
    sum+=(price*cnt)
    
if x==sum:
    print('Yes')
else:
    print('No')