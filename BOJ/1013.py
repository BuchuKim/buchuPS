import sys;read=sys.stdin.readline
# (100+1+ | 01)+
ansp = []
for _ in range(int(read())):
    string = read().rstrip()
    ans = False
    i = 0
    # s0: 10 혹은 01
    # s1: 0이 1개 이상
    # s2: 1이 1개 이상
    s = [True,False,False]
    while (i<len(string)):
        if (s[0]):
            # 10 혹은 01이 나와야하는 상태!
            ans = False
            if (i+1>=len(string)):
                break
            if (string[i:i+2]=="01"):
                i += 2
                ans = True
                continue
            elif (string[i:i+2]=="10"):
                s[0] = False
                s[1] = True
                i += 2
                continue
            else:
                break
        elif (s[1]):
            # 0이 1개 이상
            ans = False
            if (string[i]!="0"):
                break
            while (string[i]=="0"):
                i += 1
                if i==len(string):
                    break
            s[1] = False
            s[2] = True
            continue
        elif (s[2]):
            # 1이 1개 이상
            ans = False
            if (string[i]!="1"):
                break
            ans = True
            while (string[i]=="1"):
                i += 1
                if i==len(string):
                    break
            # 현재 i는 "1/0/..."의 index.. 1001? 01?
            if (i+1<len(string) and string[i+1]=="0"):
                i -= 1
            s[2] = False
            s[0] = True
            continue
    if ans:
        ansp.append("YES")
    else:
        ansp.append("NO")
for a in ansp:
    print(ansp)