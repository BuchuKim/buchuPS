import sys
from collections import Counter

_ = sys.stdin.readline()
cards = list(map(int,sys.stdin.readline().split()))
_ = sys.stdin.readline()
tofind = list(map(int,sys.stdin.readline().split()))

# 카운터 이용
myCounter = Counter(cards)
answer = []
for c in tofind:
    print(myCounter[c],end=' ')
"""
def BinarySearch(arr,n):
    start = 0
    end = len(arr)-1
    while (start<=end):
        mid = (start+end)//2
        if (arr[mid]>n):
            end = mid - 1
        elif (arr[mid]<n):
            start = mid + 1
        else:
            return mid
    if (start>end):
        return -1
        

N = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

cards.sort()

c = [cards[0]]
nums = []
index = 1
while (index<len(cards)):
    num = 1
    while (cards[index]==cards[index-1]):
        num += 1
        index += 1
        if (index==len(cards)):
            index -=1
            break
    nums.append(num)
    c.append(cards[index])
    index += 1

M = int(sys.stdin.readline())
tofind = list(map(int,sys.stdin.readline().split()))

for i in tofind:
    cardi = BinarySearch(c,i)
    if (cardi<0):
        print(0,end=' ')
    else:
        print(nums[cardi],end=' ')
"""

