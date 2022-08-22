import sys;input=sys.stdin.readline
string = input().rstrip()
if string=="P" or string=="PPAP":
    print("PPAP")
    exit()
stack = []
for i in range(len(string)):
    stack.append(string[i])
    if stack[-4:]==['P','P','A','P']:
        for _ in range(3):
            stack.pop()
string = "".join(stack)
if string=="PPAP" or string=="P":
    print("PPAP")
else:
    print("NP")
    