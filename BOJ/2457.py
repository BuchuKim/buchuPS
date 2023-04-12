import sys;input=sys.stdin.readline

flower = []
for _ in range(int(input())):
    m1,d1,m2,d2 = map(int,input().split())
    s,e = m1*100+d1,m2*100+d2
    if e>301 and s<1201:
        flower.append([s,e])
flower.sort(key=lambda x : (x[0],x[1]))

if not flower:
    print(0)
    exit()

day,idx = 301,0
ans = 0
while day<=1130:
    found,next_day = False,day
    for i in range(idx,len(flower)):
        # day 이전에 피면서 가장 늦게까지 피어있는 꽃의 index
        if flower[i][0]<=day and flower[i][1]>next_day:
            idx = i
            found,next_day = True,flower[i][1]
    if not found:
        print(0)
        exit()
    ans += 1
    day = next_day
print(ans)
    
