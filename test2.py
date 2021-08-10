def complete(arr):
    for i in arr:
        if (i!=0):
            return False
    return True
def solution(name):
    li = []
    answer = 0
    for s in name:
        if (s<='M'): # A에서 내려가야돼
            li.append(ord(s)-ord('A'))
        else:
            li.append(ord('Z')-ord(s)+1)
    index = 0
    # 왼쪽? 오른쪽?
    while True:
        answer += li[index]
        li[index] = 0
        if (complete(li)):
            break
        right = index + 1
        left = index - 1
        while (right<len(li) and li[right]==0):
            right += 1
        while (-left<=len(li) and li[left]==0):
            left -= 1
        if (right==len(li)):
            answer = answer + (index - left)
            index = left
        else:
            if (right-index<=index-left):
                answer = answer + (right - index)
                index = right
            else:
                answer = answer + (index - left)
                index = left
    return answer