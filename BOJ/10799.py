import sys;
arr = list(sys.stdin.readline())[:-1]
ptr = 0
pipe = 0
ans = 0
while (ptr<len(arr)):
    if arr[ptr]=='(':
        if (arr[ptr+1]==')'):
            ans += pipe
            ptr += 1
        else:
            pipe += 1
    else:
        pipe -= 1
    ptr += 1
print(ans)