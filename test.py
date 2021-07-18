from itertools import permutations
def isSosu(N):
    if (N==0 or N==1):
        return False
    for i in range(2,int(N**0.5)+1):
        if (N%i==0):
            return False
    return True
def solution(numbers):
    answer = 0
    cards = []
    nums = []
    for i in range(1,len(numbers)+1):
        cards += list(permutations(list(numbers),i))
    for i in range(len(cards)):
        nums.append(int("".join(cards[i])))
    nums = set(nums)
    for i in nums:
        if (isSosu(i)):
            answer+=1
    return answer

print(solution("17"))