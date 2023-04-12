from sys import stdin
from collections import deque
T = int(stdin.readline())
def D(arr:deque):
    if (len(arr)==0):
        return False
    else:
        arr.popleft()
        return True
def R(arr:deque):
    arr.reverse()

for _ in range(T):
    command = (stdin.readline())[:-1]
    command.replace("RR","")
    done = True
    N = int(stdin.readline())
    l = (stdin.readline())[1:-2]
    if (l==""):
        l = deque([])
    else:
        l = deque(list(map(int,l.split(","))))
    if (N<command.count("D")):
        print("error")
        continue
    for c in command:
        if (c=="D"):
            if (not D(l)):
                print("error")
                done = False
                break
        else:
            R(l)
    if done:
        print("[",end='')
        while (len(l)>0):
            print(l.popleft(),end='')
            if (len(l)==0):
                break
            else:
                print(",",end='')
        print("]")