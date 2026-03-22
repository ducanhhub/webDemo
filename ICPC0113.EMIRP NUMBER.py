from math import *

def nto(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1
def dx(n):
    tmp = str(n)
    if tmp[::-1] == tmp:
        return False
    return True 

n = int(input())
for i in range(n):
    k = int(input())
    d = []
    vis = [False] * (k + 1)
    for j in range(1,k+1):
        dxj = int(str(j)[::-1])
        if nto(j) and nto(dxj) and dxj <= k and dx(j) and not vis[dxj] and not vis[j]:
            d.append((j,dxj))
            vis[j] = vis[dxj] = True  
    for k in range(len(d)):
        print(*d[k],end = ' ')
    
    print()
    
    