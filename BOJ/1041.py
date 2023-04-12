import sys;read=sys.stdin.readline
from itertools import combinations
n = int(read())
dice = list(map(int,read().split()))
if n==1:
    print(sum(dice)-min(dice))
    exit()
ans = min(dice) * ((n-2)**2) * 5 + min(dice) * (n-2) * 4

index = [0,1,2,3,4,5]
index = combinations(index,2)
two = []
for i in index:
    two.append(dice[i[0]]+dice[i[1]])
two.remove(dice[0]+dice[5])
two.remove(dice[1]+dice[4])
two.remove(dice[2]+dice[3])
ans += min(two) * (n-2) * 4
ans += min(two) * (n-1) * 4

three = [dice[0]+dice[3]+dice[4],dice[0]+dice[1]+dice[2],dice[0]+dice[2]+dice[4],dice[0]+dice[1]+dice[3],
dice[5]+dice[3]+dice[4],dice[5]+dice[1]+dice[2],dice[5]+dice[2]+dice[4],dice[5]+dice[1]+dice[3]]
ans += min(three) * 4

print(ans)