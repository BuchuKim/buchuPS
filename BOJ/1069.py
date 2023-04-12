import math
import sys;read=sys.stdin.readline
import math
x,y,d,t = map(int,read().split())
dis = (x**2+y**2)**0.5
sokdo = d/t
time = max(dis//d,1)
ans = min(dis,t*time+abs(dis-d*time),t*(time+1))
print(ans)