import sys;read = sys.stdin.readline
_ = int(read())
arr = list(map(int, read().split()))
arr.sort()

# target 미만의 숫자는 모두 구성할 수 있다고 가정.
target = 1

for n in arr:
    # 갑자기 target보다 큰 n이 들어와버리면 -> target~n을 구성할 수 없다!
    if target < n:
        break
    target += n
print(target)