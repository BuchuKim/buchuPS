import sys;input=sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
if n==1:
    print(1)
    print(li[0])
    exit()
dp = [[1,-1] for i in range(n)]
# dp : [길이,그 전 숫자의 index]
dp[0] = [1,-1]
# ans : [최대 길이, 마지막 숫자의 index]
ans = [0,0]
for i in range(1,n):
    j = i-1
    while j>=0:
        if li[j]<li[i] and dp[j][0]>=dp[i][0]:
            dp[i] = [dp[j][0]+1,j]
        j -= 1
    if dp[i][0]>ans[0]:
        ans = [dp[i][0],i]
i = ans[1]
ansli = []
while i!=-1:
    ansli.append(li[i])
    i = dp[i][1]
print(ans[0])
for i in range(1,len(ansli)+1):
    print(ansli[-i],end=' ')
print()