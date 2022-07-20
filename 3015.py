import sys;input=sys.stdin.readline
n = int(input())
people = [int(input()) for _ in range(n)]
ans = 0
stack = []
for p in people:
    # stack에 나보다 작은 사람이 있다 -> p는 걔네를 다 볼 수 있어
    while stack and stack[-1][0]<p:
        ans += stack.pop()[1]
    if not stack:
        stack.append([p,1])
        continue
    if stack[-1][0]==p:
        _,cnt = stack.pop()
        ans += cnt
        if stack:
            ans += 1
        stack.append([p,cnt+1])
    else:
        stack.append([p,1])
        ans += 1
print(ans)