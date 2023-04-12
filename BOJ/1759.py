from sys import stdin
from itertools import combinations
L,C = map(int,stdin.readline().split())
# L개로 이뤄지는 암호, 최소 1개의 모음과 2개의 자음
# 알파벳 증가 순서로 이뤄짐
li = list(stdin.readline().split())
mo = []
za = []
for s in li:
    if s in "aeiou":
        mo.append(s)
    else:
        za.appepnd(s)
mo.sort()
za.sort()