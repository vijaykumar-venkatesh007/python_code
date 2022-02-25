x, y = map(int,input().split())
if x>y:
    small = y
else:
    small = x
for i in range(1,small+1):
    if(x%i ==0) and (y%i ==0):
        hcf = i
if hcf == 0:
    print(-1)
else:
    print(hcf)