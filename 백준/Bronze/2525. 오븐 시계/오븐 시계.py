hour,min=map(int, input().split())
need=int(input())

hour+=need//60
min+=need%60

if min>=60:
    hour+=1
    min-=60
if hour>=24:
    hour-=24
print(hour,min)
    