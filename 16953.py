from sys import stdin; read=stdin.readline
a,b = map(int,read().split())

def make(_a,_b):
    bfsQ = [[_a,0]]
    while bfsQ:
        V = bfsQ.pop(0)
        if (V[0]==_b):
            return V[1]+1
        double = V[0]*2
        plusOne = int(str(V[0])+"1")
        if (double<=_b):
            bfsQ.append([double,V[1]+1])
        if (plusOne<=_b):
            bfsQ.append([plusOne,V[1]+1])
    return -1

print(make(a,b))
