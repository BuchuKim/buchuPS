import sys;input=sys.stdin.readline
n,k = map(int,input().split())
height = list(map(int,input().split()))
chai = []
for i in range(n-1):
    chai.append(height[i+1]-height[i])
chai.sort(reverse=True)
print(sum(chai[k-1:]))